class Counter:
    # Class variable to track number of objects
    count = 0

    def __init__(self):
        # Each time an object is created, increment the count
        Counter.count += 1

    @classmethod
    def show_count(cls):
        # Use cls to access the class variable
        print(f"Total objects created: {cls.count}")

# Create some objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Call the class method to display the count
Counter.show_count()
