from colorama import Fore, init

init(autoreset=True)

# 1.使用內建的 sorted 函式，傳回一個排序後的新容器（不改變原容器，預設順序：從小到大）
# 1.1 若列容器中的元素：都是數字，則按照數字的大小順序進行排序。
print(
    f"{Fore.GREEN} =====1.1 若列容器中的元素：都是數字，則按照數字的大小順序進行排序。====="
)
nums = [23, 11, 32, 30, 17]
result = sorted(nums, reverse=True)
print(nums)
print(result)

# 1.2 若列容器中的元素：既有數字，又有字串，那就會報錯。
print(f"{Fore.GREEN} =====1.2 若列容器中的元素：既有數字，又有字串，那就會報錯。=====")
# nums = [23, 11, 32, 30, 17, "尚矽谷"]
# sorted(nums)

# 1.3 若列容器中的元素：都是字串，則按照字串的 Unicode 編碼大小進行排序。
print(
    f"{Fore.GREEN} =====1.3 若列容器中的元素：都是字串，則按照字串的 Unicode 編碼大小進行排序。====="
)
msg_list = ["北京", "尚矽谷", "你好"]
result = sorted(msg_list)
print(msg_list)
print(result)

# 2.使用內建的 len 函式，取得容器中元素的總數量，傳回值是：元素總數量。
print(
    f"{Fore.GREEN} =====2. 使用內建的 len 函式，取得容器中元素的總數量，傳回值是：元素總數量。====="
)
nums = [10, 20, 10, 30, 10, 40, [50, 60, 70]]
result = len(nums)
print(result)


# 3.使用內建的 max 函式，取得容器中的最大值，傳回值是：最大值。
# 3.1 如果容器中的元素：都是數字，那 max 傳回的是最大的數。
print(
    f"{Fore.GREEN} =====3.1 如果容器中的元素：都是數字，那 max 傳回的是最大的數。====="
)
nums = [23, 11, 32, 30, 17]
result = max(nums)
print(nums)
print(result)

# 3.2 如果容器中的元素：既有數字又有字串，那 max 會報錯。
print(f"{Fore.GREEN} =====3.2 如果容器中的元素：既有數字又有字串，那 max 會報錯。====")
# nums = [23, 11, 32, 30, 17, "尚矽谷"]
# max(nums)

# 3.3 如果容器中的元素：都是字串，那 max 會傳回：Unicode 編碼最大的字元。
print(
    f"{Fore.GREEN} =====3.3 如果容器中的元素：都是字串，那 max 會傳回：Unicode 編碼最大的字元。===="
)
msg_list = ["北京", "尚矽谷", "你好"]
result = max(msg_list)
print(msg_list)
print(result)

# 3.4 max 函式也可以接收多個值，並篩選出最大值
print(f"{Fore.GREEN} =====3.4 max 函式也可以接收多個值，並篩選出最大值。====")
result = max(33, 45, 12, 78, 99)
print(result)

# 4.使用內建的 min 函式，取得容器中的最小值，傳回值是：最小值。
print(
    f"{Fore.GREEN} =====4. 使用內建的 min 函式，取得容器中的最小值，傳回值是：最小值。===="
)
# 備註：min 函式的使用方式與注意點與 max 函式一樣，只不過 min 函式傳回的是最小值
nums = [23, 11, 32, 30, 17]
result = min(nums)
print(result)

# 5.使用內建的 sum 函式，對容器中的資料進行求和（元素只能是數值）。
print(
    f"{Fore.GREEN} =====5. 使用內建的 sum 函式，對容器中的資料進行求和（元素只能是數值）。===="
)
nums = [10, 20, 30, 40, 50]
result = sum(nums)
print(result)
