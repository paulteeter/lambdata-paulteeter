from pdb import set_trace as breakpoint


class Dog():
    def __init__(self, name, age, breed, housebroke=True):
        self.name = name
        self.age = age
        self.housebroke = housebroke
        self.breed = breed

    def bark(self):
        


if __name__ == '__main__':
    
    lucky = Dog("Lucky", 3, "Labrador")
    breakpoint()