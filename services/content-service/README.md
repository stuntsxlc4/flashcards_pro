# Flashcards Content Service

Service identifier: `content-service`
Owning team: `backend-team`
Generated from: `templates/fastapi-microservice`

## Responsibilities

Owns deck, card, category, and difficulty metadata used by the Flashcards application.

The service must not access another service's database or import another service's internal modules.

## Local setup

```shell
cp .env.example .env
make install
make local-run
```

The application listens on <http://127.0.0.1:8000> by default.

## Endpoints

- API status: <http://127.0.0.1:8000/api/v1/status>
- Swagger UI: <http://127.0.0.1:8000/docs>
- OpenAPI: <http://127.0.0.1:8000/openapi.json>
- Liveness: <http://127.0.0.1:8000/health/live>
- Readiness: <http://127.0.0.1:8000/health/ready>

## Quality gate

```shell
make lint
make format-check
make typecheck
make test
make docs
make image-build
```

## Runtime image

The container runs as a non-root user, listens on port `8000`, writes structured
logs to standard output, and exposes a liveness health check.

## Configuration

Configuration uses validated `APP_` environment variables. Copy `.env.example`
for local development. Never commit `.env` files or production secrets.

## Ownership

Repository automation and service catalogs should read ownership metadata from
`OWNERS.yaml`. Template provenance is recorded in `TEMPLATE_METADATA.yaml`.
