"""Unit tests for the application module."""

from application import TestMe


def test_take_five():
    """Test that take_five method returns 5."""
    assert TestMe().take_five() == 5


def test_port():
    """Test that port method returns 8000."""
    assert TestMe().port() == 8000