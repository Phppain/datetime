"""task6.py"""

from datetime import datetime

def days_between_dates(date1, date2):
    delta = date2 - date1
    return abs(delta.days)

if __name__ == "__main__":
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(input("Введите первую дату (YYYY-MM-DD): "), date_format)
    date2 = datetime.strptime(input("Введите вторую дату (YYYY-MM-DD): "), date_format)
    print("Количество дней между датами:", days_between_dates(date1, date2))
