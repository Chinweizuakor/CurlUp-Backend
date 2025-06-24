"""CurlUp Backend System User Model Tests Module."""

from datetime import date

import pytest
from pydantic import ValidationError

from backend.v1.app.models.users import Gender, Timezone, UserBase, UserLogin


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


@pytest.mark.unit
@pytest.mark.parametrize(
    "data, should_raise, error_message",
    [
        # Valid cases
        (
            {"username": "testuser", "password": "securepass123"},
            False,
            None,
        ),
        (
            {"email": "test@example.com", "password": "securepass123"},
            False,
            None,
        ),
        # Invalid cases: Neither username nor email provided
        (
            {"password": "securepass123"},
            True,
            "Exactly one of username or email must be provided",
        ),
        # Invalid cases: Both username and email provided
        (
            {"username": "testuser", "email": "test@example.com", "password": "securepass123"},
            True,
            "Exactly one of username or email must be provided",
        ),
        # Invalid cases: Invalid email format
        (
            {"email": "invalid-email", "password": "securepass123"},
            True,
            "value is not a valid email address",
        ),
        # Invalid cases: None for password
        (
            {"username": "testuser", "password": None},
            True,
            "Input should be a valid string",
        ),
        # Edge cases: Empty strings
        (
            {"username": "", "password": "securepass123"},
            False,
            None,  # Empty username is allowed by the model
        ),
        (
            {"email": "", "password": "securepass123"},
            True,
            "value is not a valid email address",
        ),
        (
            {"username": "testuser", "password": ""},
            False,
            None,  # Empty password is allowed by the model
        ),
    ],
)
def test_user_login_validation(data, should_raise, error_message):
    if should_raise:
        with pytest.raises(ValidationError) as exc_info:
            UserLogin(**data)
        # Check for specific error message as a substring
        if error_message:
            assert error_message.lower() in str(exc_info.value).lower()
    else:
        # Should not raise an error
        user = UserLogin(**data)
        # Verify the fields are set correctly
        assert user.username == data.get("username")
        assert user.email == data.get("email")
        assert user.password == data["password"]


@pytest.mark.unit
@pytest.mark.parametrize(
    "username, email, password",
    [
        ("testuser", None, "securepass123"),
        (None, "test@example.com", "securepass123"),
    ],
)
def test_user_login_valid_combinations(username, email, password):
    """Test valid combinations of username or email."""
    data = {"username": username, "email": email, "password": password}
    user = UserLogin(**data)
    assert user.username == username
    assert user.email == email
    assert user.password == password


@pytest.mark.unit
def test_user_login_exactly_one_identifier():
    """Test that exactly one of username or email is required."""
    # Test neither provided
    with pytest.raises(ValidationError) as exc_info:
        UserLogin(password="securepass123")
    assert "exactly one of username or email must be provided" in str(exc_info.value).lower()

    # Test both provided
    with pytest.raises(ValidationError) as exc_info:
        UserLogin(username="testuser", email="test@example.com", password="securepass123")
    assert "exactly one of username or email must be provided" in str(exc_info.value).lower()


