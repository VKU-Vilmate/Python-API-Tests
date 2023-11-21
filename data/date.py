import datetime
from dateutil.relativedelta import *


def string_date(months: int):
    date = datetime.datetime.now() - relativedelta(months=months)
    return date.strftime("%Y-%m-%d")


def current_month():
    return datetime.datetime.now().month


def current_year():
    return datetime.datetime.now().year


def past_date(months: int):
    past_date = datetime.datetime.now() - relativedelta(months=months)
    month = past_date.month
    year = past_date.year
    return month, year
