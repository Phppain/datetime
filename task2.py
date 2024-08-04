"""task2.py"""

from datetime import datetime, timedelta

def get_first_monday_of_week(year, week_number):
    first_day_of_year = datetime(year, 1, 1)
    first_monday_of_year = first_day_of_year + timedelta(days=(7 - first_day_of_year.weekday()) % 7)
    first_day_of_week = first_monday_of_year + timedelta(weeks=week_number - 1)
    return first_day_of_week

if __name__ == "__main__":
    year, week_number = map(int, input("Enter a date: ").split())
    first_monday = get_first_monday_of_week(year, week_number)
    print(f"{first_monday.strftime('%a %d %B %Y %H:%M:%S')}")

