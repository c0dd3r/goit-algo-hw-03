from datetime import datetime

def get_days_from_today(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    date_today = datetime.today()
    difference = date_today - date
    return difference.days
