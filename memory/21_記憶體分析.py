from colorama import Fore, init

init(autoreset=True)  

a = 666
print(Fore.BLUE + "a 的記憶體位置：", id(a))

b = a
print(Fore.BLUE + "b 的記憶體位置：", id(b))

print(Fore.RED + "a & b 都是 666")
print(a)
print(b)


# 不可變對象，對應記憶體分析-2.png
print(Fore.RED + "將 a 改成 888 後")
a = 888

print(Fore.BLUE + "a 的記憶體位置：", id(a),  Fore.BLUE + "a 的值：", a)
print(Fore.BLUE + "b 的記憶體位置：", id(b),  Fore.BLUE + "b 的值：", b)


print(Fore.BLUE + "可變對象")

stu_list = ['張三', '李四', '王五']
print(Fore.GREEN + "stu_list 的記憶體位置：", id(stu_list))
print(Fore.GREEN + "stu_list[0] 的記憶體位置：", id(stu_list[0]))
stu_list[0] = '阿三'
print(Fore.RED + "修改後 stu_list[0] 的值後")
print(Fore.GREEN + "stu_list 的記憶體位置：", id(stu_list))
print(Fore.GREEN + "stu_list[0] 的記憶體位置：", id(stu_list[0]))


