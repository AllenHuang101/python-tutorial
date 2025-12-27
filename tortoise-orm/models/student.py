from tortoise import fields, models


class Student(models.Model):
    """
    學生模型，包含基本資訊。
    用於示範單表的新增、刪除、修改、查詢操作。
    """

    id = fields.IntField(pk=True, description="學生 ID，主鍵")
    name = fields.CharField(max_length=50, description="學生姓名")
    age = fields.IntField(null=True, description="學生年齡，可為空值")
    email = fields.CharField(
        max_length=100, unique=True, null=True, description="學生電子郵件，唯一"
    )

    # related_name="student"，表示可以通過 StudentProfile 訪問對應的 Student
    profile = fields.OneToOneField(
        "models.StudentProfile",
        on_delete=fields.CASCADE,
        related_name="student",
        null=True,
    )

    class Meta:
        table = "students"

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Email: {self.email}"


class StudentProfile(models.Model):
    id = fields.IntField(pk=True)
    address = fields.CharField(max_length=100)
    phone = fields.CharField(max_length=20)


class Grade(models.Model):
    id = fields.IntField(pk=True)
    score = fields.FloatField()
    # 找 student 主鍵
    Student = fields.ForeignKeyField(
        "models.Student", related_name="grades", on_delete=fields.CASCADE
    )


class Course(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)

    # 無法實現中間表 StudentCourse 唯一約束
    # students = fields.ManyToManyField(
    #     "models.Student", related_name="courses", through="studentcourse")


class StudentCourse(models.Model):
    students = fields.ForeignKeyField("models.Student", related_name="courses")
    courses = fields.ForeignKeyField("models.Course", related_name="students")

    class Meta:
        table = "student_course"
        unique_together = ("students", "courses")
