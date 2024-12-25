from datetime import datetime

def get_days_from_today(date): # calculates the number of days between a given date and the current date.
    now = datetime.today()
    date = datetime.strptime(date, '%Y-%m-%d')
    difference = now - date
    return int(difference.days)

text = get_days_from_today("2045-10-09")
print(text)
