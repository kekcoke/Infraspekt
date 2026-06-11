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

## 6. Implementation Plan
1. **Phase 2.1**: Initialize React app and install dependencies.
2. **Phase 2.2**: Define Types and API Service.
3. **Phase 2.3**: Implement UI Components (Card, List, Form).
4. **Phase 2.4**: Implement Testing Harness.
5. **Phase 4**: Containerization (Dockerfile, Nginx, Compose).
