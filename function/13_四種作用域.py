a = 100

def test(b):
    print('我是test函式')
    print('test中列印的a是', a)
    print('test收到的參數b是', b)
    c = 200
    d = 300
    print('test中的c和d是', c, d)
    def inner():
        e = 400
        nonlocal c
        c = 999
        print('inner中的e是', e)
        print('inner中列印的c是', c)
        print('########', a)
    inner()
    print('***************', c)

print('全局列印的a是', a)
test(66)