# 多型的概念：同一個方法名，在不同的物件上呼叫時，能呈現出不同的行為。
# Python中支援：標準多型、鴨子多型
class Animal:
    def speak(self):
        print('動物正在發出聲音！')

class Dog(Animal):
    def speak(self):
        print('汪汪汪！')

class Cat(Animal):
    def speak(self):
        print('喵喵喵！')

class Pig:
    def speak(self):
        print('哼哼哼！')

def make_sound(animal:Animal):  # 類型註解
    # 多型的體現
    animal.speak()

# 建立實例物件
a1 = Animal()
d1 = Dog()
c1 = Cat()
p1 = Pig()

make_sound(a1)
make_sound(d1)
make_sound(c1)

# 此行程式碼如果在其它語言中會報錯，Python不會報錯，不推薦這樣寫
make_sound(p1) 
