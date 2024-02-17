"""
Imagine we have a washing machine which can wash the clothes, rinse the clothes and spin 
the clothes but all the tasks separately. We need a system that can automate the whole task 
without the disturbance or interference of us. 

To solve the above-described problem, we would like to hire the Facade Method. 
It will help us to hide or abstract the complexities of the subsystems as follows.

Note: the methods wash(), rinse() and spin() provide the output of the appropriate operation.
"""

class WashingMachine:

    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def startWashing(self):
        self.washing.wash()
        self.rinsing.rins()
        self.spinning.spin()


class Washing:
    
    def wash(self):
        print("Washing...")


class Rinsing:
    
    def rins(self):
        print("Rinsing...")


class Spinning:
    
    def spin(self):
        print("Spinning...")


washingMachine = WashingMachine()
washingMachine.startWashing()