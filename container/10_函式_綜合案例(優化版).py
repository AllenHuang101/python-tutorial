def calc_total(*nums):
    """
    計算總運動量（個）
    :param nums: 每一天的運動量（可變參數）
    :return: 總運動量（個）
    """
    return sum(nums)

def calc_avg(total, days=7):
    """
    計算平均值
    :param total: 總運動量（個）
    :param days: 天數（預設值是7）
    :return: 平均值
    """
    return total / days

def check_success(total, goal=120):
    """
    判斷本次挑戰是否成功
    :param total: 總運動量
    :param goal: 成功數量（預設值為120）
    :return: 成功或失敗的具體資訊
    """
    if total >= goal:
        return '✅恭喜！挑戰成功！'
    else:
        return '❌抱歉！挑戰失敗！'

def main(title, duration, goal):
    """
    主函式，用於開始一場挑戰賽
    :param title: 比賽標題
    :param duration: 比賽持續天數
    :param goal: 目標運動量
    :return: None
    """
    print(f'【{title}】【{duration}天】✊️挑戰賽（請輸入每天的數量）')
    # 定義一個nums列表，用於儲存每天的健身資料
    nums = []
    # 根據duration的值，迴圈讓使用者輸入
    for index in range(duration):
        nums.append(int(input(f'請輸入第{index + 1}天的資料：')))
    # 計算總數
    total = calc_total(*nums)
    # 計算平均值
    avg = calc_avg(total, duration)
    # 判斷挑戰是否成功
    result = check_success(total, goal)
    # 列印相關資訊
    print(f'【{title}】【{duration}天】健身總結')
    print(f'總數：{total}，平均值：{avg:.1f}')
    print(result)

main('伏地挺身', 6, 40)