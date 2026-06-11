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
from aerospace.physics.constants import (
    SEA_LEVEL_AIR_DENSITY,
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
        timestep_s: float = 1.0,
    ):
        super().__init__(timestep_s)

        self.aircraft = aircraft
        self.aircraft_state = initial_state

    def step(self):

        lift = aircraft_lift(
            density=SEA_LEVEL_AIR_DENSITY,
            velocity_ms=self.aircraft_state.velocity_ms,
            lift_coefficient=self.aircraft.lift_coefficient,
            wing_area_m2=self.aircraft.wing_area_m2,
        )

        drag = aircraft_drag(
            density=SEA_LEVEL_AIR_DENSITY,
            velocity_ms=self.aircraft_state.velocity_ms,
            drag_coefficient=self.aircraft.drag_coefficient,
            reference_area_m2=self.aircraft.wing_area_m2,
        )

        stall = stall_speed(
            mass_kg=self.aircraft.mass_kg,
            wing_area_m2=self.aircraft.wing_area_m2,
            lift_coefficient=self.aircraft.lift_coefficient,
        )

        twr = aircraft_thrust_to_weight(
            thrust_n=self.aircraft.thrust_n,
            mass_kg=self.aircraft.mass_kg,
        )

        net_force = self.aircraft.thrust_n - drag

        acceleration = net_force / self.aircraft.mass_kg

        self.aircraft_state.velocity_ms += acceleration * self.state.timestep_s

        self.aircraft_state.velocity_ms = min(
            self.aircraft_state.velocity_ms,
            self.aircraft.max_speed_ms,
        )

        mach = mach_number(
            velocity_ms=self.aircraft_state.velocity_ms,
            temperature_k=288.15,
        )

        reynolds = reynolds_number(
            density=SEA_LEVEL_AIR_DENSITY,
            velocity_ms=self.aircraft_state.velocity_ms,
            characteristic_length_m=self.aircraft.wingspan_m,
        )

        self.state.time_s = advance_time(
            self.state.time_s,
            self.state.timestep_s,
        )

        self.aircraft_state.time_s = self.state.time_s

        return AircraftResult(
            time_s=self.state.time_s,
            velocity_ms=self.aircraft_state.velocity_ms,
            lift_n=lift,
            drag_n=drag,
            stall_speed_ms=stall,
            thrust_to_weight=twr,
            mach=mach,
            reynolds_number=reynolds,
        )
