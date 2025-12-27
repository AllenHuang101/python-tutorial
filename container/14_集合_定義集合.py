# 定義有內容的【可變集合】
# s1 = {10, 20, 20, 30, 40, 40, 50, 60, 60, 70, 80, 90, 100}
# s2 = {'你好', 'hello', '你好', 'atguigu', '北京'}
# s3 = {10, '你好', True, 1, 12.4}
# print(type(s1), s1)
# print(type(s2), s2)
# print(type(s3), s3)

# 定義有內容的【不可變集合】
# s1 = frozenset({10, 20, 20, 30, 40, 40, 50, 60, 60, 70, 80, 90, 100})
# s2 = frozenset({'你好', 'hello', '你好', 'atguigu', '北京'})
# s3 = frozenset({10, '你好', True, 1, 12.4})
# print(type(s1), s1)
# print(type(s2), s2)
# print(type(s3), s3)

# frozenset 接收的參數，可以是任意可迭代物件，但最終傳回的一定是【不可變集合】
# s1 = frozenset([10, 20, 30, 40, 50])
# s2 = frozenset((10, 20, 30, 40, 50))
# s3 = frozenset('hello')
# print(type(s1), s1)
# print(type(s2), s2)
# print(type(s3), s3)

# 定義空集合（可變集合）
# s1 = set()
# print(type(s1), s1)

# 不能直接寫{}來定義空集合，因為直接寫{}定義的是：空字典
# s2 = {}
# print(type(s2), s2)

# 定義空集合（不可變集合）
# s3 = frozenset()
# print(type(s3), s3)

# 集合中不能巢狀【可變集合】，但可以巢狀【不可變集合】
# 通俗理解：只有"不可變"的東西，才能安全的放進集合裡
s1 = {10, 20, 30, 40, 50}
s2 = frozenset({100, 200, 300, 400, 500})
l1 = [666, 777, 888]
t1 = ('hello', 'atguigu', '北京')

# s3 = {11, 22, 33, s1}  # 報錯
# s3 = {11, 22, 33, s2}  # 沒問題
# s3 = {11, 22, 33, l1}  # 報錯
s3 = {11, 22, 33, t1}  # 沒問題
print(s3)