# If i want to make a pipeline object in Python - A class that can act as a pipeline given a bunch of tasks like column manipulation, column transformation, model build etc - How to go about building it

# For example - My aim is to chain a few commonly used data cleaning tasks together and make them run as a pipeline. The simple tasks all have code - I want you to design a pipeline class that takes these as inputs and executes them in order. Need an abstract base class that can furher be inherited from

from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def methodOne(self):
        print("Base methodOne Called")

    # @abstractmethod
    def methodTwo(self):
        print("Base methodTwo Called")

class Son(Parent):
    def methodOne(self):
        print("Child methodOne Called")

    # def methodTwo(self):
    #     return super().methodTwo()

def main():
    # obj = Parent()
    obj = Son()
    obj.methodOne()
    obj.methodTwo()

if __name__ == '__main__':
    main()