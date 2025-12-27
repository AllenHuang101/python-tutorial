# 1️⃣為什麼要進行異常處理？
# 程式執行過程中出現的異常，如果得不到處理，那程式就會立即崩潰，導致後續程式碼無法執行。
# 異常處理不是讓異常消失，而是將異常捕獲到，隨後根據異常的具體情況，來執行指定的邏輯。
# print('歡迎使用本程式')
# a = int(input('請輸入第一個數：'))
# b = int(input('請輸入第二個數：'))
# result = a / b
# print(f'{a}除以{b}的結果是：{result}')
# print('*******我是後續的其它邏輯1*******')
# print('*******我是後續的其它邏輯2*******')


# 2️⃣異常處理（初級）：
# 1.將可能出現異常的程式碼放在 try 中，出現異常後的處理程式碼寫在 except 中。
# 2.如果 try 中的程式碼出現異常，那 try 中的後續程式碼將不會執行，並自動跳轉到 except 中處理異常。
# 3.如果 try 中的程式碼沒有異常，那 except 中的程式碼就不會執行。
# 4.無論是否發生異常，try-except 後面的程式碼都會繼續執行。
# 5.直接寫 except 會捕獲到 Python 中所有的異常 ———— 實際開發中不推薦這樣做。
# print('歡迎使用本程式')
# try:
#     a = int(input('請輸入第一個數：'))
#     b = int(input('請輸入第二個數：'))
#     result = a / b
#     print(f'{a}除以{b}的結果是：{result}')
# except:
#     # except 太 general，後面不指定異常類別，表示捕獲所有類型的異常
#     print('抱歉，程式出現了異常！')

# print('*******我是後續的其它邏輯1*******')
# print('*******我是後續的其它邏輯2*******')


# 3️⃣異常處理（捕獲指定的類型的異常）
# print('歡迎使用本程式')
# try:
#     a = int(input('請輸入第一個數：'))
#     b = int(input('請輸入第二個數：'))
#     result = a / b
#     print(f'{a}除以{b}的結果是：{result}')
# except ZeroDivisionError:
#     print('程式異常：0不能作為除數！')
# except ValueError:
#     print('程式異常：您輸入的必須是數字！')
# print('*******我是後續的其它邏輯1*******')
# print('*******我是後續的其它邏輯2*******')


# 4️⃣驗證一下異常類別之間的繼承關係
# https://docs.python.org/3.14/library/exceptions.html

# print(issubclass(ZeroDivisionError, ArithmeticError))
# print(issubclass(ZeroDivisionError, Exception))
# print(issubclass(ValueError, Exception))
# print(issubclass(KeyboardInterrupt, Exception))
# print(issubclass(KeyboardInterrupt, BaseException))


# 5️⃣多個 except 從上往下匹配，匹配成功後不再向下匹配。
# print('歡迎使用本程式')
# try:
#     a = int(input('請輸入第一個數：'))
#     b = int(input('請輸入第二個數：'))
#     print(x)
#     result = a / b
#     print(f'{a}除以{b}的結果是：{result}')
# except ZeroDivisionError:
#     print('程式異常：0不能作為除數！')
# except ValueError:
#     print('程式異常：您輸入的必須是數字！')
# except Exception:
#     print('程式異常!')
# print('*******我是後續的其它邏輯1*******')
# print('*******我是後續的其它邏輯2*******')


# 6️⃣獲取異常的具體資訊
# print('歡迎使用本程式')
# try:
#     a = int(input('請輸入第一個數：'))
#     b = int(input('請輸入第二個數：'))
#     print(x)
#     result = a / b
#     print(f'{a}除以{b}的結果是：{result}')
# except ZeroDivisionError:
#     print('程式異常：0不能作為除數！')
# except ValueError:
#     print('程式異常：您輸入的必須是數字！')
# except Exception as e: # 異常的具體訊息都保存在 e 這個異常物件中
#     # 拋出 Exception 是 NameError 的父類別，所以這裡可以捕獲到 NameError
#     # print(f'⚠程式異常，異常資訊：{e}')
#     # print(f'⚠程式異常，異常類型：{type(e)}')
#     # print(f'⚠程式異常，異常參數：{e.args}')
#     # print(f'⚠程式異常，異常的檔案：{e.__traceback__.tb_frame.f_code.co_filename}')
#     # print(f'⚠程式異常，異常的具體行數：{e.__traceback__.tb_lineno}')
#     # 透過 traceback 來回溯異常(推薦做法)
#     import traceback
#     print(traceback.format_exc())
    
# print('*******我是後續的其它邏輯1*******')
# print('*******我是後續的其它邏輯2*******')


# 7️⃣一個 except，也可以捕獲不同的異常
# print('歡迎使用本程式')
# try:
#     a = int(input('請輸入第一個數：'))
#     b = int(input('請輸入第二個數：'))
#     print(x)
#     result = a / b
#     print(f'{a}除以{b}的結果是：{result}')
# except (ZeroDivisionError, ValueError, Exception) as e:
#     if isinstance(e, ZeroDivisionError):
#         print('程式異常：0不能作為除數！')
#     elif isinstance(e, ValueError):
#         print('程式異常：您輸入的必須是數字！')
#     else:
#         print(f'程式異常：{e}')
# print('*******我是後續的其它邏輯1*******')
# print('*******我是後續的其它邏輯2*******')


# 8️⃣異常處理的完整寫法：
#   1.try：    嘗試去做可能會出現異常的事情
#   2.except： 出現異常時的處理（出現異常時怎麼補救）
#   3.else：   如果一切順利（沒有異常出現）要做的事
#   4.finally：無論有沒有異常，都要做的事
print('歡迎使用本程式')
try:
    a = int(input('請輸入第一個數：'))
    b = int(input('請輸入第二個數：'))
    result = a / b
    print(f'{a}除以{b}的結果是：{result}')
except (ZeroDivisionError, ValueError, Exception) as e:
    if isinstance(e, ZeroDivisionError):
        print('程式異常：0不能作為除數！')
    elif isinstance(e, ValueError):
        print('程式異常：您輸入的必須是數字！')
    else:
        print(f'程式異常：{e}')
else:
    print('挺好的，try中的程式碼沒有任何異常！')
finally:
    print('無論有沒有異常，我的計算都結束了！')
print('*******我是後續的其它邏輯1*******')
print('*******我是後續的其它邏輯2*******')

