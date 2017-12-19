class ToDoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def ToList(self):
        output = ''
        for task in self.tasks:
            output += task.ToString() + '\n'
        return output       

class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

    def ToString(self):
        return 'Priority: ' + str(self.priority) + '\tTask: "' + self.description + '"'

myTasks = ToDoList()

task1 = Task('Get a job', 2)
task2 = Task('Do the washing', 1)
task3 = Task('Play some music', 3)

myTasks.add(task2)
myTasks.add(task1)
myTasks.add(task3)

print myTasks.ToList()

