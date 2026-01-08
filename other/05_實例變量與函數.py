class Student:
    def __init__(self, name):
        self.name = name

    def say_hello(self, msg):
        print(f"Hello {msg}, {self.name}")


s1 = Student("Jack")
s2 = Student("Mary")

s1.say_hello("hahaha")
s2.say_hello("xixixi")
