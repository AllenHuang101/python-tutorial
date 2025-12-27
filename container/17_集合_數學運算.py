s1 = {10, 20, 30, 40, 50, 60}
s2 = {40, 50, 60, 70, 80, 90}

# 並集
result = s1 | s2
print(result)

# 交集
result = s1 & s2
print(result)

# 差集
result = s1 - s2
print(result)

# 對稱差集
result = s1 ^ s2
print(result)