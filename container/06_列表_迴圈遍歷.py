# 定義一個成績列表
score_list = [62, 50, 60, 48, 80, 20, 95]

# 使用while迴圈遍歷列表
index = 0
while index < len(score_list):
    print(score_list[index])
    index += 1

# 使用for迴圈遍歷列表
# for item in score_list:
#     print(item)

# 使用for迴圈遍歷列表（透過range函式 和 len函式按照索引遍歷）
# for index in range(len(score_list)):
#     print(score_list[index])

# 使用for迴圈遍歷列表（透過enumerate函式，同時取得下標（索引值）和元素）
# enumerate 的 start 參數，可以讓計數從指定值開始（改變的是迴圈時的"編號"，不是真正的索引值）
# for index, item in enumerate(score_list, start=5):
#     print(index, item, score_list[0])
# print('最後的列印', score_list[0])

