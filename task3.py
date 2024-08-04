"""task3.py"""

from datetime import datetime, timedelta

def find_sundays(year):
    start_date = datetime(year, 1, 1)
    if start_date.weekday() != 6:
        start_date += timedelta(days=(6 - start_date.weekday()))
    
    sundays = []
    current_date = start_date
    while current_date.year == year:
        sundays.append(current_date)
        current_date += timedelta(weeks=1)
    
    return sundays

if __name__ == "__main__":
    try:
        year = int(input("Введите год: "))
    except TypeError:
        print("TypeError")
    sundays = find_sundays(year)
    for sunday in sundays:
        print(sunday.strftime('%Y-%m-%d'))
