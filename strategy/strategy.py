from __future__ import annotations
from abc import ABC, abstractclassmethod

class Order:
    def __init__(self, total: float, discount: DiscountStrategy):
        self._total = total
        self._discount = discount
        
    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self._total)
    

class DiscountStrategy(ABC):
    
    @abstractclassmethod
    def calculate(self, value: float) -> float: pass


class TwentPercent(DiscountStrategy):
    def calculate(self, value:float) -> float:  
        return value - ( value * 0.2 )

class FiftyPercent(DiscountStrategy):
    def calculate(self, value:float) -> float:  
        return value - ( value * 0.5 )

class NoDiscount(DiscountStrategy):
    def calculate(self, value):
        return value 

if __name__ == "__main__":
    twenty_percent = TwentPercent()
    order = Order(1000, twenty_percent)

    print(order.total)
    print(order.total_with_discount)
    print("===============")

    fifty_percent = FiftyPercent()
    order = Order(1000, fifty_percent)
    print(order.total)
    print(order.total_with_discount)

    print("===============")

    no_discount = NoDiscount()
    order = Order(1000, no_discount)
    print(order.total)
    print(order.total_with_discount)