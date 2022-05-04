import pytz
from datetime import date, time, datetime


def aware_utc_now():
    """
    :return: UTC time with timezone info.
    :rtype: datetime.datetime
    """
    return pytz.utc.localize(datetime.utcnow())


def aware_utc_midnight():
    """
    :return: Today's midnight with UTC timezone.
    :rtype: datetime.datetime
    """
    naive = datetime.combine(date.today(), time.min)
    return pytz.utc.localize(naive)
