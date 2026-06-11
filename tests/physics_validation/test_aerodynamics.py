from aerospace.physics.aerodynamics import lift_force


def test_positive_lift():

    lift = lift_force(density=1.225, velocity=100, lift_coefficient=1.2, wing_area=20)

    assert lift > 0
