from colorama import Fore, init

init(autoreset=True)

# 對列表進行切片
print(Fore.GREEN + "----- 列表切片操作 -----")
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list2 = list1[0:5:1]
print("1=>", list2)

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list2 = list1[1:8:2]
print("2=>", list2)
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list2 = list1[1:8:3]
print("3=>", list2)

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list2 = list1[::]
print("4=>", list2)
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list2 = list1[:999:]
print("5=>", list2)

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list2 = list1[3::]
print("6=>", list2)
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list2 = list1[:5:]
print("7=>", list2)

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list2 = list1[::4]
print("8=>", list2)
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list2 = list1[7:2:-1]
print("9=>", list2)

# 一個特殊情況：當同時省略起始索引和結束索引時，如果步長為負數，那Python會自動對調：起始位置和結束位置
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list2 = list1[::-1]
print("10=>", list2)

# 對元組進行切片
print(Fore.GREEN + "----- 元組切片操作 -----")
tuple1 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
tuple2 = tuple1[0:5:1]
print("1=>", tuple2)

# 對字串進行切片
print(Fore.GREEN + "----- 字串切片操作 -----")
msg1 = "welcome to atguigu"
msg2 = msg1[2:9:2]
print("1=>", msg2)
