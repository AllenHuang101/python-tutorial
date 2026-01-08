from enum import Enum, auto
import enum
from functools import total_ordering
from colorama import Fore, init

init(autoreset=True)


class Gender(Enum):
    MALE = 1
    FEMAL = 2


class Student:
    def __init__(self):
        self.gender = Gender.MALE


gender = Gender.FEMAL

if gender == Gender.FEMAL:
    print("This is a female")
else:
    print("This is a male")


print(Fore.BLUE + "Gender.MALE", Gender.MALE.name, Gender.MALE.value)

# 拿到字符串的名字或整數值，就可以拿到對應的枚舉成員
# 把字串轉成 Enum 成員
print(Fore.BLUE + "===字串轉成 Enum 成員===")
s_gender = "FEMAL"
gender = Gender[s_gender]
print(gender)

# 把數字轉成 Enum 成員
print(Fore.BLUE + "===數字轉成 Enum 成員===")
gender = Gender(1)
print(gender)

# 遍歷枚舉成員
print(Fore.BLUE + "===遍歷枚舉成員===")

for g in Gender:
    print(g)

# 枚舉成員的別名
# 當枚舉中的多個成員具有相同 value 時，其中一個成員會被視為主成員，其他成員則被視為該主成員的別名。
print(Fore.BLUE + "===枚舉成員的別名===")


class Status(Enum):
    SUCCESS = 1
    OK = 1
    FAIL = 2
    WRONG = 2


for s in Status:
    print(s.name)

print(Status.__members__)
print(Status.SUCCESS == Status.OK)
print(Status.SUCCESS is Status.OK)

# 當我們需要保證枚舉中的成員必須具有唯一的值時，可以使用 @enum.unique 裝飾器來裝飾枚舉類別。

print(Fore.BLUE + "===使用 @enum.unique 裝飾器===")


@enum.unique
class Gender2(Enum):
    MALE = 1
    FEMAL = 2


class Status2(Enum):
    SUCCESS = 1
    FAIL = 2

    def __str__(self):
        return f"Status2.{self.name}({self.value})"

    def __eq__(self, other):
        # print(self, other)
        if isinstance(other, int):
            return self.value == other

        if isinstance(other, str):
            return self.name == other.upper()

        if isinstance(other, Status2):
            return self is other

        return False


print(Fore.BLUE + "===__str__===")
print(Status2.SUCCESS)


status2 = Status2.SUCCESS
status3 = Status2.SUCCESS


print(Fore.BLUE + "===__eq__===")
print(status2 == 1)
print(status2 == "SUCCESS")
print(status2 == status3)


@total_ordering
class WorkFlowStatus(Enum):
    OPEN = 1
    IN_PROGRESS = 2
    REVIEW = 3
    COMPLETE = 4

    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < other

        if isinstance(other, WorkFlowStatus):
            return self.value < other.value

        return False


print(Fore.BLUE + "===__lt__===")

print(WorkFlowStatus.OPEN < 2)


# 自動按照順序給枚舉成員復職值
print(Fore.BLUE + "===auto()===")


class Status3(Enum):
    SUCCESS = auto()
    FAIL = auto()
    PENDING = auto()


for s in Status3:
    print(s.name, s.value)
