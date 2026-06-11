from datetime import datetime
from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Server:
    """Represents a monitored server in the infrastructure."""
    id: str
    hostname: str
    ip_address: str
    status: str  # 'healthy' | 'warning' | 'critical'
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    last_heartbeat: datetime

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'hostname': self.hostname,
            'ip_address': self.ip_address,
            'status': self.status,
            'metrics': {
                'cpu_usage': round(self.cpu_usage, 2),
                'memory_usage': round(self.memory_usage, 2),
                'disk_usage': round(self.disk_usage, 2),
            },
            'last_heartbeat': self.last_heartbeat.isoformat(),
        }


@dataclass
class InfrastructureCluster:
    """Represents a cluster of servers (e.g. a Kubernetes cluster)."""
    name: str
    servers: List[Server] = field(default_factory=list)

    @property
    def healthy_servers(self) -> int:
        return sum(1 for s in self.servers if s.status == 'healthy')

    @property
    def total_servers(self) -> int:
        return len(self.servers)
