





#  DO NOT TURN IN. THIS IS AI GENERATED EXAMPLE/REFERENCE CODE!!!!





months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
start = 0  # Sunday as index 0

def print_calendar():
    global start
    for month, days in months.items():
        print("\n{}".format(month))
        print("Su Mo Tu We Th Fr Sa")
        
        # Add leading spaces for the first week
        for _ in range(start):
            print("   ", end="")

        # Print days of the month
        for day in range(1, days + 1):
            print(f"{day:2}", end=" ")
            start = (start + 1) % 7
            if start == 0:
                print()
    
        print()

print_calendar()