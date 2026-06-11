# Architecture Spec - Day 03: React E-Commerce Frontend

## 1. Overview
The objective for Day 03 is to build a production-ready React frontend using TypeScript and Material UI. This dashboard will demonstrate distributed system patterns: component isolation, centralized state management (via React hooks/state), and API integration.

## 2. Layer Changes
- **Frontend Layer**: Introduction of a React application in `ecommerce-frontend/`.
- **API Layer**: Centralized `productService` using Axios for communication with the backend.
- **Contract Layer**: TypeScript interfaces for `Product` and `ProductFormData`.

## 3. Data Contracts
### Product Interface
```typescript
export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
  category: string;
  inStock: boolean;
  createdAt: string;
}
```

### API Endpoints (Consumed)
- `GET /api/products`: Fetch all products.
- `POST /api/products`: Create a product.
- `PUT /api/products/:id`: Update a product.
- `DELETE /api/products/:id`: Remove a product.

## 4. Component Architecture
- **Common**: `Header`, `Navigation` (Layout shell).
- **Products**:
    - `ProductList`: Orchestrator for data fetching and display.
    - `ProductCard`: Atomic display of product data.
    - `ProductForm`: Modal-based create/edit interface.
- **Layout**: `Dashboard` wrapper.

## 5. Success Criteria
- [ ] React application initializes with TypeScript and MUI.
- [ ] CRUD operations functional (with mock fallback if backend unavailable).
- [ ] Unit tests for `ProductCard` pass with >80% coverage.
- [ ] Dockerfile and Nginx configuration ready for deployment.
- [ ] Homework: Category management system implemented.

## 6. Implementation Plan (Commit Units)

### Commit 1 — Project Bootstrap
- `ecommerce-frontend/` initialized via `create-react-app --template typescript`
- Dependencies installed: MUI, Axios, React Router, testing libraries
- **Gate:** `tsc --noEmit` exits 0
- **Message:** `chore(day-03): bootstrap React TS project and install dependencies`

### Commit 2 — Types & API Service
- `src/types/Product.ts`
- `src/services/api.ts`
- **Gate:** `tsc --noEmit` exits 0
- **Message:** `feat(day-03): define Product types and Axios API service`

### Commit 3 — UI Components
- `src/components/products/ProductCard.tsx`
- `src/components/products/ProductForm.tsx`
- `src/components/products/ProductList.tsx`
- `src/App.tsx` updated
- **Gate:** `CI=true npm run build` exits 0
- **Message:** `feat(day-03): implement Product CRUD dashboard components`

### Commit 4 — Tests (QA Gate)
- `src/components/products/tests/ProductCard.test.tsx`
- `src/App.test.tsx` updated
- **Gate:** `CI=true npm run test:coverage` exits 0, all suites pass
- **Message:** `test(day-03): add unit tests for ProductCard and App (4 tests, passing)`

### Commit 5 — Assignment: Dynamic Category Management
- `src/components/products/CategoryManager.tsx`
- `src/components/products/ProductForm.tsx` updated (dynamic categories prop)
- `src/components/products/ProductList.tsx` updated (category state + handlers)
- **Gate:** `CI=true npm run test:coverage` exits 0
- **Message:** `feat(day-03): add dynamic CategoryManager (assignment)`

### Commit 6 — Ops & Docs
- `ecommerce-frontend/Dockerfile`
- `ecommerce-frontend/nginx.conf`
- `ecommerce-frontend/docker-compose.yml`
- `ops/runbooks/day_03_runbook.md`
- `docs/architecture/day_03_spec.md`
- `docs/Day_03_Review_Report.md`
- **Gate:** `docker build` exits 0 (or noted as skipped if Docker unavailable)
- **Message:** `chore(day-03): add Dockerfile, Nginx config, and ops runbook`
