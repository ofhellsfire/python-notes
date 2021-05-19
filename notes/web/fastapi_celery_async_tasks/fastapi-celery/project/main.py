from celery.result import AsyncResult
from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse

from worker import create_task


app = FastAPI()


@app.post("/tasks", status_code=201)
def run_task(payload=Body(...)):
    task_type = payload["type"]
    try:
        task = create_task.delay(int(task_type))
        return JSONResponse({"task_id": task.id})
    except (ValueError, TypeError):
        return JSONResponse({"error_message": "invalid task type"})


@app.get("/tasks/{task_id}")
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
    return JSONResponse(result)

