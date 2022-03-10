# If i want to make a pipeline object in Python - A class that can act as a
# pipeline given a bunch of tasks like column manipulation, column
# transformation, model build etc - How to go about building it?
# For example - My aim is to chain a few commonly used data cleaning tasks
# together and make them run as a pipeline. The simple tasks all have code - I
# want you to design a pipeline class that takes these as inputs and executes
# them in order. Need an abstract base class that can furher be inherited from

from abc import ABC, abstractmethod

class PipeLine(ABC):
    @abstractmethod
    def dataImport(self):
        raise NotImplementedError("dataImport() not defined in subclass")

    @abstractmethod
    def dataExport(self):
        raise NotImplementedError("dataExport() not defined in subclass")

    def dataTransform(self):
        pass

    def featureEngineering(self):
        pass

class RandomForestClassification(PipeLine):
    def dataImport(self):
        print("Sub Class Method Data Import Called")

    def dataExport(self):
        print("Sub Class Method Data Export Called")

    # def dataTransform(self):
    #     return super().dataTransform()

    # def featureEngineering(self):
    #     return super().featureEngineering()



def main():
    # Create a RandomForestClassification object which follows the properties
    # defined by Abstract SuperClass PipeLine
    obj = RandomForestClassification()
    obj.dataImport()
    obj.dataExport()
    obj.dataTransform()
    obj.featureEngineering()

if __name__ == '__main__':
    main()
