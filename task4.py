"""task4.py"""

from datetime import date

def add_years(base_date, years):
    try:
        new_date = base_date.replace(year=base_date.year + years)
    except ValueError:
        if base_date.month == 2 and base_date.day == 29:
            new_date = base_date.replace(year=base_date.year + years, day=28)
        else:
            raise
    return new_date

if __name__ == "__main__":
    print(add_years(date(2015, 1, 1), -1))
    print(add_years(date(2015, 1, 1), 0))
    print(add_years(date(2015, 1, 1), 2))
    print(add_years(date(2000, 2, 29), 1))

