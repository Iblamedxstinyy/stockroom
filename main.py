import sys


def _setup_utf8_console() -> None:
    for stream in (sys.stdout, sys.stderr, sys.stdin):
        try:
            stream.reconfigure(encoding="utf-8")
        except Exception:
            pass


_setup_utf8_console()


class Fruits :
    def __init__(self, fruit, quantity, price):
        self.fruit = fruit
        self.quantity = quantity
        self.price = price

    def Add(self):
        q = int(input("впишите количество новых предметов: "))
        self.quantity += q
        print(f"новое количество предметов {self.quantity}")

    def Subtraction(self):
        q = int(input("впишите количество предметов отнять: "))
        self.quantity -= q
        print(f"новое количество предметов {self.quantity}")
    

apple = Fruits("apple", 3, 1.5)
banana = Fruits("banana", 1, 1.25)
orange = Fruits("orange", 6, 2.0)
grape = Fruits("grape", 4, 3.5)
    


while True:
    qu = int(input(f'выберете действие(1 посмотреть товары)(2 добавить товары)(3 отнять товары)(4 выход)'))
    if qu == 1 :
        for item in [apple, banana, orange, grape]:
            print(item.fruit, item.quantity, item.price)
    elif qu == 2:
        qu2 =int(input(f'к чему добавить(1 apple)(2 banana)(3 orenge)(4grape)'))
        if qu2 == 1:
            apple.Add()
        if qu2 == 2:
            banana.Add()
        if qu2 == 3:
            orange.Add()
        if qu2 == 4:
            grape.Add()
    elif qu == 3:
        qu2 =int(input(f'к чему отнять(1 apple)(2 banana)(3 orenge)(4grape)'))
        if qu2 == 1:
            apple.Subtraction()
        if qu2 == 2:
            banana.Subtraction()
        if qu2 == 3:
            orange.Subtraction()
        if qu2 == 4:
            grape.Subtraction()
    elif qu == 4:
        break
