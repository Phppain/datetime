"""task7.py"""

from datetime import datetime

def difference_to_dhms(date1, date2):
    delta = abs(date2 - date1)
    days = delta.days
    seconds = delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return days, hours, minutes, seconds

if __name__ == "__main__":
    date_format = "%Y-%m-%d %H:%M:%S"
    date1 = datetime.strptime(input("Введите первую дату и время (YYYY-MM-DD HH:MM:SS): "), date_format)
    date2 = datetime.strptime(input("Введите вторую дату и время (YYYY-MM-DD HH:MM:SS): "), date_format)
    days, hours, minutes, seconds = difference_to_dhms(date1, date2)
    print(f"Разница: {days} дней, {hours} часов, {minutes} минут, {seconds} секунд")
