def test_response_times_200(client):
    assert client.get('/api/v1/metrics/response-times').status_code == 200


def test_response_times_body(client):
    data = client.get('/api/v1/metrics/response-times').get_json()
    assert 'endpoint_metrics' in data
    assert 'timestamp' in data
    assert len(data['endpoint_metrics']) > 0
    entry = data['endpoint_metrics'][0]
    assert {'endpoint', 'avg_ms', 'p95_ms', 'p99_ms', 'sample_count'} == set(entry.keys())


def test_error_rates_200(client):
    assert client.get('/api/v1/metrics/error-rates').status_code == 200


def test_error_rates_body(client):
    data = client.get('/api/v1/metrics/error-rates').get_json()
    assert 'error_metrics' in data
    assert data['window_minutes'] == 60
    entry = data['error_metrics'][0]
    assert {'endpoint', 'total_requests', 'errors', 'error_rate_pct'} == set(entry.keys())
