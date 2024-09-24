class Product:
    def __init__(self, name, price, quantity):
        """
        Initialize the product with a name, price, and quantity.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_value(self):
        """
        Calculate the total value of the product stock.
        """
        return self.price * self.quantity