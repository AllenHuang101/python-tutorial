from colorama import Fore, init

init(autoreset=True)

# 查詢
print(Fore.GREEN + "=====查詢=====")
d1 = {"張三": 72, "李四": 60, "王五": 85}
# 直接取值，若鍵（key）不存在，會報錯
result1 = d1["張三"]
# 安全取值，若鍵（key）不存在，會傳回預設值（若沒有設定預設值，則會傳回None）
result2 = d1.get("奥特曼", "抱歉，key不存在！")
print(result1, result2)

# 新增
print(Fore.GREEN + "=====新增=====")
d1 = {"張三": 72, "李四": 60, "王五": 85}
d1["趙六"] = 100
print(d1)

# 修改
print(Fore.GREEN + "=====修改=====")
d1 = {"張三": 72, "李四": 60, "王五": 85}
# 修改的寫法，與新增的寫法一樣，若字典中有對應的key，就是修改；若沒有，就是新增
d1["張三"] = 97
print(d1)
# 批量修改
d1.update({"李四": 40, "王五": 67})
print(d1)

# 刪除
print(Fore.GREEN + "=====刪除=====")
d1 = {"張三": 72, "李四": 60, "王五": 85}

# 刪除指定key所對應的那組鍵值對
del d1["張三"]
print(d1)

# 刪除指定key所對應的那組鍵值對，並傳回這個key所對應的值
result = d1.pop("李四")
print(d1)
print(result)

print(Fore.GREEN + "==========")
# pop方法可以設定預設值
# 預設值可以保證：當要刪除的key不存在的情況下，程式不會報錯，並且傳回這個預設值
result = d1.pop("奧特曼", "刪除失敗！")
print(d1)
print(result)

# 清空字典
d1.clear()
print(d1)
