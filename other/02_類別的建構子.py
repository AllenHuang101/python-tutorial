class Student:
    def __new__(cls, firstName, lastName):
        print("1. Creating a new student instance")
        instance = super().__new__(cls)
        return instance

    def __init__(self, firstName, lastName):
        print("2. Initializing the student instance")
        self.firstName = firstName
        self.lastName = lastName


s1 = Student("Allen", "Huang")
print(s1.firstName)
print(s1.lastName)
