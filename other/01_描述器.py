from colorama import Fore, init

init(autoreset=True)


# 描述器 descriptor
class RequiredString:
    def __init__(self, trim: bool):
        self.__property_name = None
        self.__trim = trim

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise Exception(f"{self.__property_name} must be a string")

        if self.__trim:
            value = value.strip()

        if len(value) == 0:
            raise Exception(f"{self.__property_name} cannot be empty")

        instance.__dict__[self.__property_name] = value

    def __get__(self, instance, owner):
        if self.__property_name in instance.__dict__:
            return instance.__dict__[self.__property_name]

    def __set_name__(self, owner, name):
        self.__property_name = name


class Student:
    first_name = RequiredString(trim=True)
    last_name = RequiredString(trim=False)


student1 = Student()
# 相當於 first_name.__set__(student, "John") 方法被調用
student1.first_name = " John "

student1.last_name = " Huang "

student2 = Student()
student2.first_name = " Jane "
student2.last_name = " Hsu "

print(Fore.GREEN + student1.first_name)
print(Fore.GREEN + student1.last_name)
print(Fore.GREEN + student2.first_name)
print(Fore.GREEN + student2.last_name)
