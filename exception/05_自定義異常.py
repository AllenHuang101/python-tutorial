# 自訂異常類別：
# 1.由開發人員自己定義一個異常類別，用來表示程式碼中"更具體、更有業務含義"的異常。
# 2.具體規則：定義一個類別（類別名通常以 Error 結尾），繼承 Exception 類別或它的子類別。

class SchoolNameError(Exception):
    def __init__(self, msg):
        super().__init__('【校名異常】' + msg)

def check_school_name(name):
    if len(name) > 10:
        raise SchoolNameError('學校名過長')
    else:
        print('學校名是合法的')

try:
    check_school_name('atguiguuuuuuuuuuuuuuu')
except SchoolNameError as e:
    print(f'程式異常：{e}')



