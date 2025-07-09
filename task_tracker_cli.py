import sys
import json


with open("task_storage.json", "a") as file:
    pass

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
    for i in range(len(task_storage) + 1):
        for i in task_storage:
            if id == i["id"]: 
                id += 1
                break
    


task_type = ["add", "update", "delete"]




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

def update_task(cur_id, change):
    global task_storage
    if not task_storage:
        sys.exit("Please Add a Task!")
    for i in task_storage:
        if i["id"] == cur_id:            
            task_storage[i["id"] - 1]["task"] = change
            with open("task_storage.json", "w") as file:
                json.dump(task_storage, file, indent=2)
            return
    sys.exit("Please enter a valid id")
        
            
    

def delete_task(id_del):
    global task_storage
    if not task_storage:
        sys.exit("Please Add a Task!")
    for i in task_storage:
        if i["id"] == id_del:     
            x = i
            task_storage.remove(x)
            with open("task_storage.json", "w") as file:
                json.dump(task_storage, file, indent=2)
            return
    sys.exit("Please enter a valid id")
        
   
    


if sys.argv[2] == task_type[0]:
    add_task(sys.argv[3])
elif sys.argv[2] == task_type[1] and sys.argv[3].isdigit() and type(sys.argv[4]) == str:
    update_task(int(sys.argv[3]), sys.argv[4])
elif sys.argv[2] == task_type[2] and len(sys.argv) == 4 and sys.argv[3].isdigit():
    delete_task(int(sys.argv[3]))