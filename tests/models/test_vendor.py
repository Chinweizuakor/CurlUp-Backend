"""CurlUp Backend System Vendor Model Tests Module."""

import pytest

from backend.v1.app.models.vendor import BusinessType


@pytest.mark.unit
def test_single_owner_value():
    """
    Test that the value of the SINGLE_OWNER enum member is correct.
    """
    assert BusinessType.SINGLE_OWNER.value == "Single Owner"


@pytest.mark.unit
def test_partnership_value():
    """
    Test that the value of the PARTNERSHIP enum member is correct.
    """
    assert BusinessType.PARTNERSHIP.value == "Partnership"


@pytest.mark.unit
def test_llc_value():
    """
    Test that the value of the LLC enum member is correct.
    """
    assert BusinessType.LLC.value == "Limited Liability Company"


@pytest.mark.unit
def test_all_members_exist():
    """
    Test that all expected members exist in the enum.
    """
    expected_members = {"SINGLE_OWNER", "PARTNERSHIP", "LLC"}
    actual_members = {member.name for member in BusinessType}
    assert actual_members == expected_members


@pytest.mark.unit
def test_member_lookup_by_value():
    """
    Test that you can look up enum members by their value.
    """
    assert BusinessType("Single Owner") == BusinessType.SINGLE_OWNER
    assert BusinessType("Partnership") == BusinessType.PARTNERSHIP
    assert BusinessType("Limited Liability Company") == BusinessType.LLC


@pytest.mark.unit
def test_lookup_invalid_value():
    """
    Test that looking up a non-existent value raises a ValueError.
    """
    with pytest.raises(ValueError):
        BusinessType("Invalid Value")


@pytest.mark.unit
def test_enum_is_iterable():
    """
    Test that the enum is iterable and contains all members.
    """
    members = list(BusinessType)
    assert len(members) == 3
    assert BusinessType.SINGLE_OWNER in members
    assert BusinessType.PARTNERSHIP in members
    assert BusinessType.LLC in members