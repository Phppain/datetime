"""task1.py"""

from datetime import date

def get_week_number(year, month, day):
    d = date(year, month, day)
    return d.isocalendar()[1]

if __name__ == "__main__":
    year, month, day = map(int, input("Enter a date: ").split())
    week_number = get_week_number(year, month, day)
    print(week_number)
