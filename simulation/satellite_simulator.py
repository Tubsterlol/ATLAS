from aerospace.satellite.decay import simulate_decay_step
from aerospace.satellite.groundtrack import groundtrack_position
from aerospace.satellite.maneuvers import orbit_raise
from aerospace.satellite.orbital_motion import advance_true_anomaly
from aerospace.satellite.orbital_parameters import (
    apoapsis,
    orbital_energy,
    orbital_period,
    periapsis,
    semi_major_axis,
)
from simulation.base import BaseSimulation
from simulation.maneuvers import (
    OrbitRaiseManeuver,
    StationKeepingManeuver,
)
from simulation.results import SatelliteResult
from simulation.state import SatelliteState
from simulation.station_keeping import station_keep
from simulation.timestep import advance_time


class SatelliteSimulation(BaseSimulation):
    def __init__(
        self,
        satellite,
        initial_state: SatelliteState,
        maneuvers=None,
        timestep_s: float = 1.0,
    ):
        super().__init__(timestep_s)

        self.satellite = satellite
        self.satellite_state = initial_state

        self.maneuvers = maneuvers or []
        self.executed_maneuvers = set()

    def step(self):

        result = simulate_decay_step(
            altitude_m=self.satellite_state.altitude_m,
            mass_kg=self.satellite.mass_kg,
            drag_coefficient=self.satellite.drag_coefficient,
            cross_sectional_area_m2=self.satellite.cross_sectional_area_m2,
            timestep_s=self.state.timestep_s,
        )

        self.satellite_state.altitude_m = result["altitude_m"]
        self.satellite_state.velocity_ms = result["velocity_ms"]

        for index, maneuver in enumerate(self.maneuvers):
            if isinstance(maneuver, OrbitRaiseManeuver):
                if (
                    index not in self.executed_maneuvers
                    and self.state.time_s >= maneuver.time_s
                ):
                    self.satellite_state.altitude_m = orbit_raise(
                        altitude_m=self.satellite_state.altitude_m,
                        delta_v_ms=maneuver.delta_v_ms,
                    )

                    self.executed_maneuvers.add(index)

            elif isinstance(maneuver, StationKeepingManeuver):
                self.satellite_state.altitude_m = station_keep(
                    current_altitude_m=self.satellite_state.altitude_m,
                    target_altitude_m=maneuver.target_altitude_m,
                    tolerance_m=maneuver.tolerance_m,
                )

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
        self.satellite_state.latitude_deg = latitude_deg
        self.satellite_state.longitude_deg = longitude_deg

        return SatelliteResult(
            satellite_name=self.satellite_state.satellite_name,
            time_s=self.state.time_s,
            altitude_m=altitude,
            velocity_ms=self.satellite_state.velocity_ms,
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
