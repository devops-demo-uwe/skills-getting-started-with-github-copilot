# Project Guidelines

## Project Overview

This repository contains the Mergington High School activity signup application. It exposes a small API for listing extracurricular activities and registering students, and serves a static browser interface from `src/static/`. Activity data is stored in memory, so changes do not persist when the application restarts.

## Tech Stack

- Python with FastAPI for the HTTP API
- Uvicorn as the ASGI development server
- HTML, CSS, and vanilla JavaScript for the frontend
- pytest and FastAPI `TestClient` for automated tests
- httpx for HTTP client support
- watchfiles for development reloads

## Python Guidelines

- Follow PEP 8 and preserve the established style in nearby code.
- Add type annotations to function parameters and return values when they improve clarity.
- Keep route handlers small; extract reusable domain logic when a handler becomes complex.
- Use FastAPI request validation and `HTTPException` with appropriate status codes for client-facing errors.
- Validate inputs before mutating the in-memory `activities` data.
- Avoid mutable default arguments and broad exception handlers.
- Prefer `pathlib.Path` over manual path-string manipulation.
- Write focused tests for new behavior and error cases in `tests/`.
- Tests that mutate `activities` must restore the original state, including when an assertion fails.
- Run `pytest` after changing Python code or API behavior.

---
name: Backend conventions
applyTo: "src/backend/**/*.java"
---