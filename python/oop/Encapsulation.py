class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # Private attribute

    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
        else:
            print("Invalid marks!")

student1 = Student("Wilson", 85)

print("Name:", student1.name)
print("Marks:", student1.get_marks())

student1.set_marks(90)

print("Updated Marks:", student1.get_marks())