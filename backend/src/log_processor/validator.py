from typing import Dict, Any, Set

class LogValidator:
    """Validates log entry structures and levels."""
    VALID_LEVELS: Set[str] = {
        "EMERGENCY", "ALERT", "CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"
    }
    
    def validate_log_entry(self, log_data: Dict[str, Any]) -> bool:
        """Complete validation of a log entry dictionary."""
        return (
            self._validate_required_fields(log_data) and 
            self._validate_field_types(log_data) and
            log_data.get("level", "").upper() in self.VALID_LEVELS
        )

    def _validate_required_fields(self, data: Dict[str, Any]) -> bool:
        required = {"timestamp", "level", "message"}
        return all(field in data for field in required)

    def _validate_field_types(self, data: Dict[str, Any]) -> bool:
        if not isinstance(data.get("message"), str):
            return False
        if not isinstance(data.get("level"), str):
            return False
        return True
