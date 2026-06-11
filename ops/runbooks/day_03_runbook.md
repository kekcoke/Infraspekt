# Runbook: Day 03 - React E-Commerce Frontend

## System Overview
The `ecommerce-frontend` is a React/TypeScript application served via Nginx. It communicates with a backend service (default: port 5000) for product and category management.

## Deployment
### Local Development
1. Navigate to `ecommerce-frontend/`.
2. Run `npm install`.
3. Run `npm start` to launch the dev server on `http://localhost:3000`.

### Docker
1. Build: `docker build -t ecommerce-frontend ./ecommerce-frontend`
2. Run: `docker run -p 3000:80 ecommerce-frontend`
3. Compose: `docker-compose up --build` (from `ecommerce-frontend/`)

## Testing
- Unit tests: `npm test`
- Coverage: `npm run test:coverage`

## Environment Variables
- `REACT_APP_API_URL`: Base URL for the backend API.
