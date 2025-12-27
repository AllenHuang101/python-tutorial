# 練習一：水果清單
fruits = {
    '蘋果': 4.5,
    '香蕉': 3.2,
    '橙子': 5.8,
    '草莓': 12.0,
    '哈密瓜': 8.8
}

# 需求1：列印所有的水果
# for key in fruits:
#     print(f'{key}：{fruits[key]} 元/斤')

# 需求2：找到最貴水果
# key = max(fruits, key=fruits.get)
# print(f'最貴的水果是{key}，價格是{fruits[key]} 元/斤')

# --------------------------------------------------------------------

# 練習二：學生成績表
students = [
    {
        'name': '張三',
        'scores': {'語文': 88, '數學': 92, '英語': 95}
    },
    {
        'name': '李四',
        'scores': {'語文': 75, '數學': 83, '英語': 80}
    },
    {
        'name': '王五',
        'scores': {'語文': 92, '數學': 95, '英語': 88}
    }
]

# 需求1：計算每位學生的平均分
# for stu in students:
#     # 取得目前學生的成績列表
#     score_list = stu['scores'].values()
#     # 計算平均值
#     avg = sum(score_list) / len(score_list)
#     print(f'{stu['name']}的平均成績是：{avg:.1f}')


# 需求2：找到總分最高的學生
# def find_best():
#     # 記錄分數最高的學生
#     best_students = []
#     # 記錄最高分
#     best_score = 0
#     # 迴圈遍歷
#     for stu in students:
#         # 取得目前學生的總成績
#         total = sum(stu['scores'].values())
#         # 目前學生的成績，如果大於best_score，就會更新資料
#         if total > best_score:
#             best_students = [stu['name']]
#             best_score = total
#         # 目前學生的成績與最高分相同，就加入列表
#         elif total == best_score:
#             best_students.append(stu['name'])
#     print(f'最高分為{best_score}，取得最高分的學生有：{best_students}')
# find_best()

# --------------------------------------------------------------------

# 練習三：評論內容
comment = '這家奶茶真好喝，環境也不錯，就是價格有點貴，好喝好喝好喝！強烈推薦！'

# 需求1：統計"好喝"出現次數
print(comment.count('好喝'))

# 需求2：將字串中的"貴"替換為"略高"
comment2 = comment.replace('貴', '略高')
print(comment2)

# 需求3：是否包含"推薦"兩個字
print('推薦' in comment)