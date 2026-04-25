from datetime import datetime

def get_days_from_today(date: str) -> int | None:
    """Calculates the date range between current and requested dates in days.

    Arguments:
    date (str) -- The date representation in "YYYY-MM-DD" format.

    Returns:
    int | None -- The result of range calculation between two dates.
    "None" will be returned in case of incorrect date format.   
    """
    date_parsing_format = '%Y-%m-%d'
    today = datetime.now()
    requested_date = None

    try:
        requested_date = datetime.strptime(date, date_parsing_format)
    except ValueError:
        print('Incorrect date format, please check your input')     

    
    return None if requested_date is None else (today - requested_date).days


days_diff_1 = get_days_from_today('2026-04-15')
days_diff_2 = get_days_from_today('2026-12-15')

print(f'The differece of days is: {days_diff_1}')
print(f'The differece of days is: {days_diff_2}')