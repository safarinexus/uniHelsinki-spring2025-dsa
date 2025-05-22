'''
The participants of a contest send in their solutions for tasks. 
The tasks are numbered 1,2,3,... and a solution for each task is worth 0-100 points.
If a contestant submits multiple solutions to the same task, the score for the task is the maximum score of a single solution.
The total score of a contestant is the sum of scores over all tasks.
Your task is to compile the score board of the contest containing the name and the total score of each contestant.
The contestants are sorted by their score from the highest to the lowest.
If two contestants have the same score, the one that achieved this score first is listed higher.
If two or more participants have a score 0, they are listed in alphabetical order.
In a file contest.py, implement a class Contest with the following methods:

__init__: constructs an object of the class
add_submission: processes the submission of a contestant
create_scoreboard: creates the score board of the contest

The following example illustrates the use of the class in detail.

Tiina is before Pekka on the score board because she reached the score 50 earlier.
Anna is before Kalle on the score board, because both have 0 points and Anna is earlier in alphabetical order.
'''

class Contest:
    def __init__(self, names, task_count):
        self.contestants = {}
        for i in names:
            self.contestants[i] = { 'tasks': {}, 'order': 0 }
            for j in range(1, task_count + 1):
                self.contestants[i]['tasks'][j] = 0
        
        self.submissions = []
        self.scoreboard = []

    def add_submission(self, name, task, score):
        self.submissions.append((name, task, score))

    def create_scoreboard(self):
        for i in range(len(self.submissions)):
            name = self.submissions[i][0]
            task = self.submissions[i][1]
            score = self.submissions[i][2]
            if score > self.contestants[name]['tasks'][task]:
                self.contestants[name]['tasks'][task] = score 
                self.contestants[name]['order'] = i 

        sorter = {}
        arrangement = []

        for key in self.contestants:
            total = sum(self.contestants[key]['tasks'].values())
            if total not in arrangement:
                arrangement.append(total)
            if total in sorter:
                sorter[total].append((key, self.contestants[key]['order']))
            else:
                sorter[total] = [(key, self.contestants[key]['order'])] 

        arrangement.sort(reverse=True)

        for j in arrangement:
            if j == 0:
                self.scoreboard.extend(sorted(sorter[j]))
            elif len(sorter[j]) > 1:
                 self.scoreboard.extend(sorted(sorter[j], key=lambda x: x[1]))
            else:
                self.scoreboard.extend(sorter[j])

        for l in range(len(self.scoreboard)):
            total = sum(self.contestants[self.scoreboard[l][0]]['tasks'].values())
            self.scoreboard[l] = (self.scoreboard[l][0], total)

        return self.scoreboard

if __name__ == "__main__":
    names = ["anna", "pekka", "kalle", "tiina", "eeva"]
    contest = Contest(names, 3)

    contest.add_submission("tiina", 2, 30)
    contest.add_submission("pekka", 1, 40)
    contest.add_submission("tiina", 1, 20)
    contest.add_submission("pekka", 1, 50)
    contest.add_submission("pekka", 2, 0)
    contest.add_submission("eeva", 3, 100)
    contest.add_submission("anna", 1, 0)
    contest.add_submission("eeva", 3, 80)
    contest.add_submission("tiina", 2, 30)

    scoreboard = contest.create_scoreboard()
    print(scoreboard)
    # [('eeva', 100), ('tiina', 50), ('pekka', 50), ('anna', 0), ('kalle', 0)]