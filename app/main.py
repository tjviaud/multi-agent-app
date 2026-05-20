from fastapi import FastAPI
from pydantic import BaseModel
from app.orchestrator import run_multi_agent_system

app = FastAPI()

class TaskRequest(BaseModel):
    task: str

@app.post("/run")
def run_agents(request: TaskRequest):
    return run_multi_agent_system(request.task)