# Able to pass subclass objects in place of objects of super classes without breaking code
# Extending base behavior and not replacing with a completely different
import pdb
# Example 1 - Violating the contract
from abc import ABC, abstractmethod


class Product:
    def __init__(self, name, quantity, price_usd):
        self.name = name
        self.quantity = quantity
        self.price_usd = price_usd


class Order:
    def __init__(self):
        self.list_products = []
        self.status = 'unpaid'

    def add_item(self, product: Product):
        self.list_products.append(product)


class PayMethod(ABC):
    @abstractmethod
    def pay(self, order, ccv: int):
        pass


class DebitCardPayProcessor(PayMethod):
    def pay(self, order, ccv: int):
        assert isinstance(ccv, int), f'{ccv} is not a valid int type it is a(n) {type(ccv)}'
        print(f'Processing {ccv}')
        order.status = 'paid'
        print('Successful payment through Debit Card')


class CreditCardPayProcessor(PayMethod):
    def pay(self, order, ccv: int):
        assert isinstance(ccv, int), f'{ccv} is not a valid int type it is a(n) {type(ccv)}'
        print(f'Processing {ccv}')
        order.status = 'paid'
        print('Successful payment through Credit Card')


class PaypalPayProcessor(PayMethod):
    def pay(self, order, ccv: int):
        assert isinstance(ccv, str), f'{ccv} is not a valid string type it is a(n) {type(ccv)}'
        print(f'Processing {ccv}')
        order.status = 'paid'
        print('Successful payment through Paypal')


def process_order(order, pay_method: PayMethod, security_param):
    pay_method.pay(order, security_param)


# debit_processor = DebitCardPayProcessor()
# credit_processor = CreditCardPayProcessor()
# paypal_processor = PaypalPayProcessor()
#
# order_1, order_2, order_3 = Order(), Order(), Order()
# product_1 = Product('USB', 5, 25)
# order_1.add_item(product_1)
# product_2 = Product('USB', 5, 25)
# order_2.add_item(product_2)
# product_3 = Product('USB', 5, 25)
# order_3.add_item(product_3)
#
# process_order(order_1, debit_processor, 854)
# process_order(order_2, credit_processor, 845)
# process_order(order_3, paypal_processor, 123)

"""
    There's a violation of principle not using a subclass in a compatible way with it's
    parent class.
    Not following the Design By Contract with the abstract class.
"""


#
#   Example 2 - violating the contract
#   Ostrich violates the contract because they cannot fly
#

class Bird:
    def fly(self):
        print("Flying")


class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")


def make_bird_fly(bird: Bird):
    bird.fly()


# This will raise an error
# make_bird_fly(Ostrich())


#
#   Example 3 - altering the behavior defined by the parent class.
#   All vehicles must be able to start their engines,
#

class Vehicle:
    def start_engine(self):
        print("Engine started.")


class ElectricVehicle(Vehicle):
    def start_engine(self):
        print("Engine cannot be started for an electric vehicle.")


# electric_vehicle = ElectricVehicle()
# electric_vehicle.start_engine()
