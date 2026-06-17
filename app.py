task = []

def add_task(task):
    task.append(task)

def display_task():
    for task in tasks:
        print("-", task)

add_task("Learn GitHub")
add_task("Practice branching")


display_tasks()