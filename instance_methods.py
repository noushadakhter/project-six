class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking")
        print(f"{self.breed} is woow")

if __name__ == "__main__":
    my_dog = Dog("Tomy", "German-Shepherd")
    my_dog.bark()        
        