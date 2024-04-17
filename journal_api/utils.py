from datetime import datetime

def current_date():
    cur = datetime.now()
    day = cur.day
    month = cur.month
    year = cur.year

    return f"{day}-{month}-{year}"

    