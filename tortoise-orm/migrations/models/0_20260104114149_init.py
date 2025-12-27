from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "t_user" (
    "id" VARCHAR(36) NOT NULL PRIMARY KEY,
    "username" VARCHAR(64) NOT NULL UNIQUE,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "is_active" BOOL NOT NULL DEFAULT True,
    "age" INT NOT NULL DEFAULT 0,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJzVlm1PIjEQx78K4RWXeEYB0dw7UC5yEbjgenfRmE3ZlqWh2+K2qxLDd7dTdtkHdgmonP"
    "Ju9z/TdubXh5mXsicwYfLwRhK//KP0UubII/ojpR+Uymg6jVUQFBoy46jsIPIZSuUjR2l1"
    "hJgkWsJEOj6dKiq4VnnAGIjC0Y6Uu7EUcPoQEFsJl6ixieTuXsuUY/JMZPQ7ndgjShhOBU"
    "oxrG10W82mRjsfI/+n8YTlhrYjWODx2Hs6U2PBl+46GlBdwomPFMGJBCC+MNNIWsSqBeUH"
    "ZBkkjgVMRihgKpHwhhQcwYEg5UqaFD30bDPCXTXWv7XGfJFMnOrCCzL40xycXzYHlVrjG2"
    "Qi9DYsdqcXWqrGNDdTIIUWkxiwMUnYR/O9Bc/kmH2k2qhvQLVRL6QKJqAaUyQeomwbhMsB"
    "+8ivenKyAUDtVUjQ2NIIqbT1M0Ifc05iSwhGEC+43MlxGZpDPfAtOCMh5hm/bRHQJeE3AV"
    "3Dr9XvX0HQnpQPzAgdK8PxpttqDyrHBq92osrInZ6VYYrcHJodrvJJht4ZhjriXSE8eseB"
    "dGGR79Xj+mn9rNaon2kXE8hSOV2DeJWU4xNIzkZqFdiFtijqkXxq6ZEZeDgcehh97ArlO6"
    "+3zgH3OZuF53oNOqvTbV9bze7v1BG9aFptsFSNOsuolWyBWk5S+tuxLkvwW7rt99qGoJDK"
    "9c2KsZ91W4aYUKCEzcWTjXDikYvUCMwc2obRJFHuQBgiZ/KEfGyvWERVFPmumryql1UQ1z"
    "cHh3AhzLCNahKfOuO8Biu0rG2xUOzzZVqswqcjt8PKeTnCHfvUUvYhL0dxQ/VIfAkhbdEM"
    "JIZ8TDvwH16M3TcEcDW2gBi67yfA46OjDQBqr0KAxpapaYIrwnMK2q/rfq+gmMVDMiBvuE"
    "7wDlNHHZQYler+a2JdQxGyThWtCF6l2/yX5Xp+1W9lqxFM0NKMP7W8zF8BIW0Cjw=="
)
