import sys
import json
import time
import os




if not os.path.exists("task_storage.json"):
    with open("task_storage.json", "w") as file:
        file.write("[]")

if len(sys.argv) <= 2:
    sys.exit("Not enough arguments!")

if sys.argv[1] != "task-cli":
    sys.exit("Invalid Argument!")


with open("task_storage.json") as file:
    try:
        task_storage = json.load(file)
    except json.decoder.JSONDecodeError:
        task_storage = []


with open("task_storage.json") as file:
    id = 1
    for pos, dicts in enumerate(task_storage):
        if id == dicts["id"]:
            id += 1
        else:
            break


def add_task(arg):
    if arg:
        with open("task_storage.json", "w") as file:
            global task_storage
            year = time.localtime().tm_year
            month = time.localtime().tm_mon
            day = time.localtime().tm_mday
            hour = time.localtime().tm_hour
            minute = time.localtime().tm_min
            second = time.localtime().tm_sec
            try:
                task_storage.append({"description": arg, "id": id, "status": "todo", "createdAt" : f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}", "updatedAt" : f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"})
                json.dump(task_storage, file,indent=2)
            except IndexError:
                task_storage.append({"description": arg, "id": id, "status": "todo"})
                json.dump(task_storage, file, indent=2)
            file.write("\n")
        print(f"Task added successfully ({id})")
        return

def update_task(cur_id, change):
    global task_storage
    if not task_storage:
        sys.exit("Please Add a Task!")
    for i in enumerate(task_storage):
        if i[1]["id"] == cur_id:
            year = time.localtime().tm_year
            month = time.localtime().tm_mon
            day = time.localtime().tm_mday
            hour = time.localtime().tm_hour
            minute = time.localtime().tm_min
            second = time.localtime().tm_sec
            if task_storage[i[0]]["description"] != change:
                task_storage[i[0]]["description"] = change
                task_storage[i[0]]["updatedAt"] = f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"
            with open("task_storage.json", "w") as file:
                json.dump(task_storage,file, indent=2)
            return
    sys.exit("Please enter a valid id")
        
            
def mark_task_done(cur_id):
    if not task_storage:
        sys.exit("No task available!")
    for pos, dicts in enumerate(task_storage):
        if dicts["id"] == cur_id:
            task_storage[pos]["status"] = "done"
            with open("task_storage.json", "w") as file:
                json.dump(task_storage, file, indent= 2)
            return
    sys.exit("Please enter a valid ID!")

def task_in_progress(cur_id):
    if not task_storage:
        sys.exit("No task available!")
    for pos, dicts in enumerate(task_storage):
        if dicts["id"] == cur_id:
            task_storage[pos]["status"] = "in-progress"
            with open("task_storage.json", "w") as file:
                json.dump(task_storage, file, indent= 2)
            return
    sys.exit("Please enter a valid ID!")

def delete_task(id_del):
    global task_storage
    if not task_storage:
        sys.exit("Please Add a Task!")
    for i in task_storage:
        if i["id"] == id_del:   
            task_storage.remove(i)
            with open("task_storage.json", "w") as file:
                json.dump(task_storage, file, indent=2)
            return
    sys.exit("Please enter a valid id")

def task_done():
    global task_storage
    any_done = False
    for loc, info in enumerate(task_storage):
        if info["status"] == "done":
            print(f"({info['id']}) '{info['description']}' | Status: {info['status']} | Created: {info['createdAt']} | Last Updated: {info['updatedAt']}")
            any_done = True
    if not any_done:
        sys.exit("No task to list")

def task_todo():
    global task_storage
    any_done = False
    for loc, info in enumerate(task_storage):
        if info["status"] == "todo":
            print(f"({info['id']}) '{info['description']}' | Status: {info['status']} | Created: {info['createdAt']} | Last Updated: {info['updatedAt']}")
            any_done = True
    if not any_done:
        sys.exit("No task to list")
def inprogress():
    global task_storage
    any_done = False
    for loc, info in enumerate(task_storage):
        if info["status"] == "in-progress":
            print(f"({info['id']}) '{info['description']}' | Status: {info['status']} | Created: {info['createdAt']} | Last Updated: {info['updatedAt']}")
            any_done = True
    if not any_done:
        sys.exit("No task to list")

def catcher():
    sys.exit("Invalid Argument")

def get_list():
    global task_storage

    list_opts = {
        "done" : task_done,
        "todo" : task_todo,
        "in-progress" : inprogress
    }

    #lists all tasks
    if len(sys.argv) == 3 and task_storage:
        print("All Tasks:")
        for loc, info in enumerate(task_storage):
            print(f"({info['id']}) '{info['description']}' | Status: {info['status']} | Created: {info['createdAt']} | Last Updated: {info['updatedAt']}")
    elif len(sys.argv) == 4:
        functions = list_opts.get(sys.argv[3], catcher)
        functions()
    else:
        sys.exit("No task to list")
    


#Add Task
if sys.argv[2] == "add":
    if len(sys.argv) != 4 or sys.argv[3].strip() == "":
        sys.exit("Invalid Argument or Input")
    add_task(sys.argv[3])
#Update Task
elif sys.argv[2] == "update" and sys.argv[3].isdigit() and len(sys.argv) == 5 and type(sys.argv[4]) == str:
    if sys.argv[4].strip() == "":
        sys.exit("Invalid Argument or Input")
    update_task(int(sys.argv[3]), sys.argv[4])
#Remove Task
elif sys.argv[2] == "delete" and len(sys.argv) == 4 and sys.argv[3].isdigit():
    delete_task(int(sys.argv[3]))
#Mark Task Done
elif sys.argv[2] == "mark-done" and len(sys.argv) == 4 and sys.argv[3].isdigit():
    mark_task_done(int(sys.argv[3]))
#Mark Task In Progress
elif sys.argv[2] == "mark-in-progress" and len(sys.argv) == 4 and sys.argv[3].isdigit():
    task_in_progress(int(sys.argv[3]))
#Fetch lists of users preference
elif sys.argv[2] == "list":
    get_list()
else:
    sys.exit("ERROR | INVALID ARGUMENTS")