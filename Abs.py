# practice of abstract class & abstract method

from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, BL, BW):
        self.BL = BL
        self.BW = BW

    def make_sound(self, sound):
        self.sound = sound

    def __repr__(self):
        return f"<Dog {self.BL} cm, {self.BW} kg, {self.sound}>"

a1 = Dog(100, 10)
a1.make_sound("bark")
print(repr(a1))
