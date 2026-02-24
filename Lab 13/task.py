# Lab 13
# Kamal Ali & William Nguyen
# 11/19/2024
# A class that holds the methods for a Task object

class Task:
    def __init__(self, desc, date, time):
        self.description = desc
        self.date = date    # month/day/year
        self.time = time    # hour/minute

    def __str__(self):  # print the task in main()
        return f"{self.description} - Due: {self.date} at {self.time}"

    def __repr__(self):      # prints the task as a string, separated by commas  - used for save_file()
        return f"{self.description},{self.date},{self.time}"

    def __lt__(self, other):
        monthSelf, daySelf, yearSelf = self.date.split("/")     # get "month", "day", "year"
        monthSelf = int(monthSelf)  # convert strings into int
        daySelf = int(daySelf)
        yearSelf = int(yearSelf)

        monthOther, dayOther, yearOther = other.date.split("/") # other date
        monthOther = int(monthOther)
        dayOther = int(monthOther)
        yearOther = int(yearOther)

        if yearSelf != yearOther:           # compare year
            return yearSelf < yearOther
        if monthSelf != monthOther:         # compare month
            return monthSelf < monthOther
        if daySelf != dayOther:             # compare day
            return daySelf < dayOther

        hourSelf, minuteSelf = self.time.split(":")     # get "hour", "minute"
        hourSelf = int(hourSelf)    # convert strings into int
        minuteSelf = int(minuteSelf)

        hourOther, minuteOther = other.time.split(":")  # other time
        hourOther = int(hourOther)
        minuteOther = int(minuteOther)

        if hourSelf != hourOther:       # compare hour
            return hourSelf < hourOther
        if minuteSelf != minuteOther:   # compare minute
            return minuteSelf < minuteOther

        return self.description < other.description # compare alphabet