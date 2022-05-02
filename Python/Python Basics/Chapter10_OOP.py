class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound="Woof"):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound="Bark!"):
        return f"{self.name} says {sound}"


class rectangle:
    def __init__(self, side):
        self.side = side

    def area(self):
        return f"{self.side*self.side}"

marcus = GoldenRetriever("marucs",3)
Rec = rectangle(5)
print(f"\n{Rec.area()}\n")
print(marcus.speak())