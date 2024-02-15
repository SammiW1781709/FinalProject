class ParentSchedule:
    def __init__(self):# define schedule function
        self.parentschedule = {}

    def addStudentName(self, time, student): # student function
        if time in self.parentschedule:
            self.parentschedule[time].append(student)
        else:
            self.parentschedule[time] = [student]

    def teacherview(self, Teacher_name): # define teacher function
        for time, students in sorted(self.parentschedule.items()):
                print(f"{students} at {time}")

def createtimeslots(): # define time funtion 
    times = []
    timeslot = 16.0  # set the start time at 4.30PM represented as 16.5
    while timeslot <= 20.0:  # ensures time slots run until 8 PM
        times.append(timeslot)
        timeslot += 0.167 # time slots will be every 30 minutes
    else:
        timeslot += 1
    return times

def timeslotsavalible(): # define the availbe slots 
    print("time slots available")
    for index, time in enumerate(createtimeslots(), start=1):
        hours, minutes = divmod(int(time * 60), 60)
        print(f"{index}. {hours:02d}:{minutes:02d}")

def MAINMENU(): # creating the user menu 
    parent_schedule = ParentSchedule()

    while True:
        print("1. Add meeting for student")
        print("2. View schedule")
        print("3. Exit")

        choice = input("Please select option: ")
        if choice == '1':
            timeslotsavalible()
            try:
                selected_index = int(input("Select Time: "))
                selected_time = createtimeslots()[selected_index - 1]
                name = input("Student Name: ")
                parent_schedule.addStudentName(selected_time, name)
            except (ValueError, IndexError):
                print("Invalid option.")
        elif choice == '2':
            parent_schedule.teacherview(Teacher_name)
        elif choice == '3':
            print("GOODBYE")
            break
        else:
            print("Invalid option Try again")

if __name__ == "__main__":
    MAINMENU()
