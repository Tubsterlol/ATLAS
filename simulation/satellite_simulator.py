from aerospace.satellite.decay import simulate_decay_step
from aerospace.satellite.orbital_parameters import (
    apoapsis,
    orbital_energy,
    orbital_period,
    periapsis,
    semi_major_axis,
)
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

        period = orbital_period(self.state.altitude_m)

        axis = semi_major_axis(self.state.altitude_m)

        energy = orbital_energy(self.state.altitude_m)

        apo = apoapsis(self.state.altitude_m)

        peri = periapsis(self.state.altitude_m)

        return SatelliteResult(
            time_s=self.state.time_s,
            altitude_m=self.state.altitude_m,
            velocity_ms=self.state.velocity_ms,
            drag_force_n=drag,
            decay_rate=decay,
            orbital_period_s=period,
            semi_major_axis_m=axis,
            orbital_energy_j_kg=energy,
            apoapsis_m=apo,
            periapsis_m=peri,
        )
