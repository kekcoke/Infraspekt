import random
from datetime import datetime, timedelta, timezone
from flask import Blueprint, jsonify
from app.models.infrastructure import Server, InfrastructureCluster

infrastructure_bp = Blueprint('infrastructure', __name__)

_STATUSES = ['healthy', 'warning', 'critical']


@infrastructure_bp.route('/servers')
def get_servers():
    """Return all monitored servers with live-simulated metrics."""
    servers = [
        Server(
            id=f'server-{i}',
            hostname=f'web-{i}.example.com',
            ip_address=f'10.0.1.{i + 10}',
            status=random.choice(_STATUSES),
            cpu_usage=random.uniform(10, 90),
            memory_usage=random.uniform(20, 80),
            disk_usage=random.uniform(30, 70),
            last_heartbeat=datetime.now(timezone.utc) - timedelta(seconds=random.randint(0, 300)),
        )
        for i in range(5)
    ]
    return jsonify({
        'servers': [s.to_dict() for s in servers],
        'total_count': len(servers),
        'timestamp': datetime.now(timezone.utc).isoformat(),
    })


@infrastructure_bp.route('/clusters')
def get_clusters():
    """Return infrastructure cluster overview."""
    servers = [
        Server(
            id=f'node-{i}',
            hostname=f'k8s-node-{i}',
            ip_address=f'10.0.2.{i + 10}',
            status='healthy',
            cpu_usage=45.2,
            memory_usage=60.1,
            disk_usage=35.8,
            last_heartbeat=datetime.now(timezone.utc),
        )
        for i in range(3)
    ]
    cluster = InfrastructureCluster('production-cluster', servers)
    return jsonify({
        'cluster_name': cluster.name,
        'total_servers': cluster.total_servers,
        'healthy_servers': cluster.healthy_servers,
        'servers': [s.to_dict() for s in cluster.servers],
    })
