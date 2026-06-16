from aerospace.aircraft.drag import aircraft_drag
from aerospace.aircraft.flight_conditions import (
    mach_number,
    reynolds_number,
)
from aerospace.aircraft.lift import aircraft_lift
from aerospace.aircraft.performance import (
    aircraft_thrust_to_weight,
    stall_speed,
)
from aerospace.atmosphere.isa import (
    isa_density,
    isa_temperature,
)
from aerospace.navigation.navigation import update_position
from aerospace.physics.constants import (
    EARTH_STANDARD_GRAVITY,
)
from simulation.base import BaseSimulation
from simulation.results import AircraftResult
from simulation.state import AircraftState
from simulation.timestep import advance_time


class AircraftSimulation(BaseSimulation):
    def __init__(
        self,
        aircraft,
        initial_state: AircraftState,
        profile=None,
        timestep_s: float = 1.0,
    ):
        super().__init__(timestep_s)

        self.aircraft = aircraft
        self.aircraft_state = initial_state
        self.profile = profile

    def step(self):

        if self.profile:
            self.profile.update(self.aircraft_state)

        density = isa_density(self.aircraft_state.altitude_m)

        temperature = isa_temperature(self.aircraft_state.altitude_m)

        effective_mass = self.aircraft.mass_kg + self.aircraft_state.fuel_kg

        lift = aircraft_lift(
            density=density,
            velocity_ms=self.aircraft_state.velocity_ms,
            lift_coefficient=self.aircraft.lift_coefficient,
            wing_area_m2=self.aircraft.wing_area_m2,
        )

        drag = aircraft_drag(
            density=density,
            velocity_ms=self.aircraft_state.velocity_ms,
            drag_coefficient=self.aircraft.drag_coefficient,
            reference_area_m2=self.aircraft.wing_area_m2,
        )

        stall = stall_speed(
            mass_kg=effective_mass,
            wing_area_m2=self.aircraft.wing_area_m2,
            lift_coefficient=self.aircraft.lift_coefficient,
        )

        twr = aircraft_thrust_to_weight(
            thrust_n=self.aircraft.thrust_n,
            mass_kg=effective_mass,
        )

        climb_force = (
            effective_mass * EARTH_STANDARD_GRAVITY * self.aircraft_state.climb_rate_ms
        ) / max(
            self.aircraft_state.velocity_ms,
            1.0,
        )

        net_force = self.aircraft.thrust_n - drag - climb_force

        acceleration = net_force / effective_mass

        self.aircraft_state.velocity_ms += acceleration * self.state.timestep_s

        self.aircraft_state.velocity_ms = min(
            self.aircraft_state.velocity_ms,
            self.aircraft.max_speed_ms,
        )

        mach = mach_number(
            velocity_ms=self.aircraft_state.velocity_ms,
            temperature_k=temperature,
        )

        reynolds = reynolds_number(
            density=density,
            velocity_ms=self.aircraft_state.velocity_ms,
            characteristic_length_m=self.aircraft.wingspan_m,
        )

        fuel_used = self.aircraft.fuel_burn_kg_s * self.state.timestep_s

        self.aircraft_state.fuel_kg = max(
            0.0,
            self.aircraft_state.fuel_kg - fuel_used,
        )

        self.aircraft_state.altitude_m += (
            self.aircraft_state.climb_rate_ms * self.state.timestep_s
        )

        self.aircraft_state.altitude_m = max(
            0.0,
            self.aircraft_state.altitude_m,
        )

        self.state.time_s = advance_time(
            self.state.time_s,
            self.state.timestep_s,
        )

        self.aircraft_state.time_s = self.state.time_s

        self.aircraft_state.x_m, self.aircraft_state.y_m = update_position(
            x_m=self.aircraft_state.x_m,
            y_m=self.aircraft_state.y_m,
            velocity_ms=self.aircraft_state.velocity_ms,
            heading_deg=self.aircraft_state.heading_deg,
            timestep_s=self.state.timestep_s,
        )

        return AircraftResult(
            time_s=self.state.time_s,
            altitude_m=self.aircraft_state.altitude_m,
            velocity_ms=self.aircraft_state.velocity_ms,
            lift_n=lift,
            drag_n=drag,
            stall_speed_ms=stall,
            thrust_to_weight=twr,
            mach=mach,
            reynolds_number=reynolds,
            density=density,
            temperature_k=temperature,
            fuel_kg=self.aircraft_state.fuel_kg,
            effective_mass_kg=effective_mass,
            phase=self.aircraft_state.phase,
            x_m=self.aircraft_state.x_m,
            y_m=self.aircraft_state.y_m,
            heading_deg=self.aircraft_state.heading_deg,
        )
