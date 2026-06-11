from datetime import datetime, timezone
from app.models.infrastructure import Server, InfrastructureCluster


def _make_server(id='s1', status='healthy'):
    return Server(
        id=id, hostname=f'{id}.host', ip_address='10.0.0.1',
        status=status, cpu_usage=50.0, memory_usage=60.0, disk_usage=40.0,
        last_heartbeat=datetime.now(timezone.utc),
    )


def test_server_to_dict_keys():
    d = _make_server().to_dict()
    assert {'id', 'hostname', 'ip_address', 'status', 'metrics', 'last_heartbeat'} == set(d.keys())


def test_server_metrics_rounded():
    s = Server('x', 'h', '1.1.1.1', 'healthy', 12.3456, 78.9012, 34.5678,
                datetime.now(timezone.utc))
    m = s.to_dict()['metrics']
    assert m['cpu_usage'] == round(12.3456, 2)


def test_cluster_healthy_count():
    servers = [_make_server(f's{i}', 'healthy' if i < 3 else 'critical') for i in range(5)]
    cluster = InfrastructureCluster('test', servers)
    assert cluster.healthy_servers == 3
    assert cluster.total_servers == 5


def test_cluster_empty():
    cluster = InfrastructureCluster('empty', [])
    assert cluster.healthy_servers == 0
    assert cluster.total_servers == 0
