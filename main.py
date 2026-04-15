class Fruits :
    def __init__(self, fruit, quantity, price):
        self.fruit = fruit
        self.quantity = quantity
        self.price = price

apple = Fruits("apple", 3, 1.5)
banana = Fruits("banana", 1, 1.25)
orange = Fruits("orange", 6, 2.0)
grape = Fruits("grape", 4, 3.5)
    
for Fruits in [apple, banana, orange, grape]:
    print(Fruits.fruit, Fruits.quantity, Fruits.price)