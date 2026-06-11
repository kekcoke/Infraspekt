from typing import Dict, Optional, Any
from datetime import datetime


class LogEntry:
    """Represents a single log entry with strict typing."""

    def __init__(
        self,
        timestamp: datetime,
        level: str,
        message: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.timestamp = timestamp
        self.level = level.upper()
        self.message = message
        self.metadata = metadata or {}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp.isoformat(),
            "level": self.level,
            "message": self.message,
            "metadata": self.metadata,
        }
