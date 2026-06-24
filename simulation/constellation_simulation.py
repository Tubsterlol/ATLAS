class ConstellationSimulation:
    def __init__(self, simulations):
        self.simulations = simulations

    def run_step_count(self, steps):

        results = []

        for _ in range(steps):
            for simulation in self.simulations:
                results.append(simulation.step())

        return results
