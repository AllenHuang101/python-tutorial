# 知識點1：能被 for 迴圈遍歷的物件，被稱為：可迭代物件 (iterable)
# region
# names = ["張三", "李四", "王五"]
# citys = ("北京", "上海", "深圳")
# msg = "hello"
# age = 10
#
#
# def test():
#     pass
#
#
# for item in age:
#     print(item)
# endregion


# 知識點2：可迭代物件 (iterable) 能呼叫到 __iter__ 方法。
# region
# names = ["張三", "李四", "王五"]
# citys = ("北京", "上海", "深圳")
# msg = "hello"
# age = 10


# def test():
#     pass


# names.__iter__()
# citys.__iter__()
# msg.__iter__()

# 判斷是否為可迭代對象
# print(hasattr(names, "__iter__"))
# print(hasattr(citys, "__iter__"))
# print(hasattr(msg, "__iter__"))
# print(hasattr(age, "__iter__"))
# print(hasattr(test, "__iter__"))
# endregion


# 知識點3：呼叫 __iter__ 方法會得到：迭代器 (iterator)
# 備註1：__iter__ 是一個魔法方法，當呼叫 iter 函式時，__iter__ 會自動被呼叫。
# 備註2：可迭代物件.__iter__() 等價於 iter(可迭代物件)。
# 備註3：如果 iter(obj) 能得到一個迭代器 (iterator)，那 obj 就是可迭代物件。
# region
# names = ["張三", "李四", "王五"]
# citys = ("北京", "上海", "深圳")
# msg = "hello"

# print(names.__iter__())
# print(citys.__iter__())
# print(msg.__iter__())

# print(iter(names))
# print(iter(citys))
# print(iter(msg))
# endregion


# 知識點4：迭代器 (iterator) 擁有 __next__ 方法，
# 每次呼叫都會依據目前的狀態，回傳下一個元素。
# 備註1：迭代器.__next__() 等價於 next(迭代器)。
# 備註2：當所有元素都被取出後，若繼續呼叫 __next__ 方法，
#         Python 會拋出 StopIteration 例外。
# region
# names = ["張三", "李四", "王五"]
# it = iter(names)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# endregion


# for 迴圈背後的工作邏輯
# region
names = ["張三", "李四", "王五"]

# 撰寫 for 迴圈遍歷 names 清單
# for item in names:
#     print(item)

# for 迴圈背後的邏輯
# 1️⃣ 呼叫【可迭代物件的 __iter__ 方法】取得一個迭代器 (iterator)
it = iter(names)
# 2️⃣ 開啟一個無限迴圈
while True:
    try:
        # 3️⃣ 呼叫 __next__ 方法，取得下一個元素
        item = next(it)
        print(item)
    except StopIteration:
        # 4️⃣ 捕捉 StopIteration 例外，然後結束迴圈
        break
# endregion


# 知識點5：迭代器 (iterator) 也擁有 __iter__ 方法，
# 且其回傳值是迭代器本身。
# 這樣設計的原因如下：
# 讓 for 迴圈也能遍歷迭代器
# （也就是：為了讓 iter(迭代器) 不會出錯）。
# region
# names = ['張三', '李四', '王五']
#
# it = iter(names)
# print(it)
#
# result = iter(it)
# print(result)
#
# x = iter(result)
# print(x)
#
# it = iter(names)
# for item in it:
#     print(item)
# endregion


# 知識點6：迭代器協議
#   1. 能被 iter() 接受
#   2. 能被 next() 一步一步取值
# 遵循迭代器協議的物件，可以被 for 迴圈遍歷。
