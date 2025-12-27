# 核心理念：如果一個東西看起來像鴨子，叫起來也像鴨子，那它就是鴨子。
# 鴨子類型是一種程式設計風格，它不檢查物件的類型，只關注物件能否「做某件事」（是否有對應的方法）。

# 鴨子多型
class Dog:
    def speak(self):
        print('汪汪汪！')

class Cat:
    def speak(self):
        print('喵喵喵！')

class Pig:
    def speak(self):
        print('哼哼哼！')

class Fish:
    def speak(self):
        print('咕嚕嚕！')

class Computer:
    def speak(self):
        print('滋滋滋！')

def make_sound(animal):
    # 有 speak 方法就調用，沒有會報錯
    animal.speak()

# 建立實例物件
d1 = Dog()
c1 = Cat()
p1 = Pig()
f1 = Fish()
cm1 = Computer()


make_sound(d1)
make_sound(c1)
make_sound(p1)
make_sound(f1)
make_sound(cm1)
