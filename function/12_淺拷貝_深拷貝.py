import copy
from colorama import Fore, init

init(autoreset=True)


# 直接賦值：兩個變數指向同一個物件，修改其中一個，就會影響另一個（互相影響）。
print(Fore.YELLOW + "直接賦值")
nums1 = [10, 20, 30, 40]
nums2 = nums1
nums2[3] = 99
print(id(nums1), id(nums2))
print(nums1[3], nums2[3])

# 淺拷貝：建立一個新的外層容器，但內部元素仍然引用原來的物件
print(Fore.YELLOW + "淺拷貝")
nums1 = [10, 20, 30, 40]
nums2 = copy.copy(nums1)
nums2[3] = 99
print(id(nums1), id(nums2))
print(nums1[3], nums2[3])

# 淺拷貝存在的問題：嵌套資料仍然是共享的，修改嵌套資料會互相影響
print(Fore.YELLOW + "淺拷貝存在的問題")
nums1 = [10, 20, 30, [40, 50]]
nums2 = copy.copy(nums1)
nums2[3][0] = 99
print(id(nums1), id(nums2))
print(id(nums1[3]), id(nums2[3]))
print(nums1[3][0], nums2[3][0])

print(Fore.YELLOW + "深拷貝")
# 深拷貝：建立一個新的外層容器，並對其內部所有的【可變子物件】進行遞迴複製
# 備註：
#   1. 深拷貝可以徹底消除資料之間的相互影響。
#   2. 深拷貝遇到【不可變物件】不會複製，會直接引用。
nums1 = [10, 20, 30, [40, 50]]
nums2 = copy.deepcopy(nums1)
nums2[3][0] = 99
print(id(nums1), id(nums2))
print(id(nums1[3]), id(nums2[3]))
print(nums1[3][0], nums2[3][0])

print(Fore.YELLOW + "注意點")
# 注意點：
#   1. 深拷貝只複製可變物件，不可變物件會直接引用。
a = 666
b = copy.deepcopy(a)
print(id(a), id(b))

#   2. 元組中如果只包含不可變物件，則深拷貝沒有效果。
nums1 = (10, 20, 30, (40, 50))
nums2 = copy.deepcopy(nums1)

print(id(nums1), id(nums2))
