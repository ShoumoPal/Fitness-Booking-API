from datetime import datetime
import pytz

def convert_timezone(dt : datetime, from_tz : str, to_tz : str) -> datetime:
    from_timezone = pytz.timezone(from_tz)
    to_timezone = pytz.timezone(to_tz)
    if dt.tzinfo is None:
        dt = from_timezone.localize(dt)
    
    return dt.astimezone(to_timezone)