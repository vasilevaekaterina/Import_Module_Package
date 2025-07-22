import datetime as dt


def today_date():
    today = dt.date.today()
    date = dt.date.strftime(today, '%d.%m.%Y')
    print(date)
