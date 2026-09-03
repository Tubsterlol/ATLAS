import logging

from aerospace.satellite.orbital.groundtrack import groundtrack_position
from aerospace.satellite.orbital.orbital_motion import advance_true_anomaly
from aerospace.satellite.orbital.orbital_parameters import (
    apoapsis,
    orbital_energy,
    orbital_period,
    periapsis,
    semi_major_axis,
)
from aerospace.satellite.perturbations.decay import simulate_decay_step
from simulation.core.base import BaseSimulation
from simulation.core.results import SatelliteResult
from simulation.core.state import SatelliteState
from simulation.core.timestep import advance_time
from simulation.satellite.mission_profile import SatelliteMissionProfile

logger = logging.getLogger(__name__)


class SatelliteSimulation(BaseSimulation):
    def __init__(
        self,
        satellite,
        initial_state: SatelliteState,
        profile=None,
        maneuvers=None,
        timestep_s: float = 1.0,
    ):
        super().__init__(timestep_s)

        self.satellite = satellite
        self.satellite_state = initial_state

        self.profile = profile or SatelliteMissionProfile(maneuvers=maneuvers)
        logger.info(
            "Initialized satellite simulation for %s with a %.3f s timestep",
            satellite.name,
            timestep_s,
        )

    def step(self):
        self.profile.update(self.satellite_state)
        result = simulate_decay_step(
            altitude_m=self.satellite_state.altitude_m,
            mass_kg=self.satellite.mass_kg,
            drag_coefficient=self.satellite.drag_coefficient,
            cross_sectional_area_m2=self.satellite.cross_sectional_area_m2,
            timestep_s=self.state.timestep_s,
        )

        self.satellite_state.altitude_m = result["altitude_m"]
        self.satellite_state.velocity_ms = result["velocity_ms"]

        self.state.time_s = advance_time(
            self.state.time_s,
            self.state.timestep_s,
        )

        self.satellite_state.time_s = self.state.time_s

        altitude = self.satellite_state.altitude_m

        period = orbital_period(altitude)

        self.satellite_state.true_anomaly_deg = advance_true_anomaly(
            true_anomaly_deg=self.satellite_state.true_anomaly_deg,
            orbital_period_s=period,
            timestep_s=self.state.timestep_s,
        )

        latitude_deg, longitude_deg = groundtrack_position(
            true_anomaly_deg=self.satellite_state.true_anomaly_deg,
            inclination_deg=self.satellite_state.inclination_deg,
        )

        axis = semi_major_axis(altitude)
        energy = orbital_energy(altitude)
        apo = apoapsis(altitude)
        peri = periapsis(altitude)

        self.satellite_state.semi_major_axis_m = axis
        self.satellite_state.orbital_period_s = period
        self.satellite_state.orbital_energy_j_kg = energy
        self.satellite_state.apoapsis_m = apo
        self.satellite_state.periapsis_m = peri
        self.satellite_state.latitude_deg = latitude_deg
        self.satellite_state.longitude_deg = longitude_deg

        return SatelliteResult(
            satellite_name=self.satellite_state.satellite_name,
            time_s=self.state.time_s,
            altitude_m=altitude,
            velocity_ms=self.satellite_state.velocity_ms,
            phase=self.satellite_state.phase,
            drag_force_n=result["drag_force_n"],
            decay_rate=result["decay_rate"],
            orbital_period_s=period,
            semi_major_axis_m=axis,
            orbital_energy_j_kg=energy,
            apoapsis_m=apo,
            periapsis_m=peri,
            inclination_deg=self.satellite_state.inclination_deg,
            eccentricity=self.satellite_state.eccentricity,
            true_anomaly_deg=self.satellite_state.true_anomaly_deg,
            latitude_deg=latitude_deg,
            longitude_deg=longitude_deg,
        )
