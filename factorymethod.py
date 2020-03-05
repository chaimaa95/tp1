#!/user/bin/env python
# -*- coding utf-8 -*-

class PizzaFactory:
    def createPizza(type):
        pass
class PizzeriaHouma(PizzaFactory):
    def createPizza(type):
        if type == "TunaPizza" : return TunaPizza()
        elif type == "SimplePizza" : return SimplePizza()
        else: return None

class PizzeriaLux(PizzaFactory):
    def createPizza(type):
        if type == "TunaPizza" : return TunaPizza()
        elif type == "MargaritaPizza" : return MargaritaPizza()
        else: return None
class Pizza:
    def __init__(self):
      self.price=15
    def get_price(self):
        pass
class TunaPizza(Pizza):
    def get_price(self):
        print ("TunaPizza price: "+str(self.price+5))

class SimplePizza(Pizza):
    def get_price(self):
        print ("SimplePizza price: "+str(self.price))

class MargaritaPizza(Pizza):
    def get_price(self):
        print ("MargaritaPizza price: "+str(self.price+15))
def main():
    for type in ("TunaPizza","SimplePizza"):
        pizza = PizzeriaHouma.createPizza(type)
        pizza.get_price()

    for type in ("TunaPizza","MargaritaPizza"):
        pizza = PizzeriaLux.createPizza(type)
        pizza.get_price()

if __name__ == '__main__':
     main()