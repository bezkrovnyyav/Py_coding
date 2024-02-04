"""
Create a class hierarchy to represent different types of cars. Your hierarchy should include a base class Car and two subclasses - ElectricCar and HybridElectricCar.

Each class should have attributes:

model (car model)

year (manufacturing year)

color (color)

speed (initial speed)

In the ElectricCar class, add the attribute:

battery_capacity (battery capacity)

In the HybridElectricCar class, add the attribute:

fuel_consumption (fuel consumption)

Create a method accelerate that increases the speed of the car.

Implement the magic method to allow comparison of cars based on their speed.

Create a class CarFleet that contains a list of Car objects. 
Add a method to add car and methods to sort this list by the speed of the cars.
"""

class Car:
    def __init__(self, model, year, color, speed):
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed

    def accelerate(self, acceleration):
        self.speed += acceleration
        return None

    def __lt__(self, other):
        return self.speed < other.speed

    def __eq__(self, other):
        return self.speed == other.speed

    def __str__(self):
        return f"{self.model} - Year: {self.year}, Color: {self.color}, Speed: {self.speed} km/h"

    def __repr__(self):
        return f"Car('{self.model}', {self.year}, '{self.color}', {self.speed})"


class ElectricCar(Car):
    def __init__(self, model, year, color, speed, battery_capacity):
        super().__init__(model, year, color, speed)
        self.battery_capacity = battery_capacity
        
    def accelerate(self, acceleration):
        self.speed += acceleration
        return f"Electric car accelerates by {acceleration} km/h, current spead {self.speed}"

    def __str__(self):
        return f"{self.model} - Year: {self.year}, Color: {self.color}, Speed: {self.speed} km/h, Battery Capacity: {self.battery_capacity} kWh"


    def __repr__(self):
        return f"ElectricCar('{self.model}', {self.year}, '{self.color}', {self.speed}, {self.battery_capacity})"
        

class HybridElectricCar(Car):
    def __init__(self, model, year, color, speed, fuel_consumption):
        super().__init__(model, year, color, speed)
        self.fuel_consumption = fuel_consumption

    def accelerate(self, acceleration):
        self.speed += acceleration
        return None

    def __str__(self):
        return f"{self.model} - Year: {self.year}, Color: {self.color}, Speed: {self.speed} km/h"


    def __repr__(self):
        return f"HybridElectricCar('{self.model}', {self.year}, '{self.color}', {self.speed}, {self.fuel_consumption})"


class CarFleet:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def sort_cars_by_speed(self):
        return sorted(self.cars, key=lambda x: x.speed, reverse=False)

    def display_fleet(self):
        for car in self.cars:
            print(car)

    def __str__(self):
        return str(self.cars)


# Test data

car1 = Car("Sedan", 2022, "Blue", 120)
electric_car1 = ElectricCar("Tesla", 2023, "Black", 150, 60)
hybrid_car1 = HybridElectricCar("Toyota", 2022, "Silver", 130, 0.05)

# print([car1, electric_car1, hybrid_car1])

car_fleet = CarFleet()
car_fleet.add_car(car1)
car_fleet.add_car(electric_car1)
car_fleet.add_car(hybrid_car1)

# print(car_fleet)

sorted_cars = car_fleet.sort_cars_by_speed()
# for car in sorted_cars:
#     print(car)