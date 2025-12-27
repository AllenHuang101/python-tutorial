from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "grade" DROP CONSTRAINT IF EXISTS "fk_grade_students_63351866";
        ALTER TABLE "grade" RENAME COLUMN "student_id" TO "Student_id";
        ALTER TABLE "grade" ADD CONSTRAINT "fk_grade_students_af2b49de" FOREIGN KEY ("Student_id") REFERENCES "students" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "grade" DROP CONSTRAINT IF EXISTS "fk_grade_students_af2b49de";
        ALTER TABLE "grade" RENAME COLUMN "Student_id" TO "student_id";
        ALTER TABLE "grade" ADD CONSTRAINT "fk_grade_students_63351866" FOREIGN KEY ("student_id") REFERENCES "students" ("id") ON DELETE CASCADE;"""


MODELS_STATE = (
    "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"
)
