"""
Your task is to create an application for the departmental store. 
Initially, there was one and only one type of discount called the On-Sale-Discount (50%).
 But as time passes, the owner of the departmental store demands for including 
 some other types of discount also for the customers. 

Please, solve the above-described problem in an efficient way. 
Our actual class should store the reference to one of the strategy function.

You have the structure of your future application in the answer box preload.
"""
class Goods: 

    def __init__(self, price, discount_strategy = None):
        self.price = price
        self.discount_strategy = discount_strategy
          
    def price_after_discount(self):
        return self.price - self.discount_strategy(self) if self.discount_strategy else self.price
    
    def __str__(self):
        return f'Price: {self.price}, price after discount: {self.price_after_discount()}'

      
def on_sale_discount(order):
    return order.price / 2

def twenty_percent_discount(order): 
    return order.price / 5


print(Goods(20000))
print(Goods(20000, discount_strategy=twenty_percent_discount))