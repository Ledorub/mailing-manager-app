import pytz
from datetime import datetime


def aware_utc_now():
    """
    :return: UTC time with timezone info.
    :rtype: datetime.datetime
    """
    return pytz.utc.localize(datetime.utcnow())
