import json

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

if __name__ == "__main__":
    # Testando a criação de uma tarefa
    new_task = {
        "title": "Nova Tarefa",
        "description": "Descrição da nova tarefa",
        "due_date": "2025-02-10",
        "priority": "Alta"
    }
    created_task = create_task(new_task)
    print(f"Tarefa criada: {created_task}")

    # Listando todas as tarefas
    tasks = get_tasks()
    print(f"Tarefas: {tasks}")

    # Atualizando uma tarefa
    updated_task = {"title": "Tarefa Atualizada"}
    update_task(created_task['id'], updated_task)
    print(f"Tarefas após atualização: {get_tasks()}")

    # Deletando uma tarefa
    delete_task(created_task['id'])
    print(f"Tarefas após deleção: {get_tasks()}")