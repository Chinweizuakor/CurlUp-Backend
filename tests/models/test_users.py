"""CurlUp Backend System User Model Tests Module."""

import pytest

from backend.v1.app.models.users import Gender, Timezone


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


@pytest.mark.unit
def test_timezone_values():
    """Test that Timezone enum has the correct values."""
    assert Timezone.UTC.value == "UTC"
    assert Timezone.GMT.value == "GMT"
    assert Timezone.EAT.value == "EAT"
    assert Timezone.CAT.value == "CAT"
    assert Timezone.WAT.value == "WAT"
    assert Timezone.EET.value == "EET"
    assert Timezone.CET.value == "CET"
    assert Timezone.AEST.value == "AEST"
    assert Timezone.EST.value == "EST"
    assert Timezone.PST.value == "PST"
    assert Timezone.CST.value == "CST"
    assert Timezone.MST.value == "MST"


@pytest.mark.unit
def test_timezone_names():
    """Test that Timezone enum has the correct names."""
    assert Timezone.UTC.name == "UTC"
    assert Timezone.GMT.name == "GMT"
    assert Timezone.AEST.name == "AEST"


@pytest.mark.unit
def test_timezone_count():
    """Test that Timezone enum has the expected number of members."""
    assert len(Timezone) == 12


@pytest.mark.unit
def test_timezone_instantiation_valid():
    """Test instantiation with valid Timezone values."""
    assert Timezone("UTC") == Timezone.UTC
    assert Timezone("AEST") == Timezone.AEST
    assert Timezone("PST") == Timezone.PST


@pytest.mark.unit
def test_timezone_instantiation_invalid():
    """Test that invalid Timezone values raise ValueError."""
    try:
        Timezone("XYZ")
        raise AssertionError("Expected ValueError for invalid Timezone value")
    except ValueError:
        pass
    try:
        Timezone("utc")  # Case sensitivity check
        assert AssertionError, "Expected ValueError for case-sensitive Timezone value"
    except ValueError:
        pass
