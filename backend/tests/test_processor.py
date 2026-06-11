from datetime import datetime
from src.log_processor.processor import LogEntry


def test_log_entry_initialization():
    now = datetime.now()
    entry = LogEntry(now, "info", "test message", {"user_id": 1})
    assert entry.level == "INFO"
    assert entry.message == "test message"
    assert entry.metadata["user_id"] == 1


def test_log_entry_to_dict():
    now = datetime.now()
    entry = LogEntry(now, "error", "critical failure")
    data = entry.to_dict()
    assert data["level"] == "ERROR"
    assert data["message"] == "critical failure"
    assert "timestamp" in data
