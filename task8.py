"""task8.py"""

from datetime import datetime, timedelta

def create_html_calendar(year, month):
    first_day = datetime(year, month, 1)
    start_day = (first_day.weekday() + 1) % 7
    days_in_month = (first_day.replace(month=month % 12 + 1, day=1) - timedelta(days=1)).day
    
    html_calendar = '<html><body><table border="1">\n'
    html_calendar += '<tr><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr>\n'
    
    html_calendar += '<tr>'
    for _ in range(start_day):
        html_calendar += '<td></td>'
    
    for day in range(1, days_in_month + 1):
        html_calendar += f'<td>{day}</td>'
        if (start_day + day) % 7 == 0:
            html_calendar += '</tr>\n<tr>'
    
    html_calendar += '</tr>\n</table></body></html>'
    
    with open('calendar.html', 'w') as f:
        f.write(html_calendar)
    
    print("HTML-календарь создан и сохранён как 'calendar.html'.")

if __name__ == "__main__":
    year = int(input("Введите год: "))
    month = int(input("Введите месяц: "))
    create_html_calendar(year, month)
