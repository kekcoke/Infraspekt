def test_servers_returns_200(client):
    assert client.get('/api/v1/servers').status_code == 200


def test_servers_body_structure(client):
    data = client.get('/api/v1/servers').get_json()
    assert 'servers' in data
    assert 'total_count' in data
    assert data['total_count'] == 5
    first = data['servers'][0]
    assert {'id', 'hostname', 'ip_address', 'status', 'metrics', 'last_heartbeat'} <= set(first.keys())
    assert {'cpu_usage', 'memory_usage', 'disk_usage'} == set(first['metrics'].keys())


def test_clusters_returns_200(client):
    assert client.get('/api/v1/clusters').status_code == 200


def test_clusters_body_structure(client):
    data = client.get('/api/v1/clusters').get_json()
    assert data['cluster_name'] == 'production-cluster'
    assert data['total_servers'] == 3
    assert data['healthy_servers'] == 3
    assert len(data['servers']) == 3
