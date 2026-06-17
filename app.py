task = []

def add_task(task):
    if task.strip() =="":
        print("task cannot be empty.")
    task.append(task)
    print(f"Added: {task}")

    print("Current Tasks:")

for t in tasks:
    print(f"-{t}")

def display_task():
    for task in tasks:
        print("-", task)

add_task("Learn GitHub")
add_task("Practice branching")


display_tasks()
