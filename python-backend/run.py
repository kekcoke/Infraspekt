import logging
from app import create_app
from app.core.config import DevelopmentConfig

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s',
)

app = create_app(DevelopmentConfig)

if __name__ == '__main__':
    # Development server only — use gunicorn in production
    app.run(host='0.0.0.0', port=5001, debug=True)
