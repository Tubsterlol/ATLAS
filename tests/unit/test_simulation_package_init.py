from simulation import (
    FlapsRetractEvent,
    GearUpEvent,
    MissionEvaluator,
    MissionEvent,
    MissionPhase,
    MissionProfile,
    MissionResult,
    TelemetryRecord,
)


def test_simulation_package_exports():
    assert MissionProfile is not None
    assert MissionEvent is not None
    assert GearUpEvent is not None
    assert FlapsRetractEvent is not None
    assert MissionEvaluator is not None
    assert MissionResult is not None
    assert MissionPhase is not None
    assert TelemetryRecord is not None
