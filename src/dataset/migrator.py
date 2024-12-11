import json

with open('helps.json', 'r') as file:
    data = json.load(file)

tasks = []

for i, task in enumerate(data):
    tasks.append({
        "task_id": f"helps/{i}",
        "input": task["task"]
    })

with open('helps.json', 'w') as file:
    json.dump(tasks, file, indent=2)