class Coffee:

    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)
    
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if type(value) is str and len(value) >= 3 and not hasattr(self, "name"):
            self._name = value
        else:
            print("cannot change the name of the coffee")

    name = property(get_name, set_name)

    def orders(self):
        pass
    
    def customers(self):
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass

class Customer:

    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
        
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if type(value) is str and 1 <= len(value) <= 15:
            self._name = value
        else:
            print("Not a name")
        
    name = property(get_name, set_name)

    def orders(self):
        for order in Order.all:
            if order.customer == self and type(order.customer) is Customer:
                return order.customer
            else:
                print("no")
    
    def coffees(self):
        pass
    
    def create_order(self, coffee, price):
        pass
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    def get_price(self):
        return self._price
    
    def set_price(self, value):
        if type(value) is float and 1.0 <= value <= 10.0 and not hasattr(self, "price"):
            self._price = value
        else:
            print("cannot change the price of the coffee")

    price = property(get_price, set_price)