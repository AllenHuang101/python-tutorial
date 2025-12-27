print('請輸入學生成績，輸入"結束"停止錄入')
score_list = []

# 持續迴圈，讓使用者輸入學生成績
while True:
    data = input('📝請輸入成績：')
    if data == '結束':
        break
    else:
        score_list.append(int(data))

# 如果score_list中有資料，則開始統計
if score_list:
    # 統計平均分
    avg = sum(score_list) / len(score_list)
    # 合格人數
    pass_count = 0
    # 優秀人數
    excellent_count = 0
    # 遍歷列表，開始統計
    for item in score_list:
        if item >= 60:
            pass_count += 1
        if item >= 90:
            excellent_count += 1
    # 合格率
    pass_rate = pass_count / len(score_list) * 100
    # 優秀率
    excellent_rate = excellent_count / len(score_list) * 100
    # 列印資訊
    print('********⬇️統計資訊如下⬇️********')
    print(f'🧑‍🎓總人數為：{len(score_list)}')
    print(f'🔺最高分為：{max(score_list)}')
    print(f'🔻最低分為：{min(score_list)}')
    print(f'✅合格人數：{pass_count}人')
    print(f'📈合格率為：{pass_rate:.1f}%')
    print(f'🏆優秀人數：{excellent_count}人')
    print(f'📈優秀率為：{excellent_rate:.1f}%')
    print(f'📊平均分數：{avg:.1f}')
else:
    print('您沒有輸入任何成績！')