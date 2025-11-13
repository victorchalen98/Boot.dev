import datetime

def sort_dates(dates):
    sorted_dates = sorted(dates, key=transform_date)
    return sorted_dates


def transform_date(dates):
    return datetime.datetime.strptime(dates, "%m-%d-%Y")
