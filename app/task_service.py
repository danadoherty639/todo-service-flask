from flask import abort

from app import task_model

def get_tasks():
    return task_model.get_tasks()

def get_task(task_id):
    task = task_model.get_task(task_id)
    
    if task is None:
        abort(404)

    return task

def add_task(task):
    if not task or not 'name' in task:
        abort(400)
    
    new_task = task_model.add_task(task['name'], task['description'], False)

    return new_task

def update_task(task_id, task):
    existing_task = task_model.get_task(task_id)

    if existing_task is None:
        abort(404)
    
    if not task:
        abort(400)

    if 'name' in task and type(task['name']) != str:
        abort(400)

    if 'description' in task and type(task['description']) is not str:
        abort(400)

    if 'done' in task and type(task['done']) is not bool:
        abort(400)
    
    task_model.update_task(task_id, task['name'], task['description'], task['done'])

    existing_task['name'] = task['name']
    existing_task['description'] = task['description']
    existing_task['done'] = task['done']

    return existing_task

def delete_task(task_id):
    task = task_model.get_task(task_id)

    if task is None:
        abort(404)

    task_model.delete_task(task_id)

    return task
