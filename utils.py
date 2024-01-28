from math import ceil
from datetime import datetime
from pydantic import BaseModel


class DeliveryDetails(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: str


def validate_input(body: DeliveryDetails):
    """
    Return error message as a string if there is any,
    else returns None
    """
    if (not isinstance(body.cart_value, int) or
            not isinstance(body.delivery_distance, int) or
            not isinstance(body.number_of_items, int) or
            not isinstance(body.time, str)):
        return "JSON Data in invalid format"
    try:
        datetime.fromisoformat(body.time)
    except:
        return "Date in incorrect format"
    return False


def fee_calculator(body: DeliveryDetails):
    if body.cart_value >= 20000:
        return 0

    fee = 0

    # Add surcharge if value less than 1000c
    if body.cart_value < 1000:
        fee += 1000 - body.cart_value

    # Add 200c + 100c for each starting 500m after 1km
    fee += max(200, ceil(body.delivery_distance / 500) * 100)

    # Add 50c for each item above the 4th + 120c if amount of items exceeds 12
    if body.number_of_items >= 5:
        fee += (body.number_of_items - 4) * 50
        if body.number_of_items >= 12:
            fee += 120

    # Rush hour multiplier
    parsedtime = datetime.fromisoformat(body.time)
    if parsedtime.date().isoweekday() == 5 and 15 <= parsedtime.time().hour < 19:
        fee *= 1.2

    if fee <= 1500:
        return fee
    return 1500
