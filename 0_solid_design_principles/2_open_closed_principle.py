"""
    To exemplify open closed principle we use Strategy pattern

    Open for extension: Able to add new functionality to class or module
    Closed for modification: Not change existing code to add new behavior.

    For this abstraction and polymorphism are used:

    Bad example:

    class DiscountCalculator:
        def calculate_discount(self, customer_type):
            if customer_type == 'a':
                return 0.1
            elif customer_type == 'b':
                return 0.2

    Why it's bad: if new customer_type ex. 'c' wants to be added
    the class will be modified.

    Reasons:
        - Scalability.
        - Maintainability.
        - Avoid breaking code when new features are implemented

"""
from abc import ABC, abstractmethod


class DiscountStrategy(A1BC):
    @abstractmethod
    def calculate_discount(self):
        pass


class NormalClient(DiscountStrategy):
    def calculate_discount(self):
        return 0.1


class PremiumClient(DiscountStrategy):
    def calculate_discount(self):
        return 0.2


class DiscountCalculator:
    @staticmethod
    def get_discount(strategy: DiscountStrategy):
        return strategy.calculate_discount()


premium_client = PremiumClient()
p_discount = DiscountCalculator.get_discount(premium_client)
print(f'Premium Client discount: {p_discount}')

normal_client = NormalClient()
n_discount = DiscountCalculator.get_discount(normal_client)
print(f'Normal Client discount: {n_discount}')

"""
    In previous example DiscountCalculator class is open to extension and closed
    to modification. 
    -> Open to extension: accepts objects from classes that are 
    derived from Discount Strategy.
    -> Closed to modification: no need to change if a new type of client is added
    
"""

# Example 2


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Triangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return self.base * self.height / 2


class AreaCalculator:

    def calculate_area_of_figure(self, figure: Figure) -> float:
        return figure.get_area()


area_calculator = AreaCalculator()
triangle = Triangle(4,5)
triangle_area = area_calculator.calculate_area_of_figure(triangle)
print(f'Area of triangle: {triangle_area}')

