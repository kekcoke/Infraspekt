from datetime import datetime, timezone
from flask import Blueprint, jsonify

health_bp = Blueprint('health', __name__)


@health_bp.route('/health')
def health_check():
    """Health endpoint — critical for load balancers and monitoring."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'version': '1.0.0',
        'service': 'infrawatch-python-backend',
    })
