from colorama import Fore, init

init(autoreset=True) 


# Python 中，所有的類別都繼承了 object 類別，即：object 類別是所有類別的父類別。
# 因為 object 是所有類別的父類別，所以 Python 中的所有物件，都間接是 object 類別的實例。

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# 驗證一下：所有的類別繼承了object類別
print(Fore.YELLOW + "驗證1", issubclass(Person, object))
print(Fore.YELLOW + "驗證1",issubclass(int, object))
print(Fore.YELLOW + "驗證1",issubclass(str, object))
print(Fore.YELLOW + "驗證1",issubclass(list, object))
print(Fore.YELLOW + "驗證1",issubclass(bool, object))
print(Fore.YELLOW + "驗證1",issubclass(tuple, object))

# 因為 object 是所有類別的父類別，所以 Python 中的所有物件，都間接是 object 類別的實例。
p1 = Person('張三', 18, '男')
print(Fore.BLUE + "驗證2", isinstance(p1, object))
print(Fore.BLUE + "驗證2", isinstance(100, object))
print(Fore.BLUE + "驗證2", isinstance('hello', object))
print(Fore.BLUE + "驗證2", isinstance(True, object))
print(Fore.BLUE + "驗證2", isinstance(None, object))
print(Fore.BLUE + "驗證2", isinstance([10, 20, 30], object))
print(Fore.BLUE + "驗證2", isinstance({'吃飯','睡覺'}, object))

# 所有物件都繼承了object類別所提供的：各種屬性和方法，從而保證了每個物件都具備統一的基本能力
for key in object.__dict__:
    print(key)

p1 = Person('張三', 18, '男')
# 物件身上自己的東西
print(Fore.YELLOW + "對象所有可以訪問到的東西", p1.__dict__)  
# 物件可以存取到的東西（自己的、繼承過來的）
print(Fore.RED + "對象所有可以訪問到的東西", dir(p1))


