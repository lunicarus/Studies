class Dog:
    species = "DOG"
    
    def  __init__(self, name, age):
       self.name = name;
       self.age = age;
    
    def __str__(self):
        return f"{self.name} is {self.age} old." 
          
Buddy = Dog("Buddy", 24);
print(Buddy);