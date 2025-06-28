"""CurlUp Backend System Client Model Tests Module."""

import pytest

from backend.v1.app.models.client import Gender


@pytest.mark.unit
def test_gender_enum_values():
    assert Gender.MALE.value == "Male"
    assert Gender.FEMALE.value == "Female"


@pytest.mark.unit
def test_gender_names():
    """Test that Gender enum has the correct names."""
    assert Gender.MALE.name == "MALE"
    assert Gender.FEMALE.name == "FEMALE"


@pytest.mark.unit
def test_gender_count():
        """Test that Gender enum has the expected number of members."""
        assert len(Gender) == 2


@pytest.mark.unit
def test_gender_instantiation_valid():
    """Test instantiation with valid Gender values."""
    assert Gender("Male") == Gender.MALE
    assert Gender("Female") == Gender.FEMALE


@pytest.mark.unit
def test_gender_instantiation_invalid():
    """Test that invalid Gender values raise ValueError."""
    try:
        Gender("Other")
        raise AssertionError("Expected ValueError for invalid Gender value")
    except ValueError:
        pass
    try:
        Gender("male")  # Case sensitivity check
        raise AssertionError("Expected ValueError for case-sensitive Gender value")
    except ValueError:
        pass
