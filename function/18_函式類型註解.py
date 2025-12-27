# 函式型別註解：給函式的【參數】和【傳回值】添加型別說明。
# 語法格式：函式名(參數1: 型別, 參數2: 型別) -> 傳回值型別:。

# 範例1：設定參數型別註解、設定傳回值型別註解
# def add(x: int, y: int) -> int:
#     return x + y

# 範例2：參數有預設值(Python可以推導出參數的型別)、設定傳回值型別
# def add(x=1, y=1) -> int:
#     return x + y

# 範例3：設定多個傳回值的型別註解
# def show_nums_info(nums: list[int]) -> tuple[int, int, float]:
#     max_value = max(nums)
#     min_value = min(nums)
#     result = max_value / min_value
#     return max_value, min_value, result

# 範例4：設定 *args 的型別註解，要求 args 中的每個參數都必須是 int 型別
# def add(*args: int) -> int:
#     return sum(args)

# 範例5：設定 **kwargs 的型別註解，要求 kwargs 中的每組參數的值，必須是 str 或 int 型別
# def show_info(**kwargs: str | int):
#     print(kwargs)

# 取得函式的註解資訊
# print(add.__annotations__)

