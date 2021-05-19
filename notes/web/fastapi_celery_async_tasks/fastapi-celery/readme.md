# FastAPI + Celery Simple Example Project

## Usage

```
docker-compose up -d --build
curl http://localhost:8004/tasks -H "Content-Type: application/json" --data '{"type": 3}'
curl http://localhost:8004/tasks/<task_id>
```
