def read_tasks_from_file(file_path: str):
    try:
        with open(file_path, 'r') as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def write_tasks_to_file(file_path: str, tasks: list):
    with open(file_path, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def get_tasks(file_path: str):
    return read_tasks_from_file(file_path)

def add_task(file_path: str, task: str):
    tasks = get_tasks(file_path)
    tasks.append(task)
    write_tasks_to_file(file_path, tasks)

def delete_task(file_path: str, task_id: int):
    tasks = get_tasks(file_path)
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        write_tasks_to_file(file_path, tasks)