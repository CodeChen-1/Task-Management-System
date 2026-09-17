from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from app.database import get_db
from app.models.task import Task
from app.models.user import User
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.utils.security import get_current_user

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse)
def create_task(
    task: TaskCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    new_task = Task(
        user_id = current_user.id,
        title = task.title,
        description = task.description,
        priority = task.priority,
        deadline = task.deadline
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/tasks", response_model=List[TaskResponse])
def get_tasks(
    search: Optional[str] = Query(None, description="Search in title and description"),
    status: Optional[str] = Query(None, description="Filter by status: pending, in_progress, completed"),
    priority: Optional[str] = Query(None, description="Filter by priority: low, medium, high"),
    sort_by: Optional[str] = Query(None, description="Sort by: deadline, priority, created_at"),
    deadline_status: Optional[str] = Query(None, description="Filter: overdue, upcoming, due_soon"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Task).filter(Task.user_id == current_user.id)
    
    if search:
        query = query.filter(
            (Task.title.contains(search)) | (Task.description.contains(search))
        )

    if status:
        query = query.filter(Task.status == status)

    if priority:
        query = query.filter(Task.priority == priority)

    if deadline_status:
        now = datetime.utcnow()
        if deadline_status == "overdue":
            query = query.filter(Task.deadline < now, Task.status != "completed")
        elif deadline_status == "upcoming":
            query = query.filter(Task.deadline > now)
        elif deadline_status == "due_soon":
            from datetime import timedelta
            soon = now + timedelta(hours=24)
            query = query.filter(Task.deadline > now, Task.deadline < soon)
 
    if sort_by == "deadline":
        query = query.order_by(Task.deadline.asc())
    elif sort_by == "priority":
        query = query.order_by(Task.priority.asc())
    elif sort_by == "created_at":
        query = query.order_by(Task.created_at.desc())
    else:
        query = query.order_by(Task.created_at.desc())
    
    return query.all()

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    update_data = task_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task

@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}

