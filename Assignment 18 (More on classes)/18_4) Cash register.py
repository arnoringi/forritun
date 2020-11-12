class CashRegister:
    def __init__(self, tax=0):
        self.tax = tax
        self.items = 0
        self.price = 0
        self.price_tax = 0

    def __str__(self):
        return "Items: {}, total price: {:.2f}, including tax: {:.2f}".format(self.items, self.price, self.price_tax)

    def add_item(self, price, taxable):
        self.items += 1
        if taxable: # With tax
            self.price += price
            self.price_tax += price * (1 + (self.tax/100))
        else: # Without tax
            self.price += price
            self.price_tax += price
        
    def get_count(self):
        return self.items

    def get_total(self):
        return self.price

    def get_total_with_tax(self):
        return self.price_tax

    def clear(self):
        self.items = 0
        self.price = 0
        self.price_tax = 0
        return self.__str__()