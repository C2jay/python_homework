from math import sqrt

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*(self.width + self.height)

    def diagonal(self):
        return sqrt(self.width**2 + self.height**2)
    
    def is_square(self):
        if self.width == self.height:
            return f"That's a square!"
        else:
            return f"That's a rectangle, fool!"

rectangle_1 = Rectangle(5,5)

print(rectangle_1.is_square())


# Q3 cars go vroom vroom!

class Cars:

    def __init__(self, make, model, colour, seating, max_speed):
        self.make = make
        self.model = model
        self.colour = colour
        self.seating = seating
        self.max_speed = max_speed
        self.fuel_gauge = 100

    def __str__(self):
        return f" This vehicle is a {self.colour} {self.make} {self.model}. It can seat {self.seating} people and has a max speed of {self.max_speed}. "

    def rev_engine(self):
        return "VRRRRRRRRM!!!!!!!!"

    def measure_fuel(self, kilometers):
        fuel_level = self.fuel_gauge - kilometers
        self.fuel_gauge = fuel_level
        if self.fuel_gauge <= 20:
            return f"fuel levels low - you have {self.fuel_gauge}% left in the tank."
        else:
            return self.fuel_gauge



car_1 = Cars("toyota", "yaris", "black", 4, "150km/hr")

print(car_1.measure_fuel(50))
print(car_1.measure_fuel(30))
