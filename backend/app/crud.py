from app.database import tasks_collection
from app.response import response
from bson import ObjectId

def create_task(title, desc=None):
    """
    Create a new task in the database.

    Args:
        title (str): Title of the task.
        desc (str, optional): Task description.

    Returns:
        dict: Standardized API response.
    """
    try:
        task = {
            "title": title,
            "desc": desc,
            "completed": False
        }

        result = tasks_collection.insert_one(task)

        created_task = {
            "id": str(result.inserted_id),
            "title": title,
            "desc": desc,
            "completed": False
        }

        return response(
            success=1,
            message="Task created successfully",
            data=created_task
        )

    except Exception as e:
        return response(
            success=0,
            message="Failed to create task",
            trace=str(e)
        )
    

def get_all_tasks():
    """
    Retrieve all tasks from the database.

    Returns:
        dict: Standardized API response containing list of all tasks.
    """
    try:
        tasks = []

        for task in tasks_collection.find():
            tasks.append({
                "id": str(task["_id"]),
                "title": task["title"],
                "desc": task.get("desc", ""),
                "completed": task["completed"]
            })

        return response(
            success=1,
            message="Tasks retrieved successfully",
            data={"tasks": tasks}
        )

    except Exception as e:
        return response(
            success=0,
            message="Failed to retrieve tasks",
            trace=str(e)
        )
    

def update_task(task_id: str, update_data: dict):
    """
    Update an existing task in the database.

    Args:
        task_id (str): Task ID to update.
        update_data (dict): Fields to update.

    Returns:
        dict: Standardized API response with updated task.
    """
    try:
        result = tasks_collection.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": update_data}
        )

        if result.matched_count == 0:
            return response(
                success=0,
                message="Task not found"
            )

        updated_task = tasks_collection.find_one({"_id": ObjectId(task_id)})

        return response(
            success=1,
            message="Task updated successfully",
            data={
                "id": str(updated_task["_id"]),
                "title": updated_task["title"],
                "desc": updated_task.get("desc", ""),
                "completed": updated_task["completed"]
            }
        )

    except Exception as e:
        return response(
            success=0,
            message="Failed to update task",
            trace=str(e)
        )


def delete_task(task_id: str):
    """
    Delete a task from the database.

    Args:
        task_id (str): Task ID to delete.

    Returns:
        dict: Standardized API response confirming deletion.
    """
    try:
        result = tasks_collection.delete_one({"_id": ObjectId(task_id)})

        if result.deleted_count == 0:
            return response(
                success=0,
                message="Task not found"
            )

        return response(
            success=1,
            message="Task deleted successfully",
            data={"id": task_id}
        )

    except Exception as e:
        return response(
            success=0,
            message="Failed to delete task",
            trace=str(e)
        )