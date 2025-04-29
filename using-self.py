class Student:
    # Constructor to initialize name and marks using self
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Method to display student details
    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Creating a student object
student1 = Student("Noushad", 85)

# Displaying student details
student1.display()
