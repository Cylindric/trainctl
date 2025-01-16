"""This module contains example tests."""
from trainctl.trainctl import Trainctl


def test_my_function() -> None:
    """Test the my_function method."""
    trainctl = Trainctl()
    expected = 42
    assert trainctl.my_function() == expected
