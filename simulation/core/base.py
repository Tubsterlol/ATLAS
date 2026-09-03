from simulation.core.state import SimulationState


class BaseSimulation:
    def __init__(self, timestep_s: float = 1.0):
        self.state = SimulationState(timestep_s=timestep_s)

    def step(self):
        raise NotImplementedError

    def run_step_count(self, steps: int):
        if not isinstance(steps, int) or isinstance(steps, bool) or steps < 0:
            raise ValueError(f"steps must be a non-negative integer; got {steps!r}")

        results = []

        for _ in range(steps):
            if not self.state.running:
                break

            results.append(self.step())

        return results
