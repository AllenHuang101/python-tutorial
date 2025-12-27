from models.student import Course, Grade, Student, StudentCourse, StudentProfile
from tortoise import Tortoise, run_async


async def create_student(name: str, age: int = None, email: str = None) -> Student:
    try:
        stu = await Student.create(name=name, age=age, email=email)
        return stu
    except Exception as e:
        print(f"創建學生失敗: {e}")


async def update_student(
    stu_id: int, name: str = None, age: int = None, email: str = None
) -> Student:
    stu = await Student.get(id=stu_id)
    # 判斷使用者是否有傳遞某個資料；若未傳遞，則不進行更新。
    if name:
        stu.name = name
    if age is not None:
        stu.age = age
    if email is not None:
        stu.email = email

    await stu.save()
    return stu


async def delete_student(stu_id: int) -> None:
    stu = await Student.get(id=stu_id)
    await stu.delete()


# 單條數據
async def get_student(stu_id: int) -> Student:
    stu = await Student.get(id=stu_id)
    return stu


# 多條數據
async def get_students(name: str) -> list[Student]:
    """
    完成匹配
    """
    stus = await Student.filter(name=name)
    return stus


async def get_students2(name: str) -> list[Student]:
    """
    模糊查询
    """
    stus = await Student.filter(name__contains=name)
    return stus


async def get_students3() -> list[Student]:
    """
    獲取所有數據
    """
    stus = await Student.all()
    return stus


async def init():
    await Tortoise.init(
        db_url="postgres://postgres:postgres@localhost:5432/fastapi_db",
        modules={"models": ["models.student"]},
    )
    # await Tortoise.generate_schemas()


async def create_data():
    await init()
    # 1 對 1
    # stu1 = await Student.create(name="Allen")
    # pro1 = await StudentProfile.create(address="新北", phone="123456")
    # stu1.profile = pro1
    # await stu1.save()

    # pro2 = await StudentProfile.create(address="台北", phone="654321")
    # stu2 = await Student.create(name="Bob", profile=pro2)
    # print(stu2)

    # 1對多
    # stu7 = await Student.get(id=7)
    # await Grade.create(score=95, Student=stu7)
    # await Grade.create(score=98, Student=stu7)
    # await Grade.create(score=100, Student=stu7)

    # 多對多
    # stu7 = await Student.get(id=7)
    # stu8 = await Student.get(id=8)

    # cou1 = await Course.create(name="Python")
    # cou2 = await Course.create(name="React")
    # await StudentCourse.create(students=stu7, courses=cou1)
    # await StudentCourse.create(students=stu7, courses=cou2)
    # await StudentCourse.create(students=stu8, courses=cou1)
    # await StudentCourse.create(students=stu8, courses=cou2)


async def update_data():
    await init()
    # 1對1
    # stu = await Student.get(id=7)
    # pro = await StudentProfile.create(address="汐止", phone="12345678901")
    # stu.profile = pro
    # await stu.save()

    # 1對多
    stu2 = await Student.get(id=8)
    grade1 = await Grade.get(id=4)
    grade1.Student = stu2
    await grade1.save()

    await Grade.filter(id=7).update(Student=stu2)


async def query_data():
    await init()
    stu = await Student.get(id=7)
    print(stu.name)
    pro = await stu.profile
    print(pro.address)
    print(pro.phone)

    # 獲取關聯數據
    stu2 = await Student.get(id=7).prefetch_related("profile")
    print(stu2.profile.address)
    print(stu2.profile.phone)

    stu3 = await Student.get(id=7).prefetch_related("grades").all()
    for grade in stu3.grades:
        print(grade.score)


async def delete_data():
    await init()

    # grade = await Grade.get(id=9)
    # await grade.delete()

    stu = await Student.get(id=7)
    await stu.delete()


if __name__ == "__main__":
    # run_async(create_data())
    # run_async(update_data())
    run_async(delete_data())
    # run_async(query_data())
