from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def create_task(task):
    tasks = get_tasks()
    task_id = len(tasks) + 1
    task['id'] = task_id
    tasks.append(task)
    save_tasks(tasks)
    return task

def get_tasks():
    try:
        with open('memory', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        return []
    return tasks

def delete_task(task_id):
    tasks = get_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)

def update_task(task_id, updated_task):
    tasks = get_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task.update(updated_task)
            break
    save_tasks(tasks)

def save_tasks(tasks):
    with open('memory', 'w') as file:
        json.dump(tasks, file)

@app.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = get_tasks()
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json
    created_task = create_task(task)
    return jsonify(created_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def modify_task(task_id):
    updated_task = request.json
    update_task(task_id, updated_task)
    return jsonify({'message': 'Task updated'})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    delete_task(task_id)
    return jsonify({'message': 'Task deleted'})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    tasks = get_tasks()
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is not None:
        return jsonify(task)
    else:
        return jsonify({'message': 'Task not found'}), 404

if __name__ == "__main__":
    app.run(debug=True)