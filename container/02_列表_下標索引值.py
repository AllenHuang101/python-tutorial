from colorama import Fore, init

init(autoreset=True)

# 定義一個列表
nums = [10, 20, 30, 40, 50]

# 測試正索引
print(f"{Fore.GREEN} =====測試正索引=====")
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])

# 測試負索引
print(f"{Fore.GREEN} =====測試負索引=====")
print(nums[-1])
print(nums[-2])
print(nums[-3])
print(nums[-4])
print(nums[-5])

# 測試錯誤索引
print(f"{Fore.GREEN} =====測試錯誤索引=====")
# print(nums[5])

# 定義一個巢狀列表
nums2 = [10, 20, ["你好啊", "尚矽谷"], 40, 50]

print(f"{Fore.GREEN} =====測試巢狀列表=====")
print(nums2[2][1])
