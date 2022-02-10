class Cat:

    nbChats = 0

    def __init__(self, nom, age):
        self.name = nom
        self.age = age
        Cat.nbChats +=1

    def info(self):
        print(f"My name is {self.name} and I am {self.age} old.")

    def Talk(self):
        return "Miaou"
    @staticmethod
    def add5(x):
        return x+5

print(Cat.Talk())
