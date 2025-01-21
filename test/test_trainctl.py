"""This module contains example tests."""
from trainctl.test import Trainctl


def test_my_function() -> None:
    """Test the my_function method."""
    trainctl = Trainctl()
    expected = 42
    assert trainctl.my_function() == expected
