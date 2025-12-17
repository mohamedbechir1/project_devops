# DevOps Demo App

- Frontend: Vue 3 + Vite
- Backend: FastAPI (Python)
- AI service: FastAPI + scikit-learn (sentiment)
- Database: PostgreSQL 15

## Local development

Requirements: Docker & Docker Compose.

```bash
# From deploy/
docker compose up --build
```

Services:
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- AI: http://localhost:8001
- DB: localhost:5432 (appuser/apppassword, db appdb)

## API
- GET /health
- GET /api/hello
- GET /api/db-time
- POST /api/sentiment { "text": "your phrase" }

Examples:
```bash
curl http://localhost:8000/health
curl http://localhost:8000/api/db-time
curl -X POST http://localhost:8000/api/sentiment \
  -H 'Content-Type: application/json' \
  -d '{"text":"I love this"}'
```

## Next steps
- Vagrant + Ansible (2 VMs: vm-jenkins, vm-app+monitor)
- Jenkins pipeline + Docker Hub push
- Nagios monitoring
