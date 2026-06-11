import time
import logging
from flask import Flask, g, request
from app.core.config import Config

logger = logging.getLogger(__name__)


def create_app(config_class=Config):
    """Application factory pattern — enables testing and multiple configurations."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    _register_blueprints(app)
    _register_middleware(app)

    return app


def _register_blueprints(app: Flask) -> None:
    from app.api.v1.health import health_bp
    from app.api.v1.infrastructure import infrastructure_bp
    from app.api.v1.metrics import metrics_bp

    app.register_blueprint(health_bp, url_prefix='/api/v1')
    app.register_blueprint(infrastructure_bp, url_prefix='/api/v1')
    app.register_blueprint(metrics_bp, url_prefix='/api/v1/metrics')


def _register_middleware(app: Flask) -> None:
    @app.before_request
    def _start_timer():
        g.start_time = time.perf_counter()

    @app.after_request
    def _log_request_duration(response):
        duration_ms = (time.perf_counter() - g.start_time) * 1000
        logger.info(
            "method=%s path=%s status=%d duration_ms=%.2f",
            request.method,
            request.path,
            response.status_code,
            duration_ms,
        )
        response.headers["X-Response-Time-Ms"] = f"{duration_ms:.2f}"
        return response
