from random import sample;

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """Generates unique lottery numbers.

    Arguments:
    min (int) -- The start point of the lottery numbers range.
    max (int) -- The end point of the lottery numbers range.
    quantity (int) -- The amount of lottery numbers which need to take from the range.

    Returns:
    list[int] -- The selected lottery numbers in range. The empty list
    will be if:
    -- "min" less than 1;
    -- "max" greater than 1000;
    -- "quantity" less than 1 or greater than max availalble numbers in range;
    """
    is_range_valid = min >= 1 and (max >= min and max <= 1000); 
    available_quantity_amount = (max - min) + 1;
    is_quantity_in_ranage = quantity >= 0 and quantity <= available_quantity_amount;

    if not is_range_valid or not is_quantity_in_ranage:
        return [];


    return sample(range(min, max + 1), quantity);


print(f"The lottery numbers are: {get_numbers_ticket(1, 49, 6)}")
print(f"The lottery numbers are: {get_numbers_ticket(995, 1000, 3)}")
print(f"The lottery numbers are: {get_numbers_ticket(1, 10, 10)}")


