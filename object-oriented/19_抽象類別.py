from abc import ABC, abstractmethod


# 【抽象類別】是一種不能直接實例化的類別，它通常作為「規範」，讓子類別去繼承，並實現其中定義的【抽象方法】。
# MustRun類別一旦繼承了ABC類別，那麼MustRun類別就是抽象類別了
class MustRun(ABC):
    name: str

    # 抽象方法：沒有具體實現的方法
    @abstractmethod
    def run(self):
        pass

    def speak(self):
        print(f"你好，我叫{self.name}")


class Person(MustRun):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def run(self):
        print(f"我叫{self.name}，我在努力的奔跑")


p1 = Person("張三", 18, "男")
p1.run()
p1.speak()
