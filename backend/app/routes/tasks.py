from fastapi import APIRouter
from app.schemas import TaskCreate, TaskUpdate
from app.crud import create_task, get_all_tasks, update_task, delete_task

# Router for all task-related endpoints
router = APIRouter(prefix="/tasks", tags=["Tasks"])


# -------------------- CREATE TASK --------------------
@router.post("/")
def add_task(task: TaskCreate):
    """Create a new task."""
    return create_task(task.title, task.desc)


# -------------------- GET ALL TASKS --------------------
@router.get("/")
def fetch_tasks():
    """Retrieve all tasks from the database."""
    return get_all_tasks()


# -------------------- UPDATE TASK --------------------
@router.put("/{task_id}")
def modify_task(task_id: str, update: TaskUpdate):
    """Update an existing task by ID."""
    update_data = update.dict(exclude_unset=True)
    return update_task(task_id, update_data)


# -------------------- DELETE TASK --------------------
@router.delete("/{task_id}")
def remove_task(task_id: str):
    """Delete a task by its ID."""
    return delete_task(task_id)