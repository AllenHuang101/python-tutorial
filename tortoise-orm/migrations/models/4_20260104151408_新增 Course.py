from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "course" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL
);
        CREATE TABLE IF NOT EXISTS "student_course" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "courses_id" INT NOT NULL REFERENCES "course" ("id") ON DELETE CASCADE,
    "students_id" INT NOT NULL REFERENCES "students" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_student_cou_student_6b3972" UNIQUE ("students_id", "courses_id")
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "course";
        DROP TABLE IF EXISTS "student_course";"""


MODELS_STATE = (
    "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"
)
