class Animal:
    def eat(self):
        print("Animal eat mothod is called")


class Bird:
    def walk(self):
        print("Brid walk method is called")



class Duck(Animal,Bird):
    pass

duck=Duck()
duck.eat()
duck.walk()