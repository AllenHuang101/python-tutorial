from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "grade" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "score" DOUBLE PRECISION NOT NULL,
    "student_id" INT NOT NULL REFERENCES "students" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "grade";"""


MODELS_STATE = (
    "eJztmW1v2kgQgP8K4lNO6lXGr3DfgJAr1wQiQu5ObSprba/BillTe900qvjvN7v4HZsaCg"
    "V0/YLM7Mx659nxzKz9rbnwLOwGbx8D7Df/aHxrErTAcJGTv2k00XKZSpmAIsPlilQPYx0j"
    "oD4yKUht5AYYRBYOTN9ZUscjICWh6zKhZ4KiQ2apKCTO5xDr1JthOucr+fgJxA6x8FccxH"
    "+Xz7rtYNfKLdSx2L25XKevSy7rz5F/wzXZ7Qzd9NxwQVLt5SudeyRRh9Uw6QwT7COKrYwD"
    "bH2Rp7FovVYQUD/EySKtVGBhG4UuzThck4LpEUbQITTgLi7QV93FZEbn8FdSV2tnUlfXWs"
    "yDv7uT/rvu5EpSf2OeeLAN690ZRSMiH1rxKRBF60k42JQk20d+vQPPrM0lUlXlGlRVuZIq"
    "G2JUU4p4gRx3F4SJwSXyExWlBkDQqiTIx/IInUCHNOJ8KYnEnue5GJGKhztrV6BpgOE+OG"
    "NByjPNbTHQhPBeQLfw643Ht2zRiyD47HLBcFrg+HjXG0yuWhwvKDmUi4ejaYEpmpXQHBJa"
    "TjLSLjCEFR8LofADATljN/ldbMma3JZUuQ0qfCGJRNuCeJOU6WPmnI7oJrBrGKHOApdTy1"
    "sW4FmR6dv44lgof/DxBh+sMXFfo7jegm46vBs8TLt397kQve5OB2xE5NLXgvSqWKCSSRr/"
    "DKfvGuxv48N4NOAEvYDOfH7HVG/6ocnWhELq6cR70ZGVSXKxNAazYm2D/Zwpd0xgIPP5Bf"
    "mWvjHiiV6V7ubQQlwUJYjAk2NFcNkyozbqTx9ZuKy/Wg9sbbBmicrZ9FeVeaO0vSpJG9F2"
    "nbSOHSRtVHdTgen5JSn3xvVQBbzEosDPZibnmS22ELoeP/ZuB437yaA/fBiOR/l0wAfzNW"
    "sy6N4WUnFAQwsTqu8Ug3mjn1fCTh+OG8lug2RJPELMOTPyHr9ymkNYFCJmWRhGGeshnen8"
    "KK7iYIilad7w0UuS3QoxAk6Ca3gdhv3uQ797PWiuTlMpYrwltSJDvrpaRJ4FtQpG8ylUDK"
    "39FGpKy34KVSS2QKK1jafQtgUTriVBgV9ZNJjcRqCjiSBvm6YGv0gAiSQIvNZnd+dgEz8R"
    "NocIM6mKAeNaR4IRzTBlsFMQBt22yu6jtmWuI4C83cHcmt1TFEG/o6pyLJFtjJmm1Iklqo"
    "YVdk9VhGvZtJiOYqaO/X+KZ27bGsPreLdkLME+dSRNKW70aWrrrm8pDvuGYu80VngqlI4l"
    "sWdAsGpSzZ28FaHGwVsRKs/dbOhUR8QoGg9PFGvwnHdstZXmGQxyTTBY1kAa/CqCZP7MKD"
    "7Zm6Ei5EPkBJZKbZayDQUSbUewFZYcbDXBrYg2kwjCPiHdEurENGhVBjUfy1Nf+p7tuHi3"
    "HjJvdJge8hIONDscl1PC/IAalLyri+xu3k+wi7g7lV1lcg6+nJ5ytdkGbkTdJpQxwVMPfn"
    "brtu/T6c4t7Oq23PlHqkbLfYg2OuZW3U1nyH63qc5s6q93MeeWurb1i8iyfByUpKjq2psx"
    "OXHXuOeXmeMUUwCxU+edGFwmRLEOQ7EaocgJHusldI3XO3ENjsvO9ytx/fc7B+viD1OKd6"
    "gOXew75rysKkQjW6sBSnV+VYELqgJfsB9EoV83fWVMLjSBHeP7PHs0dimla/XLBHiUMgp3"
    "pKXp+q+H8aji23JqUgD5SMDBj5Zj0jcN1wnop/PEuoUi8zr3DTmGd3XX/bfItX877hU/Dr"
    "MJekcstLXKy+o/AQ6OsQ=="
)
