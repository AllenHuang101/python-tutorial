# 異常的傳遞機制：
# 1.如果異常沒有被當前程式碼區塊所捕獲處理，那該異常就會沿著呼叫鏈，逐層傳遞給其呼叫者。
# 2.如果所有呼叫者，都沒有捕獲該異常，那最終程式將因【未處理異常】而意外終止。
def test1():
    print('******test1開始******')
    result = '100' + 100
    print('******test1結束******')

def test2():
    print('******test2開始******')
    try:
        test1()
    except Exception as e:
        print(f'程式異常：{e}')
    print('******test2結束******')

def test3():
    print('******test3開始******')
    test2()
    print('******test3結束******')

test3()
