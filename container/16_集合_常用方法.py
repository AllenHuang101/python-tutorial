# 集合A.difference(集合B)：
# 作用：找出集合A中，不同於集合B的元素（集合A 與 集合B 都不變，傳回的是一個新的集合）
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# result = s1.difference(s2)
# print(s1)
# print(s2)
# print(result)

# 集合A.difference_update(集合B)：
# 作用：從集合A中，刪除集合B中存在的元素（集合A會被修改，集合B不會）
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# s1.difference_update(s2)
# print(s1)
# print(s2)


# 集合A.union(集合B)：
# 作用：合併兩個集合，集合A 和 集合B 都不變，傳回的是一個新的集合
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# result = s2.union(s1)
# print(s1)
# print(s2)
# print(result)

# 集合A.issubset(集合B)：
# 作用：判斷集合A是否為集合B的子集
# 如果 集合A的所有元素都在集合B中，那就傳回True，否則傳回False
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# s3 = {30, 40, 50}
# result = s3.issubset(s1)
# print(result)

# 集合A.issuperset(集合B)：
# 作用：判斷集合A是否是集合B的超集
# 如果集合A中，包含了集合B中的所有元素，那就傳回True，否則傳回False
# s1 = {10, 20, 30, 40, 50}
# s2 = {30, 40, 50, 60, 70}
# s3 = {30, 40, 50}
# result = s1.issuperset(s3)
# print(result)

# 集合A.isdisjoint(集合B)：
# 作用：判斷集合A和集合B是否沒有交集
# 如果沒有交集，傳回True；只要有一個公共元素，就傳回False
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70}
s3 = {80, 90}
result = s1.isdisjoint(s2)
print(result)
