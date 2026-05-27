from dataclasses import dataclass


@dataclass
class SimulationState:
    time_s: float = 0.0
    timestep_s: float = 1.0
    running: bool = True
