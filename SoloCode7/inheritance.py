from abc import ABC, abstractmethod

# The base class
class Item(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_cost(self):
        pass # Is put in the subclasses


# The sub -classes
class ByWeightItem(Item):

    def __init__(self, name, weight, cost_per_pound):
        super().__init__(name)
        self.weight = weight
        self.cost_per_pound = cost_per_pound

    def calculate_cost(self):
        return self.weight * self.cost_per_pound
    

class ByQuantityItem(Item):
    def __init__(self, name, quantity, cost_each):
        super().__init__(name)
        self.quantity = quantity
        self.cost_each = cost_each

    def calculate_cost(self):
        return self.quantity * self.cost_each
    

# Specific classes for products
class Grapes(ByWeightItem):
    def __init__(self, weight):
        super().__init__("Grapes", weight, 2.0)

class Bananas(ByWeightItem):
    def __init__(self, weight):
        super().__init__("Bananas", weight, 1.5)

class Oranges(ByQuantityItem):
    def __init__(self, quantity):
        super().__init__("Oranges", quantity, 1.0)

class Cantaloupes(ByQuantityItem):
    def __init__(self, quantity):
        super().__init__("Cantaloupes", quantity, 4.0)


# Order class for holding all the items
class Order:
    def __init__(self):
        self.items = [] # starting list to store items

    def add_item(self, item):
        self.items.append(item)  # adding item to list   

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.calculate_cost() # add each cost per item to total cost
        return total
    
    def get_items(self):
        return self.items
    
    def __len__(self):
        return len(self.items)  # number of items
    

# running the program
order = Order() # creating a order

# adding items
order.add_item(Grapes(2))
order.add_item(Bananas(3))
order.add_item(Oranges(4))
order.add_item(Cantaloupes(5))

print ("reciept:")
for item in order.get_items():
    print(item.name, item.calculate_cost())

print ("total:" , order.calculate_total(), "$") # the total cost of the order
print ("number of items:", len(order)) # the number of items in order



