class Student:
    school = "MIT"

    def __init__(self, name, gender):
        # _ protected 屬性
        self._name = name
        # __ private屬性
        self.__gender = gender

    # _ protected 方法
    def _say_hello(self, msg):
        print(f"Hello {msg}, {self._name}, {self.__gender}")

    # __ private 方法
    def __say_hello(self, msg):
        print(f"Hi {msg}, {self.__gender}")

    # 類方法
    @classmethod
    def hello(cls):
        print(f"Hello {cls.school}")

    @staticmethod
    def info():
        print("This is a Student class", Student.school)


s1 = Student("Jack", "Male")
Student.hello()
Student.info()
