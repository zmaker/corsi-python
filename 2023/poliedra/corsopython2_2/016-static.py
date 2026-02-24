class Bakery:
    type = 'cake'                  # Class Variable
    def __init__(self,flavor,price):
        self.flavor = flavor            # Instance Variable
        self.price = price            # Instance Variable
 
# Objects of Bakery class
a = Bakery('Butterscotch Cake', 300)
b = Bakery('Chocolate-Truffle Cake', 250)

a.type = 'xxx'
print(a.type)  # prints "cake"
print(b.type)  # prints "cake"
print(a.flavor)    # prints "Butterscotch Cake"
print(b.flavor)    # prints "Chocolate-Truffle Cake"
print(a.price)    # prints "300"
print(b.price)    # prints "250"