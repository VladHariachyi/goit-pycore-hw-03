import re;

def normalize_phone(phone_number: str) -> str:
    """Refactros the phone number format.

    Arguments:
    phone_number (str) -- The phone number required to be formatted.

    Returns:
    str -- The formatted phone number.
    """
    country_code = "+380";
    cleaned_phone_number = re.sub(r"\D", "", phone_number)
    phone_number_with_country_code = re.sub(r"380|^0", country_code, cleaned_phone_number)

    return phone_number_with_country_code;


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\nNa",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Formatted phone numbers for SMS-mailings", sanitized_numbers)