from datetime import datetime, timedelta;

def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    """Generates a list of upcoming birthdays for 7 days in advance including today.

    Arguments:
    users (dict) -- The list of users, birthdays of whose need to check. 
    The user dictionary consist of folloiwng properties:
        -- user.name (str) -- Determines the user name
        -- user.birthday (str) -- Determines the user birthday date in following format 'YYYY.MM.DD' 

    Returns:
    users (dict) -- The list of users whose need to congratulate on this week. Users who have already
    had their birthday will be congratulated next year on their birthday date. The user dictionary 
    consist of folloiwng properties:
        -- user.name (str) -- Determines the user name
        -- user.congratulation_date (str) -- Determines the scheduled congratulation date. Users who 
        have birthday on the weekend will be congratulated on the Monday of the next week. 
    """
    date_format = "%Y.%m.%d"
    today = datetime.now().date()
    upcoming_birthdays = []

    for user in users:
        try:
            user_birthday = datetime.strptime(user["birthday"], date_format).date()
        except ValueError:
            print(f"The date format is incorrect for {user}, expected format 'YYYY.MM.DD'")
            continue

        birthday_this_year = datetime(year=today.year, month=user_birthday.month, day=user_birthday.day).date()

        if birthday_this_year < today:
            next_year_birthday_date = birthday_this_year.replace(year=birthday_this_year.year + 1)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": datetime.strftime(next_year_birthday_date, date_format)
            })

            continue
        
        upcoming_birthday_max_date = today + timedelta(days=6)
        is_date_in_range = birthday_this_year >= today and birthday_this_year <= upcoming_birthday_max_date

        if not is_date_in_range:
            continue
    
        saturday_weekday_number = 5
        sunday_weekday_number = 6
        is_birthday_on_weekend = birthday_this_year.weekday() in [saturday_weekday_number, sunday_weekday_number]
        congratulation_date = None

        if is_birthday_on_weekend:
            week_days_amount = 7
            amount_days_to_shift = week_days_amount - birthday_this_year.weekday()
            congratulation_date = birthday_this_year + timedelta(days=amount_days_to_shift)
        else:
            congratulation_date = birthday_this_year
        
        upcoming_birthdays.append({
            "name": user["name"],
            "congratulation_date": datetime.strftime(congratulation_date, date_format)
        })
    
    return upcoming_birthdays



users = [
    { "name": "John Doe", "birthday": "1980.04.22"},    # already celebrated
    { "name": "Lisa Doe", "birthday": "1980.04.26"},    # on this week but on weekend
    { "name": "Marcus Doe", "birthday": "1980.04.28"},  # on this week
    { "name": "Peter Doe", "birthday": "1980.05.15"},   # in future, outside of 7 days range
]

upcoming_birthdays = get_upcoming_birthdays(users)

print(f"Upcoming birthdays on this week: {upcoming_birthdays}")