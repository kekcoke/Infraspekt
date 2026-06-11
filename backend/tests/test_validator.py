from src.log_processor.validator import LogValidator


def test_validator_valid_entry():
    validator = LogValidator()
    valid_data = {
        "timestamp": "2024-03-21T10:00:00",
        "level": "ERROR",
        "message": "system crash",
    }
    assert validator.validate_log_entry(valid_data) is True


def test_validator_invalid_level():
    validator = LogValidator()
    invalid_data = {
        "timestamp": "2024-03-21T10:00:00",
        "level": "INVALID",
        "message": "bad level",
    }
    assert validator.validate_log_entry(invalid_data) is False


def test_validator_missing_fields():
    validator = LogValidator()
    incomplete_data = {"message": "missing fields"}
    assert validator.validate_log_entry(incomplete_data) is False
