"""task5.py"""

from datetime import datetime, timezone

def get_time_info():
    utc_now = datetime.now(timezone.utc)
    local_time = datetime.now()
    
    print("Время по Гринвичу (UTC):", utc_now.strftime('%Y-%m-%d %H:%M:%S %Z'))
    print("Местное время:", local_time.strftime('%Y-%m-%d %H:%M:%S %Z'))

if __name__ == "__main__":
    get_time_info()
