from aerospace.satellite.decay import simulate_decay_step
from simulation.base import BaseSimulation
from simulation.results import SatelliteResult
from simulation.timestep import advance_time


class SatelliteSimulation(BaseSimulation):
    def __init__(self, satellite, timestep_s: float = 1.0):

        super().__init__(timestep_s)

        self.satellite = satellite

    def step(self):

        result = simulate_decay_step(
            satellite=self.satellite, timestep_s=self.state.timestep_s
        )

        self.state.time_s = advance_time(self.state.time_s, self.state.timestep_s)

        return SatelliteResult(
            time_s=self.state.time_s,
            altitude_m=result["altitude_m"],
            velocity_ms=result["velocity_ms"],
            drag_force_n=result["drag_force_n"],
            decay_rate=result["decay_rate"],
        )
