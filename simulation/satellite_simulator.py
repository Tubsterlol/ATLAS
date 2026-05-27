from simulation.base import (
    BaseSimulation
)

from simulation.timestep import (
    advance_time
)

from aerospace.satellite.decay import (
    simulate_decay_step
)


class SatelliteSimulation(
    BaseSimulation
):

    def __init__(
        self,
        satellite,
        timestep_s: float = 1.0
    ):

        super().__init__(timestep_s)

        self.satellite = satellite

    def step(self):

        result = simulate_decay_step(
            satellite=self.satellite,
            timestep_s=self.state.timestep_s
        )

        self.state.time_s = advance_time(
            self.state.time_s,
            self.state.timestep_s
        )

        result["time_s"] = (
            self.state.time_s
        )

        return result
