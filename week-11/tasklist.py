'''
Your task is to maintain a list of tasks supporting the addition of new tasks.
Each task has a name and a priority, which is an integer.

The task list supports the retrieval and removal of the task with the highest priority.
If multiple tasks have the same priority, the alphabetically first task should be chosen.

In a file tasklist.py, implement the class Tasks with the following methods:

add_task(name, priority): add a task to the list
fetch_task(): find and remove the highest priority task
Both methods should be efficient even when the list has a large number of tasks.
'''

import heapq

class Tasks:
    def __init__(self):
        self.tasklist = []

    def add_task(self, name, priority):
        heapq.heappush(self.tasklist, (100 - priority, name))

    def fetch_task(self):
        return heapq.heappop(self.tasklist)[1]

if __name__ == "__main__":
    tasks = Tasks()

    tasks.add_task("siivous", 20)
    tasks.add_task("koodaus", 90)
    tasks.add_task("treffit", 80)

    print(tasks.fetch_task()) # koodaus

    tasks.add_task("nukkuminen", 20)

    print(tasks.fetch_task()) # treffit
    print(tasks.fetch_task()) # nukkuminen