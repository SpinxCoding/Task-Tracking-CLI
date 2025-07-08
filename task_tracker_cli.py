import sys
import json

#Have [add, update, delete] tasks

task_types = ["add", "update", "delete"]

def add_task(arg):
    if arg:
        print("Task added successfully")
        return

if sys.argv[2] == task_types[0]:
    add_task(sys.argv[3])