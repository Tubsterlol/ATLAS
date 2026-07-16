from aerospace.aircraft.drag import aircraft_drag
from aerospace.aircraft.flight_conditions import (
    mach_number,
    reynolds_number,
)
from aerospace.aircraft.geometry_calculations import aspect_ratio
from aerospace.aircraft.induced_drag import induced_drag_coefficient
from aerospace.aircraft.lift import aircraft_lift
from aerospace.aircraft.lift_curve import lift_coefficient
from aerospace.aircraft.performance import (
    aircraft_thrust_to_weight,
    stall_speed,
)
from aerospace.aircraft.trim import trim_angle_of_attack
from aerospace.aircraft.wave_drag import wave_drag_coefficient
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

        required_lift = effective_mass * EARTH_STANDARD_GRAVITY

        self.aircraft_state.alpha_deg = trim_angle_of_attack(
            required_lift_n=required_lift,
            density=density,
            velocity_ms=self.aircraft_state.velocity_ms,
            wing_area_m2=self.aircraft.geometry.wing_area_m2,
        )

        cl = lift_coefficient(
            self.aircraft_state.alpha_deg,
        )

        ar = aspect_ratio(
            wing_span_m=self.aircraft.geometry.wing_span_m,
            wing_area_m2=self.aircraft.geometry.wing_area_m2,
        )

        cdi = induced_drag_coefficient(
            lift_coefficient=cl,
            aspect_ratio=ar,
        )

        mach = mach_number(
            velocity_ms=self.aircraft_state.velocity_ms,
            temperature_k=temperature,
        )

        wave_cd = wave_drag_coefficient(
            mach,
        )

        total_cd = self.aircraft.drag_coefficient + cdi + wave_cd

        lift = aircraft_lift(
            density=density,
            velocity_ms=self.aircraft_state.velocity_ms,
            wing_area_m2=self.aircraft.geometry.wing_area_m2,
            lift_coefficient=cl,
        )

        drag = aircraft_drag(
            density=density,
            velocity_ms=self.aircraft_state.velocity_ms,
            drag_coefficient=total_cd,
            reference_area_m2=self.aircraft.geometry.wing_area_m2,
        )

        stall = stall_speed(
            mass_kg=effective_mass,
            wing_area_m2=self.aircraft.geometry.wing_area_m2,
            lift_coefficient=cl,
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

        reynolds = reynolds_number(
            density=density,
            velocity_ms=self.aircraft_state.velocity_ms,
            characteristic_length_m=self.aircraft.geometry.mean_chord_m,
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
            alpha_deg=self.aircraft_state.alpha_deg,
            lift_coefficient=cl,
            drag_coefficient=total_cd,
            induced_drag_coefficient=cdi,
            aspect_ratio=ar,
            wave_drag_coefficient=wave_cd,
        )
