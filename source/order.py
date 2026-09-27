def calculate_order_total(items, discount_code=None):
    """
    items: list of dictionaries
    Each item must contain:
        name: str
        price: positive number
        quantity: positive integer

    Discount codes:
        SAVE10  -> 10% discount
        SAVE20  -> 20% discount
        None    -> no discount

    Rules:
        - items must be a non-empty list
        - price must be > 0
        - quantity must be a positive integer
        - discount code must be None, SAVE10, or SAVE20
        - subtotal cannot exceed 100000

    Returns:
        Final order total after discount.
    """

    if not isinstance(items, list):
        raise TypeError("Items must be a list")

    if not items:
        raise ValueError("Order cannot be empty")

    subtotal = 0

    for item in items:
        if not isinstance(item, dict):
            raise TypeError("Each item must be a dictionary")

        if "name" not in item or "price" not in item or "quantity" not in item:
            raise ValueError("Item must contain name, price and quantity")

        if not isinstance(item["name"], str) or not item["name"].strip():
            raise ValueError("Invalid item name")

        if not isinstance(item["price"], (int, float)):
            raise TypeError("Price must be a number")

        if item["price"] <= 0:
            raise ValueError("Price must be positive")

        if not isinstance(item["quantity"], int):
            raise TypeError("Quantity must be an integer")

        if item["quantity"] <= 0:
            raise ValueError("Quantity must be positive")

        subtotal += item["price"] * item["quantity"]

    if subtotal > 100000:
        raise ValueError("Order total cannot exceed 100000")

    if discount_code not in (None, "SAVE10", "SAVE20"):
        raise ValueError("Invalid discount code")

    if discount_code == "SAVE10":
        subtotal *= 0.90
    elif discount_code == "SAVE20":
        subtotal *= 0.80

    return round(subtotal, 2)