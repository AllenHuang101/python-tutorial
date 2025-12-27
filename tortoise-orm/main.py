from typing import Dict, Union
import uvicorn
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# Tortoise-ORM 配置
TORTOISE_ORM: Dict = {
    "connections": {
        # 開發環境使用 SQLite（基於檔案，無需伺服器）
        # "default": "sqlite://db.sqlite3",
        # 生產環境示例：PostgreSQL
        "default": "postgres://postgres:postgres@localhost:5432/fastapi_db",
    },
    "apps": {
        "models": {
            "models": [
                "models.user",
                "models.student",
                "aerich.models",
            ],  # 模型模組與 Aerich 遷移模型
            "default_connection": "default",
        }
    },
    # 連線池配置（推薦）
    "db_pool": {
        "max_size": 10,  # 最大連線數
        "min_size": 1,  # 最小連線數
        "idle_timeout": 30,  # 閒置連線超時（秒）
    },
}


register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,  # 自動生成資料庫結構（開發環境使用）
    add_exception_handlers=True,  # 自動添默認加異常處理
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
