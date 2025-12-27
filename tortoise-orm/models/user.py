from tortoise.models import Model
from tortoise.fields import CharField, DatetimeField, BooleanField, IntField


class User(Model):
    id = CharField(max_length=36, pk=True)              # 主鍵，UUID 字串
    username = CharField(max_length=64, unique=True)    # 使用者名稱，唯一
    email = CharField(max_length=255, unique=True)                   # 電子郵件
    is_active = BooleanField(default=True)              # 是否啟用
    age = IntField(default=0)                           # 年齡，預設為 0    
    created_at = DatetimeField(auto_now_add=True)       # 建立時間
 
    class Meta:
        table = "t_user"
        # unique_together = ("username", "email")  # 複合唯一約束                          
        ordering = ["-created_at"]          # - 降冪排序            
        # 創建索引
        # indexes = ["email"]
                              
    def __str__(self):
        return self.username
