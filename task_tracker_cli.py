import sys
import json

#Have [update, delete] tasks

with open() as file:
    ...
    
task_types = ["add", "update", "delete"]

if len(sys.argv) < 2:
    sys.exit("Not enough arguments!")

if sys.argv[1] != "task-cli":
    sys.exit("Invalid Argument!")


def add_task(arg):
    if arg:
        print("Task added successfully")
        return

if sys.argv[2] == task_types[0]:
    add_task(sys.argv[3])