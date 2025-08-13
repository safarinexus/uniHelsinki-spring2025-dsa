'''
Your task is to design a class that supports adding courses and their prerequisite relations, and finding a way to take the courses in an order that satisfies the requisites.

Example: There are four courses Jym, Ohpe, Ohja and Tira. The prerequisites are:

Ohpe has to be taken before Ohja
Ohja has to be taken before Tira
Jym has to be taken before Tira
In this case, the satisfactory course orders are:

Jym, Ohpe, Ohja, Tira
Ohpe, Jym, Ohja, Tira
Ohpe, Ohja, Jym, Tira
You can return any satisfactory course order. In the example above, there are three different acceptable answers.

In a file courseplan.py, implement the class CoursePlan with the following methods:

add_course adds a course with the given name
add_requisite adds a prerequisite
find_order returns a satisfactory course order as a list
The method find_order can return any satisfactory order. If there is no satisfactory order, the method should return None.
'''

class CoursePlan:
    def __init__(self):
        pass

    def add_course(self, course):
        pass

    def add_requisite(self, course1, course2):
        pass

    def find_order(self):
        pass

if __name__ == "__main__":
    courses = CoursePlan()

    courses.add_course("Ohpe")
    courses.add_course("Ohja")
    courses.add_course("Tira")
    courses.add_course("Jym")

    courses.add_requisite("Ohpe", "Ohja")
    courses.add_requisite("Ohja", "Tira")
    courses.add_requisite("Jym", "Tira")

    print(courses.find_order()) # esim. [Ohpe, Jym, Ohja, Tira]

    courses.add_requisite("Tira", "Tira")

    print(courses.find_order()) # None