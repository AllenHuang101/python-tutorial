# 1.使用 index 方法，尋找指定元素在列表中第一次出現的下標，傳回值是：元素下標。
# fruits = ['香蕉', '蘋果', '橙子', '香蕉']
# result = fruits.index('香蕉')
# print(result)

# 2.使用 count 方法，統計某個元素在列表中出現的次數，傳回值是：元素出現的次數。
# nums = [10, 20, 10, 30, 10, 40, [10, 10, 10]]
# result = nums.count(10)
# print(result)

# 3.使用 reverse 方法，對列表進行反轉（會改變原列表）。
# nums = [23, 11, 32, 30, 17, [6, 7, 8, 9]]
# nums.reverse()
# print(nums)

# 4.使用 sort 方法，對列表排序（預設從小到大），若想從大到小，可以將 reverse 參數設為True。
# 4.1 若列表中的元素：都是數字，則按照數字的大小順序進行排序。
# nums = [23, 11, 32, 30, 17]
# nums.sort(reverse=True)
# print(nums)

# 4.2 若列表中的元素：既有數字，又有字串，那就會報錯。
# nums = [23, 11, 32, 30, 17, '尚矽谷']
# nums.sort()
# print(nums)

# 4.3 若列表中的元素：都是字串，則按照字串的 Unicode 編碼大小進行排序
# msg_list = ['北京', '北硅谷', '北好']
# msg_list.sort()
# print(msg_list)
# print(ord('京'), ord('好'), ord('硅'))

# 備註：所有的列表方法，都只作用於"目前層"的元素（淺層操作），不會自動進入巢狀的"裡層"結構中。