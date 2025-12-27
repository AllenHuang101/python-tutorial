from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "studentprofile" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "address" VARCHAR(100) NOT NULL,
    "phone" VARCHAR(20) NOT NULL
);
        ALTER TABLE "students" ADD "profile_id" INT NOT NULL UNIQUE;
        ALTER TABLE "students" ADD CONSTRAINT "fk_students_studentp_cb1173b3" FOREIGN KEY ("profile_id") REFERENCES "studentprofile" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "students" DROP CONSTRAINT IF EXISTS "fk_students_studentp_cb1173b3";
        ALTER TABLE "students" DROP COLUMN "profile_id";
        DROP TABLE IF EXISTS "studentprofile";"""


MODELS_STATE = (
    "eJztmW1v2kgQx78K4lVO6lXGj3DvgHAqpyZUCbk7tVTW2l4TK2ZN7XXTqOK738xi4wdsag"
    "gkQbo3lvnv7MP8dj0zNj/bi8ChfvT+LqJh+4/WzzYjCwo3Bf1dq02Wy0xFgRPLF4bcjFMb"
    "K+IhsTmoLvEjCpJDIzv0ltwLGKgs9n0UAxsMPTbPpJh532Jq8mBO+b1YyZevIHvMoT9olP"
    "5cPpiuR32nsFDPwbmFbvKnpdCG9yT8U1jidJZpB368YJn18onfB2xjDqtBdU4ZDQmnTs4B"
    "XF/iaSqt1woCD2O6WaSTCQ51SezznMMNKdgBQ4Ie45FwcUF+mD5lc34PPxV9tXYmc3VthR"
    "783b8ZfujfXCj6b+hJANuw3p3rpEUWTSsxBOFkPYgAm5HEfRT3e/DM9zlHqrragKqu1lLF"
    "JqSaUaQL4vn7INx0OEd+sqY1AAhWtQRFWxGhF5kQRrzvFSdxEAQ+Jazm4c73K9G0oOMhOF"
    "Mh45nFthTohvBBQHfwG0wmH3HRiyj65gthPC1xvLsajG4uOgIvGHlcyOPraYkpmVfQHDNe"
    "TTKxLjGEFZ8KofSMAznHSX6XO6qhdhVd7YKJWMhGMXYg3iZlhxSdMwnfBnYJLdxb0GpqxZ"
    "4leE7S9X16cyqUz3y8wQdnwvyn5FzvQDcdX41up/2rT4UjetmfjrBFFupTSb0oJ6jNIK1/"
    "xtMPLfzZ+jy5HgmCQcTnoZgxs5t+buOaSMwDkwWPJnFyQS5VUzArLBvch1y6Q8Ei9sMjCR"
    "1zqyWQgzrb7aaFvCgrhMGT4yRwcZlJGXXLY4cyXlVhpU07i6xobRQ1KrPas1izjO4sNrSO"
    "O4t1IndAMbrWLHZdyYZ7RdLgqsoW6i4BG0MGvWvbBlyJBIoiSWIH8yfmaAPPGI4hw0i6Zk"
    "G70VOgxbBsFfpphIJtV8d59K4qbCTQuz0qeuOcsgz2PV1XU0V1KUVLpZcqukE1nFOX4V61"
    "HbTR7MyxI5ectaG0suKsiKTJCT5Bai9sW2t8me6WShXYp55iaOWNPmWgra8/9609j1t3Hh"
    "xaS0+F1nMUfAYkpyHVQj2lSQ3KKU2qraaw6bUSf3Iaj0+UGvCc91y9k8UZCrohWRg1iAFX"
    "TVLslzzFr1bvlyEfIyZgKHUxZFsaBNqe5GoYHFx9g1uTXVQk6ZAj3ZGanGmwqj3Uoq1IfR"
    "kGrudTc69QXOx0nOL25K9bRziuzyqCtphvA58wOg3gIqiPYfmE2VVhpFjxfMqGe2vQV+nJ"
    "SdVsipA8biqC0oECT8E/un4DG/Zvh/3LUXt19CIy5VZfS+bI/rKkzG3q2/l+94aLqRd+La"
    "2vluC9B16Non0yT67LK9dMB35tOk0qARB71Z2bDucJUW7CUK5HKAuCp3qxzvYlyl6MS98A"
    "k55p2rmhPhFIfpVxXrKGfXauWe2ZHfo09Oz7qqyQtOzMBiSz+T8LnFEW+E7DKDn6TcNXrs"
    "uZBrBT/OeAj8Y+qXRtfp4AT5JGYUZeGa7/up1c13wvz7qUQN4xcPCL49n8Xcv3Iv71bWLd"
    "QRG9LnwXT+FdXPX/LXMdfpwMyh+8cYDBCRNto/Sy+g/VZzxr"
)
