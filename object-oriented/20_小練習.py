from datetime import datetime

# 定義Person類別
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    # 計數器
    count = 0

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        Student.count += 1
        # 給每個學生新增stu_id屬性，格式為：年份-序號，序號靠計數器增長。
        self.stu_id = f'{datetime.now().year}{Student.count:03d}'
        # 給學生新增成績，格式為： {'數學':90, '語文':80, '英語':70}
        self.scores = {}

    # 給當前學生新增成績
    def add_score(self, subject, score):
        # 給指定學生新增成績，subject是學科，score是成績
        self.scores[subject] = score

    # 計算平均分
    def calcu_avg(self):
        if self.scores:
            # 計算平均成績
            return sum(self.scores.values()) / len(self.scores)
        else:
            return 0

    # 魔法方法
    def __str__(self):
        return f'{self.name}({self.age}-{self.gender})，成績：{self.scores}，平均分:{self.calcu_avg():.1f}'

class Manager:
    def __init__(self):
        self.stu_list = []

    # 新增學生
    def add_student(self):
        name = input('請輸入姓名：')
        age = int(input('請輸入年齡：'))
        gender = input('請輸入性別：')
        # 建立學生實例物件
        stu = Student(name, age, gender)
        # 將當前學生新增到stu_list列表中
        self.stu_list.append(stu)
        print(f'新增成功！學號是：{stu.stu_id}')

    # 刪除學生
    def del_student(self):
        sid = input('請輸入學號：')
        # target用於儲存要刪除的學生
        target = None
        # 遍歷所有學生，找到要刪除的學生，並交給target變數
        for stu in self.stu_list:
            if stu.stu_id == sid:
                target = stu
        # 如果找到了要刪除的學生，就呼叫remove方法移除該學生
        if target:
            self.stu_list.remove(target)
            print('刪除成功！')
        # 如果未找到要刪除的學生
        else:
            print('學號有誤，刪除失敗！')

    # 展示所有學生
    def show_all_student(self):
        # 如果當前stu_list中有學生，就遍歷展示
        if self.stu_list:
            for stu in self.stu_list:
                print(stu)
        # 如果當前stu_list中沒有學生，就列印：暫無學生！
        else:
            print('暫無學生！')

    # 給指定學生設定成績
    def set_score(self):
        sid = input('請輸入學號：')
        # 遍歷stu_list列表
        for stu in self.stu_list:
            # 如果當前學生學號，與輸入的sid相等
            if stu.stu_id == sid:
                # 輸入成績字串，格式為：學科-分數，學科-分數
                score_str = input('清輸入成績（學科-分數，學科-分數）')
                # 將輸入的多個成績，按照逗號拆分，形成成績列表
                score_list = score_str.replace('，', ',').split(',')
                # 迴圈成績列表，依次新增成績
                for item in score_list:
                    # 獲取科目與成績
                    subject, score = item.split('-')
                    subject = subject.strip()
                    score = float(score.strip())
                    # 呼叫add_score方法，新增科目，成績
                    stu.add_score(subject, score)
                print('新增成功！')
                # 結束迴圈，同時結束set_score函式
                return
        # 若程式能執行到此處，證明在stu_list中沒有找到與sid對應的學生
        print('學號有誤！')

    # 提供主選單
    def run(self):
        while True:
            print('************學生管理************')
            print('1. 新增學生')
            print('2. 刪除學生')
            print('3. 查看所有學生')
            print('4. 錄入成績')
            print('5. 退出')

            chocie = input('請輸入操作編號：')
            if chocie == '1':
                self.add_student()
            elif chocie == '2':
                self.del_student()
            elif chocie == '3':
                self.show_all_student()
            elif chocie == '4':
                self.set_score()
            elif chocie == '5':
                print('再見！')
                break
            else:
                print('輸入有誤！')

m1 = Manager()
m1.run()
