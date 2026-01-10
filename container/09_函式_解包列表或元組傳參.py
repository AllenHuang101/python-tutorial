from colorama import Fore, init

init(autoreset=True)


# 定義函式時，使用*args（變數不一定非要用args，例如寫：*data也可以），將收到的多個參數，打包成一個元組
def test(*args):
    print(f"我是test函式，我收到的參數是：{args}，參數類型是：{type(args)}")


list1 = [100, 200, 300, 400]
tuple1 = ("你好", "北京", "尚矽谷")

# 函式呼叫時，正常傳遞：列表 或 元組
print(Fore.GREEN + "----- 正常傳遞列表或元組 -----")
test(list1)
test(tuple1)

# 函式呼叫時，使用*對：列表 或 元組進行解包後，再傳遞參數
print(Fore.GREEN + "----- 使用*解包列表或元組傳遞參數 -----")
test(*list1)  # 此種寫法相當於：test(100, 200, 300, 400)
test(*tuple1)  # 此種寫法相當於：test('你好', '北京', '尚矽谷')
