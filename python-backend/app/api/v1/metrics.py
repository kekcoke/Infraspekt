from datetime import datetime, timezone
from flask import Blueprint, jsonify

metrics_bp = Blueprint('metrics', __name__)

# Mock performance data — replaced with real instrumentation when DB is introduced
_RESPONSE_TIME_DATA = [
    {'endpoint': '/api/v1/health',          'avg_ms': 12.4,  'p95_ms': 28.1,  'p99_ms': 45.0,  'sample_count': 1000},
    {'endpoint': '/api/v1/servers',         'avg_ms': 34.7,  'p95_ms': 72.3,  'p99_ms': 98.5,  'sample_count': 850},
    {'endpoint': '/api/v1/clusters',        'avg_ms': 28.1,  'p95_ms': 61.0,  'p99_ms': 82.3,  'sample_count': 620},
    {'endpoint': '/api/v1/metrics/response-times', 'avg_ms': 9.8, 'p95_ms': 21.0, 'p99_ms': 31.5, 'sample_count': 400},
    {'endpoint': '/api/v1/metrics/error-rates',    'avg_ms': 10.2, 'p95_ms': 22.4, 'p99_ms': 33.1, 'sample_count': 390},
]

_ERROR_RATE_DATA = [
    {'endpoint': '/api/v1/health',          'total_requests': 10000, 'errors': 3,  'error_rate_pct': 0.03},
    {'endpoint': '/api/v1/servers',         'total_requests': 5000,  'errors': 12, 'error_rate_pct': 0.24},
    {'endpoint': '/api/v1/clusters',        'total_requests': 3200,  'errors': 8,  'error_rate_pct': 0.25},
    {'endpoint': '/api/v1/metrics/response-times', 'total_requests': 2000, 'errors': 1, 'error_rate_pct': 0.05},
    {'endpoint': '/api/v1/metrics/error-rates',    'total_requests': 1900, 'errors': 0, 'error_rate_pct': 0.00},
]


@metrics_bp.route('/response-times')
def response_times():
    """Return mock P50/P95/P99 response-time metrics per endpoint."""
    return jsonify({
        'endpoint_metrics': _RESPONSE_TIME_DATA,
        'timestamp': datetime.now(timezone.utc).isoformat(),
    })


@metrics_bp.route('/error-rates')
def error_rates():
    """Return mock error-rate metrics per endpoint over a rolling 60-minute window."""
    return jsonify({
        'error_metrics': _ERROR_RATE_DATA,
        'window_minutes': 60,
        'timestamp': datetime.now(timezone.utc).isoformat(),
    })
