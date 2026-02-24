# Lab 13
# Kamal Ali & William Nguyen
# 11/19/2024
# A list of Task objects, can add, view, and remove tasks, includes an iterator, and can save changes made to the .txt file

from task import Task

class Tasklist:
    def __init__(self):
        self.tasklist = []  # create list of tasks

        with open("tasklist.txt", "r") as file:     # read file
            for line in file:
                line = line.strip()     # remove \n
                if line == "":          # empty line
                    continue
                desc, date, time = line.split(",")      # create desc, date, time variables
                self.tasklist.append(Task(desc, date, time))    # append Task object to task list

        self.tasklist.sort()    # sort the list

    def add_task(self, desc, date, time):
        self.tasklist.append(Task(desc, date, time))        # construct new task and append it to the tasklist
        self.tasklist.sort()            # sort the list

    def get_current_task(self):
        if len(self.tasklist) == 0:     # No more tasks
            return None
        return self.tasklist[0]         # return task at the beginning of the list

    def mark_complete(self):
        if len(self.tasklist) == 0:     # No more tasks
            return None
        return self.tasklist.pop(0)     # remove and return the current task from the task list

    def save_file(self):
        with open("tasklist.txt", "w") as file:     # write into file
            for task in self.tasklist:
                file.write(repr(task) + "\n")       # write each line of tasks into the file

    def __len__(self):
        return len(self.tasklist)   # return number of items in tasklist

    def __iter__(self):
        self.n = -1          # counter for the iterator
        return self

    def __next__(self):
        self.n += 1     # iterate one position at atime
        if self.n >= len(self.tasklist):    # raise StopIteration when iterator reaches end of tasklist
            raise StopIteration
        else:
            return self.tasklist[self.n]    # return Task object at current position