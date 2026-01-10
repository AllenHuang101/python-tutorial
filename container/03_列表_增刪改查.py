from colorama import Fore, init

init(autoreset=True)

# 新增操作
# 方式一：透過列表的append方法，在列表尾部追加一個元素
print(f"{Fore.GREEN} =====方式一：透過列表的append方法，在列表尾部追加一個元素=====")
nums = [10, 20, 30, 40]
nums.append(50)
print(nums)

# 方式二：透過列表的insert方法，在列表的指定下標處新增一個元素
print(
    f"{Fore.GREEN} =====方式二：透過列表的insert方法，在列表的指定下標處新增一個元素====="
)
nums = [10, 20, 30, 40]
nums.insert(2, 666)
print(nums)

# 方式三：透過列表的extend方法，將可迭代物件中的內容依次取出，追加到列表尾部
print(
    f"{Fore.GREEN} =====方式三：透過列表的extend方法，將可迭代物件中的內容依次取出，追加到列表尾部====="
)
nums = [10, 20, 30, 40]
nums.extend("尚硅谷")
nums.extend(range(1, 4))
nums.extend([70, 80, 90])
print(nums)

# 删除操作
# 方式一：透過列表的pop方法，刪除指定位置的元素，並返回該元素
print(
    f"{Fore.GREEN} =====方式一：透過列表的pop方法，刪除指定位置的元素，並返回該元素====="
)
nums = [10, 20, 10, 40, 50]
result = nums.pop(1)
print(nums)
print(result)

# 方式二：透過列表的remove方法，刪除列表中第一次出現的指定值
print(
    f"{Fore.GREEN} =====方式二：透過列表的remove方法，刪除列表中第一次出現的指定值====="
)
nums = [10, 20, 10, 40, 50]
nums.remove(10)
print(nums)

# 方式三：透過列表的clear方法，刪除列表中所有的元素（清空列表）
print(
    f"{Fore.GREEN} =====方式三：透過列表的clear方法，刪除列表中所有的元素（清空列表）====="
)
nums = [10, 20, 10, 40, 50]
nums.clear()
print(nums)

# 方式四：透過del關鍵字，刪除指定元素
print(f"{Fore.GREEN} =====方式四：透過del關鍵字，刪除指定元素=====")
nums = [10, 20, 10, 40, 50]
del nums[3]
print(nums)

# 修改操作
print(f"{Fore.GREEN} ======修改操作====")
nums = [10, 20, 10, 40, 50]
nums[2] = 66
print(nums)

# 查詢操作
print(f"{Fore.GREEN} ======查詢操作====")
nums = [10, 20, 10, 40, 50]
print(nums[3])
