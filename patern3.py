import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """ Реєстрація об'єкту """
        self._objects[name] = obj

    def unregister_object(self, name):
        """ Видалення об'єкту """
        del self._objects[name]

    def clone(self, name, **attrs):
        """ Клонування об'єкту """
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj

# Приклад використання:
class Car:
    def __init__(self):
        self.make = "Toyota"
        self.model = "Camry"
        self.year = 2022

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

car = Car()
prototype = Prototype()
prototype.register_object("car", car)

# Клонуємо об'єкт і змінюємо деякі властивості
car_clone = prototype.clone("car", year=2023)

print(car_clone)  # Виведе: Toyota Camry (2023)