@pytest.mark.unit
@pytest.mark.parametrize(
    "data, should_raise, error_message",
    [
        # Valid case: All required fields, no optional fields
        (
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "username": "johndoe",
                "gender": Gender.MALE,
                "dateofbirth": date(1990, 1, 1),
                "mobile": "1234567890",
            },
            False,
            None,
        ),
        # Valid case: All fields including optional
        (
            {
                "first_name": "Jane",
                "middle_name": "Marie",
                "last_name": "Smith",
                "email": "jane.smith@example.com",
                "username": "janesmith",
                "gender": Gender.FEMALE,
                "dateofbirth": date(1985, 5, 15),
                "timezone": Timezone.UTC,
                "mobile": "9876543210",
            },
            False,
            None,
        ),
        # Valid case: Optional fields explicitly None
        (
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "username": "johndoe",
                "gender": Gender.MALE,
                "dateofbirth": date(1990, 1, 1),
                "mobile": "1234567890",
                "middle_name": None,
                "timezone": None,
            },
            False,
            None,
        ),
        # Invalid case: Missing required field (first_name)
        (
            {
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "username": "johndoe",
                "gender": Gender.MALE,
                "dateofbirth": date(1990, 1, 1),
                "mobile": "1234567890",
            },
            True,
            "Field required",
        ),
        # Edge case: Empty string for required field (username) is allowed by the model
        (
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "username": "",
                "gender": Gender.MALE,
                "dateofbirth": date(1990, 1, 1),
                "mobile": "1234567890",
            },
            True,
            None,
        ),
        # Invalid case: Invalid email format
        (
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "invalid-email",
                "username": "johndoe",
                "gender": Gender.MALE,
                "dateofbirth": date(1990, 1, 1),
                "mobile": "1234567890",
            },
            True,
            "value is not a valid email address",
        ),
        # Invalid case: Invalid gender value
        (
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "username": "johndoe",
                "gender": "OTHER",
                "dateofbirth": date(1990, 1, 1),
                "mobile": "1234567890",
            },
            True,
            "Input should be 'Male' or 'Female'",
        ),
        # Invalid case: Invalid date format
        (
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "username": "johndoe",
                "gender": Gender.MALE,
                "dateofbirth": "1990-13-01",  # Invalid month
                "mobile": "1234567890",
            },
            True,
            "Input should be a valid date",
        ),
        # Invalid case: Invalid timezone value
        (
            {
                "first_name": "John",
                "middle_name": "Marie",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "username": "johndoe",
                "gender": Gender.MALE,
                "dateofbirth": date(1990, 1, 1),
                "timezone": "Invalid/Zone",
                "mobile": "1234567890",
            },
            True,
            (
                "Input should be 'UTC', 'GMT', 'EAT', 'CAT', 'WAT', 'EET', 'CET', 'AEST', "
                "'EST', 'PST', 'CST' or 'MST'"
            ),
        ),
        # Invalid case: None for required field (mobile)
        (
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
                "username": "johndoe",
                "gender": Gender.MALE,
                "dateofbirth": date(1990, 1, 1),
                "mobile": None,
            },
            True,
            "Input should be a valid string",
        ),
    ],
)
def test_user_base_validation(data, should_raise, error_message):
    if should_raise:
        with pytest.raises(ValidationError) as exc_info:
            UserBase(**data)
        # Check for specific error message as a substring
        if error_message:
            assert error_message.lower() in str(exc_info.value).lower()
    else:
        # Should not raise an error
        user = UserBase(**data)
        # Verify fields are set correctly
        assert user.first_name == data["first_name"]
        assert user.middle_name == data.get("middle_name")
        assert user.last_name == data["last_name"]
        assert user.email == data["email"]
        assert user.username == data["username"]
        assert user.gender == data["gender"]
        assert user.dateofbirth == data["dateofbirth"]
        assert user.timezone == data.get("timezone")
        assert user.mobile == data["mobile"]


@pytest.mark.parametrize(
    "first_name, middle_name, last_name, email, username, gender, dateofbirth, timezone, mobile",
    [
        (
            "John",
            None,
            "Doe",
            "john.doe@example.com",
            "johndoe",
            Gender.MALE,
            date(1990, 1, 1),
            None,
            "1234567890",
        ),
        (
            "Jane",
            "Marie",
            "Smith",
            "jane.smith@example.com",
            "janesmith",
            Gender.FEMALE,
            date(1985, 5, 15),
            Timezone.CST,
            "9876543210",
        ),
    ],
)
def test_user_base_valid_combinations(first_name,
                                      middle_name, last_name,
                                      email, username, gender,
                                      dateofbirth, timezone, mobile):
    """Test valid combinations of fields."""
    data = {
        "first_name": first_name,
        "middle_name": middle_name,
        "last_name": last_name,
        "email": email,
        "username": username,
        "gender": gender,
        "dateofbirth": dateofbirth,
        "timezone": timezone,
        "mobile": mobile,
    }
    user = UserBase(**data)
    assert user.first_name == first_name
    assert user.middle_name == middle_name
    assert user.last_name == last_name
    assert user.email == email
    assert user.username == username
    assert user.gender == gender
    assert user.dateofbirth == dateofbirth
    assert user.timezone == timezone
    assert user.mobile == mobile


def test_user_base_required_fields():
    """Test that all required fields are enforced."""
    # Missing multiple required fields
    with pytest.raises(ValidationError) as exc_info:
        UserBase(email="test@example.com", username="testuser")
    assert "field required" in str(exc_info.value).lower()


def test_user_base_empty_strings():
    """Test that empty strings are rejected for required string fields."""
    invalid_data = {
        "first_name": "",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "username": "johndoe",
        "gender": Gender.MALE,
        "dateofbirth": date(1990, 1, 1),
        "mobile": "1234567890",
    }
    with pytest.raises(ValidationError) as exc_info:
        UserBase(**invalid_data)
    assert "string should have at least 1 character" in str(exc_info.value).lower()
