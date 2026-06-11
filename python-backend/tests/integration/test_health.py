def test_health_returns_200(client):
    resp = client.get('/api/v1/health')
    assert resp.status_code == 200


def test_health_body(client):
    data = client.get('/api/v1/health').get_json()
    assert data['status'] == 'healthy'
    assert data['service'] == 'infrawatch-python-backend'
    assert 'timestamp' in data
    assert 'version' in data


def test_health_response_time_header(client):
    resp = client.get('/api/v1/health')
    assert 'X-Response-Time-Ms' in resp.headers
