from simulation.base import (
    BaseSimulation
)

from simulation.timestep import (
    advance_time
)

from aerospace.aircraft.performance import (
    stall_speed,
    aircraft_thrust_to_weight
)

from aerospace.aircraft.lift import (
    aircraft_lift
)

from aerospace.aircraft.drag import (
    aircraft_drag
)

from aerospace.physics.constants import (
    SEA_LEVEL_AIR_DENSITY
)


class AircraftSimulation(
    BaseSimulation
):

    def __init__(
        self,
        aircraft,
        velocity_ms: float,
        timestep_s: float = 1.0
    ):

        super().__init__(timestep_s)

        self.aircraft = aircraft
        self.velocity_ms = velocity_ms

    def step(self):

        lift = aircraft_lift(
            density=SEA_LEVEL_AIR_DENSITY,
            velocity_ms=self.velocity_ms,
            lift_coefficient=self.aircraft.lift_coefficient,
            wing_area_m2=self.aircraft.wing_area_m2
        )

        drag = aircraft_drag(
            density=SEA_LEVEL_AIR_DENSITY,
            velocity_ms=self.velocity_ms,
            drag_coefficient=self.aircraft.drag_coefficient,
            reference_area_m2=self.aircraft.wing_area_m2
        )

        stall = stall_speed(
            mass_kg=self.aircraft.mass_kg,
            wing_area_m2=self.aircraft.wing_area_m2,
            lift_coefficient=self.aircraft.lift_coefficient
        )

        twr = aircraft_thrust_to_weight(
            thrust_n=self.aircraft.thrust_n,
            mass_kg=self.aircraft.mass_kg
        )

        self.state.time_s = advance_time(
            self.state.time_s,
            self.state.timestep_s
        )

        return {
            "time_s": self.state.time_s,
            "lift_n": lift,
            "drag_n": drag,
            "stall_speed_ms": stall,
            "thrust_to_weight": twr
        }
