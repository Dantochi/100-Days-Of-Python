def add(*args):  # args is a tuple and it represents unlimited positional arguments
    for n in args:
        print(f"This is an array {n}")


add(3, 5, 6)


def calculate(**kwargs):  # Kwargs represents unlimited keyword arguments or optional keyword arguments
    for key, value in kwargs.items():
        print(key, value)


calculate(add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]


my_car = Car(make="Nissan", model="GTR")
print(my_car.model)
