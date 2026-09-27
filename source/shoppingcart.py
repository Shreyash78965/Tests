class ShoppingCart:

    def __init__(self):
        self.items = {}

    def add_item(self, item: str, price: float):
        if price <= 0:
            raise ValueError("Price must be positive")
        self.items[item] = price

    def get_total(self, discount_percent: float = 0) -> float:
        if not 0 <= discount_percent <= 100:
            raise ValueError("Invalid discount percentage")

        subtotal = sum(self.items.values())
        return subtotal * (1 - discount_percent / 100)