# Sales Dashboard

A small full-stack application built as a hands-on practice project for
refreshing backend development skills while using technologies similar
to those used in my work environment.

## Architecture

``` text
React + TypeScript
        ↓
TanStack React Query
        ↓
Axios
        ↓
FastAPI
        ↓
SQLAlchemy
        ↓
asyncpg
        ↓
PostgreSQL
```

Supporting technologies will include:

-   **Frontend:** React, TypeScript, Vite, TanStack React Query,
    TanStack React Table, AG Grid, Zustand, Recharts, Axios
-   **Backend:** Python, Poetry, FastAPI, Pydantic, SQLAlchemy, asyncpg,
    Alembic
-   **Database:** PostgreSQL
-   **Testing / quality:** Pytest, pytest-asyncio, Ruff, MyPy
-   **Infrastructure:** Docker / Docker Compose

## Project Goal

Build a small sales dashboard that retrieves sales data from a
PostgreSQL database through a Python/FastAPI backend and displays it in
a React frontend.

The goal is not simply to build the application, but to practice the
complete request/data flow:

``` text
PostgreSQL
    ↓
SQLAlchemy
    ↓
FastAPI
    ↓
Axios
    ↓
TanStack React Query
    ↓
React
    ↓
AG Grid / Recharts
```

## Current Project Structure

``` text
sales-dashboard/
├── .gitignore
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.ts
│   └── ...
│
└── backend/
    └── pyproject.toml
```

## What Has Been Completed

### Frontend

Created the React application with Vite:

``` bash
npm create vite@latest sales-dashboard -- --template react-ts
```

The frontend was reorganized into a `frontend` directory so that the
repository can contain separate frontend and backend applications.

Installed the initial frontend dependencies:

``` text
axios
@tanstack/react-query
@tanstack/react-table
ag-grid-react
ag-grid-community
zustand
recharts
```

The frontend production build currently succeeds:

``` bash
npm run build
```

### Backend Development Environment

Created a separate `backend` directory.

Installed Python **3.14.8** for this personal project.

Installed Poetry **2.5.1** for Python dependency and project management.

Initialized the backend with:

``` bash
poetry init
```

The project intentionally uses the latest Python version available for
this personal practice project rather than copying the Python 3.11
version used by the company's backend.

## Planned Backend

The backend will use:

-   Python 3.14
-   Poetry
-   FastAPI
-   Pydantic
-   SQLAlchemy 2.x
-   asyncpg
-   Alembic
-   PostgreSQL

The backend will eventually be organized approximately as:

``` text
backend/
├── app/
│   ├── routes/
│   ├── services/
│   ├── repositories/
│   ├── models/
│   ├── schemas/
│   ├── database.py
│   └── main.py
│
├── migrations/
├── tests/
├── alembic.ini
└── pyproject.toml
```

This structure is intentionally similar to the Python/FastAPI backend
architecture used at work.

## Planned Database

The initial database will contain a small sales model:

### Customers

``` text
id
name
region
industry
```

### Products

``` text
id
name
category
```

### Sales

``` text
id
customer_id
product_id
sale_date
quantity
revenue
```

## Planned API

The first API endpoint will be something similar to:

``` text
GET /api/sales
```

The endpoint will retrieve sales data from PostgreSQL and return
validated response data through FastAPI/Pydantic.

Later endpoints may support:

-   Filtering
-   Pagination
-   Date ranges
-   Sales summaries
-   Aggregations
-   Individual sales records

## Planned Frontend

The React application will:

1.  Request sales data from the FastAPI backend.
2.  Use Axios for HTTP communication.
3.  Use TanStack React Query to manage server state.
4.  Display sales in AG Grid.
5.  Add charts using Recharts.
6.  Potentially use Zustand for client-side application state.

## Learning Objectives

This project is primarily a backend refresher for a frontend engineer.

Key concepts to practice:

-   REST APIs
-   FastAPI routing
-   Pydantic request/response models
-   SQLAlchemy models and queries
-   Async Python
-   PostgreSQL
-   Database migrations with Alembic
-   Repository/service separation
-   HTTP requests from React
-   TanStack Query
-   Loading and error states
-   API testing
-   Docker and Docker Compose
-   Full-stack debugging

## Development Roadmap

### Phase 1 --- Project Setup

-   [x] Create React/Vite application
-   [x] Organize frontend and backend directories
-   [x] Install frontend dependencies
-   [x] Verify frontend production build
-   [x] Install Python
-   [x] Install Poetry
-   [x] Initialize backend Poetry project

### Phase 2 --- Backend

-   [ ] Configure FastAPI
-   [ ] Add SQLAlchemy
-   [ ] Add asyncpg
-   [ ] Add PostgreSQL
-   [ ] Configure database connection
-   [ ] Create SQLAlchemy models
-   [ ] Configure Alembic
-   [ ] Create initial migration
-   [ ] Seed sample data
-   [ ] Create sales API endpoint
-   [ ] Add Pydantic response schemas

### Phase 3 --- Frontend/API Integration

-   [ ] Configure Axios
-   [ ] Configure TanStack Query
-   [ ] Create sales query hook
-   [ ] Connect React to FastAPI
-   [ ] Display sales data
-   [ ] Add loading/error states

### Phase 4 --- Dashboard

-   [ ] Add AG Grid
-   [ ] Add sorting
-   [ ] Add filtering
-   [ ] Add pagination
-   [ ] Add sales charts
-   [ ] Add date-range filtering
-   [ ] Add summary metrics

### Phase 5 --- Engineering Practice

-   [ ] Add backend tests
-   [ ] Add API integration tests
-   [ ] Add frontend tests
-   [ ] Add Docker Compose
-   [ ] Add environment configuration
-   [ ] Improve error handling
-   [ ] Add linting/type checking
-   [ ] Document the API

## Status

**Current stage:** Project setup complete; backend implementation next.

The application is intentionally being developed incrementally rather
than generated as a complete application. The objective is to understand
and practice each layer of the stack.
