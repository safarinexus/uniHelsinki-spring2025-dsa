'''
Your task is to implement a class that maintains a list of numbers and has a method that reports how many distinct occurrence counts the numbers on the list have. 
The occurrence count of a number tells how many times that number occurs on the list.
For example, the list [1,2,3,1,2,3] has just one occurrence count because each number occurs twice on the list. 
The list [1,2,2,3,3,3] has three occurrence counts, because the number 1 occurs once, the number 2 occurs twice and the number 3 occurs three times.
In a file occurrences.py, implement the class OccurrenceTracker with the following methods:

append(number): add number to the end of the list
count(): return the number of distinct occurrence counts

Both methods should work in O(1) time.

You can test the efficiency of your solution with the following code. In this case too the code should finish almost immediately.
'''

class OccurrenceTracker:
    def __init__(self):
        self.occurrences = {}

    def append(self, number):
        self.occurrences[number] = self.occurrences.get(number, 0) + 1

    def count(self):
        return len(set(self.occurrences.values()))

if __name__ == "__main__":
    tracker = OccurrenceTracker()

    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    print(tracker.count()) # 2

    tracker.append(2)
    tracker.append(3)
    print(tracker.count()) # 1

    tracker.append(2)
    tracker.append(3)
    tracker.append(3)
    print(tracker.count()) # 3

    tracker = OccurrenceTracker()
    total = 0
    for i in range(10**5):
        tracker.append(i % 100 + 1)
        total += tracker.count()
    print(total) # 198901