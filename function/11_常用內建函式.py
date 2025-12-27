# 一、输入与输出
# print() ===> 输出指定内容
# 完整参数：print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# 参数详解：
#   1.objects：要输出的内容
#   2.sep：分隔符
#   3.end：结束符
#   4.file：输出位置
#   5.flush：是否立即刷新

# f = open('a.txt', 'w', encoding='utf-8')
# print(10, 20, 30, 40, sep='-', end='!', file=f)

import time
# 第一種進度條
# print('加载中', end='')
# for index in range(5):
#     print('.', end='', flush=True)
#     time.sleep(1)
# print('完成！', end='')

# 第二種進度條
# for index in range(1, 101):
#     print(f'\r已載入{index}%', end='', flush=True)
#     time.sleep(0.1)


# input() ===> 獲取使用者輸入

# 二、類型轉換
# int() ======> 轉為整數
# float() ====> 轉為浮點數
# str() ======> 轉為字串
# bool() =====> 轉為布林值
# list() =====> 轉為列表
# tuple() ====> 轉為元組
# set() ======> 轉為集合
# dict() =====> 轉為字典

# 三、數學相關
# abs() =========> 取絕對值
# print(abs(-9))
# print(abs(-2.5))
# print(abs(3 - 5))


# round() =======> 四舍五入
# 注意：round函数的四舍五入，是银行家舍入法：小于5就舍，大于5就入，等于5看奇偶（奇入偶舍）
# print(round(3.4))
# print(round(4.6))
# print(round(6.5))
# print(round(7.5))
# print(round(7.543, 2))

# pow()	=========> 次方
# print(pow(2, 3))    # 2的3次方
# print(pow(2, -1))   # 2的-1次方
# print(pow(2, 0.5))  # 2的開平方
# print(pow(2, 3, 5)) # 2的3次方對5取模


# divmod() ======> 商和餘數
# print(divmod(10, 3))


# max()	=========> 最大值（支援 key 函式）
# min()	=========> 最小值（支援 key 函式）
# sum()	=========> 求和
# map()	=========> 加工一組資料
# filter() ======> 按條件過濾資料（支援 key 函式）
# reduce() ======> 合併計算（需導入 functools）
# sorted() ======> 排序（支援 key 函式）

# 四、資料容器相關
# len()	==========> 獲取容器中元素的個數
# range() ========> 生成一個數字序列（可用於迴圈）
# for index in range(0, 10, 2):
#     print(index)

# enumerate() ====> 給序列添加索引
# zip()	==========> 將多個序列一一配對
# names = ('张三', '李四', '王五')
# scores = [60, 70, 80]
# result = zip(names, scores)
# for item in result:
#     print(item)

# 五、類型判斷與物件相關
# type() ==========> 查看類型
# isinstance() ====> 判斷類型
# issubclass() ====> 判斷兩個類別的繼承關係
# id() ============> 查看物件的記憶體位址

# 六、邏輯判斷相關
# all() ====> 全為真返回True
# l1 = [10, '尚硅谷', {1, 2, 3}, -9]
# print(all(l1))

# any() ====> 有一個為真即可
# l2 = [0, '', None, False, 10]
# print(any(l2))

# 七、字串輔助相關
# ord() ====>  獲取字元的 Unicode 編碼值
# chr() ====>  將 Unicode 編碼值轉為字元
