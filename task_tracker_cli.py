import sys
import json

if len(sys.argv) < 2:
    sys.exit("Not enough arguments!")

if sys.argv[1] != "task-cli":
    sys.exit("Invalid Argument!")

#Have [update, delete] tasks

with open("task_storage.json") as file:
    try:
        task_storage = json.load(file)
    except json.decoder.JSONDecodeError:
        task_storage = []


with open("task_storage.json") as file:
    id = len(task_storage) + 1



task_types = ["add", "update", "delete"]




def add_task(arg):
    if arg:
        with open("task_storage.json", "w") as file:
            global task_storage
            try:
                task_storage.append({"task": arg, "id": id})
                json.dump(task_storage, file,indent=2)
            except IndexError:
                task_storage.append({"task": arg, "id": id})
                json.dump(task_storage, file)
            file.write("\n")
        print(f"Task added successfully ({id})")
        return

if sys.argv[2] == task_types[0]:
    add_task(sys.argv[3])
elif sys.argv[2] == task_types[1]:
    ...