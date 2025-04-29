# Defining the Car class
class Car:
    # Public variable
    brand = "Toyota"  
    
    # Public method
    def start(self):
        print("Car is starting...")  # This method will start the car

# Creating an object of the class
my_car = Car()

# Accessing the public variable from outside
print(my_car.brand)  

# Calling the public method from outside
my_car.start()  
