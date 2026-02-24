# Lab 13
# Kamal Ali & William Nguyen
# 11/19/2024
# A program that maintains a list of tasks for the user, allowing the user to view tasks and mark them as complete.

from tasklist import Tasklist
import check_input

def main_menu():
    print("1. Display current task")        # print menu
    print("2. Display all tasks")
    print("3. Mark current task complete")
    print("4. Add new task")
    print("5. Search by date")
    print("6. Save and quit")

    choice = check_input.get_int_range("Enter choice: ",1,6)
    return choice   # return menu choice

def get_date():
    month = check_input.get_int_range('Enter month: ',1,12)

    day = check_input.get_int_range("Enter day: ",1,31)

    year = check_input.get_int_range("Enter year: ",2000,2100)

    return f"{month:02d}/{day:02d}/{year}"  # return mm/dd/yyyy


def get_time():
    hour = check_input.get_int_range('Enter hour: ', 0,23)

    minute = check_input.get_int_range('Enter minute: ',0,59)

    return f"{hour:02d}:{minute:02d}"   # return hh/mm


def main():
    tasks = Tasklist()  # make a list of tasks

    while True:
        print("-Tasklist-")
        print("Tasks to complete: ",len(tasks))     # show how many tasks left
        choice = main_menu()    # print menu and get user choice

        if choice == 1:     # 1. Display current task
            current_task = tasks.get_current_task()
            if current_task is None:                # no more tasks
                print("No current task.")
            else:
                print("Current task is:")
                print(current_task)

        elif choice == 2:   # 2. Display all tasks
            print("Tasks:")
            count = 1
            for current_task in tasks:                  # iterate through each task in the tasks list
                print(f"{count}. {current_task}")       # print the task number followed by the task
                count += 1                              # increase task number
        elif choice == 3:   # 3. Mark current task complete
            current_task = tasks.get_current_task()     # get first task in tasks list
            if current_task is None:                    # no more tasks
                print("No current task")
            else:
                print("Marking current task as complete:\n", current_task)
                tasks.mark_complete()           # remove task from list
                new_task = tasks.get_current_task()
                if new_task is None:
                    print("All tasks complete!")
                else:
                    print("New current task is:")
                    print(new_task)
        elif choice == 4:     # 4. Add new task
            desc = input("Enter a task: ")      # user inputs a string

            print("Enter due date:")
            date = get_date()                   # create date variable in the mm/dd/yyyy format

            print("Enter time:")
            time = get_time()                   # get the time

            tasks.add_task(desc, date, time)    # make a new task and add it to the tasks list
        elif choice == 5:   # 5. Search by date
            print("Enter date to search:")
            date = get_date()                   # search a date in the mm/dd/yyyy format

            print(f"Tasks due on {date}:")
            count = 1
            for current_task in tasks:
                if current_task.date == date:
                    print(f"{count}. {current_task}")   # print the task with the matching date
                    count += 1

        elif choice == 6:   # 6. Save and quit
            print("Saving List...")
            tasks.save_file()   # write to .txt file
            break               # end while loop
        
        print()

if __name__ == "__main__":
    main()