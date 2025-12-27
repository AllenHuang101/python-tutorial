from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "students" ALTER COLUMN "profile_id" DROP NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "students" ALTER COLUMN "profile_id" SET NOT NULL;"""


MODELS_STATE = (
    "eJztmm1zokgQgP+K5adc1d4W8qr3TY259TaJKWPurjZJUQMMhgqCC8NmU1v+9+sZeRcMJJ"
    "rIJV8s7emGmYee7p6WX+2Fa2Db/3zlY6/9R+tX20ELDF8y8k+tNlouEykVEKTZTJGoQaSj"
    "+cRDOgGpiWwfg8jAvu5ZS2K5DkidwLap0NVB0XLmiShwrO8BVok7x+SOzeT6FsSWY+Cf2I"
    "9+Lu9V08K2kZmoZdB7M7lKHpdMNrxD3gnTpLfTVN21g4WTaC8fyZ3rxOowGyqdYwd7iGAj"
    "tQA6v3ClkWg9VxAQL8DxJI1EYGATBTZJLbgiBd11KEHLIT5b4gL9VG3szMkd/BTk1XoxyV"
    "LXWnQFf/enwy/96ZEg/0ZX4sJjWD+d83CEZ0MrdglE0PoiDGxCkj5H9r0Gz7RNE6nKYgWq"
    "slhKlQ5RqglFvECWXQdhbNBEfrwkVQAIWqUE2VgWoeWrEEasHwWeOHBdGyOnZHOn7XI0NT"
    "B8Ds5IkPBMYlsENCb8LKBb+A0mk1M66YXvf7eZYDzLcbw6G4ymRx2GF5QswsTj81mOKZoX"
    "0Bw7pJhkqJ1jCDPeF0LuBQ45pzf5ne+IitgVZLELKmwisUTZgniTlO5hujgVkU1gxzBCrA"
    "Uuppa1zMEzQtPP0Zd9oXzh9oY1GBPHfgz9egu62fhsdDnrn11kXPS4PxvREZ5JH3PSo3yC"
    "ii/S+mc8+9KiP1vfJucjRtD1ydxjd0z0Zt/adE4oIK7quA8qMlJBLpJGYFa0bDDvU+mOCj"
    "Sk3z8gz1A3RlzeLdPdHFrwi7wEObBzjBAunWZYRg3dwPNxUYEVjmwtsfRE52BKrNLQUVhh"
    "FUSO8Im9aSrbSeQoL6jqFlO7LaReIVZkSgGJq1AJSFxpIUCHVnU2bALaJ4GB6aQ264XQ8u"
    "TrFNuILXATcLgVL9dXSXbk4RFfRS4TSaMovc/g9aeHjMLYtR7YGrrmscpH5GpQ5PJ11ysI"
    "XSe2i0rgxRY5fiY1OejNVEToeHI1OB21Lqaj4fhyPDnP1jJsMFtwT0f901wdGQYltZYPZo"
    "1er/5+e3fcCPwbJAv8EXzOmjtf8SOjOYZJIUcvcsNsiD9MimXBHcQeeoijW85HYJGwNLx2"
    "w2H/ctg/HrVXb1PmRngLckWKfHm2SOfxJxNG+yaQNKV7EyhSx7wJZMR3QKJ0tZvANDkdvg"
    "ucBJ8ir1G5iUBH4UHe1XUFPhEHEoHj2EEl/XR2duEbh16DhyvJkgbjSk+AEUXTRbCTEAbd"
    "rkzvI3dFpsOBvNvDzJrek+dBvyfLYiQRTYypptCLJLKCJXpPmYfvom5QHUlPFvZ+kmfmsb"
    "XGx9HTErEAz6knKFL+QX+cCmqEsdyukHqGQPcAZ1Skuoezwtv0t0Jv3D1RrMA+75lyJ4kz"
    "GOQKp9GogRT4lDhBf00vfrO2dh7yLmICDaUmDdmaBIG2x5kSDQ6mHOOWeJNKOO45Lt3hqv"
    "g0aJU6NRvLUl96rmnZuF4NmTXaiY834TzzrM4BO5++sG8QH4ObU1JmG96s4fHRPCl0kHAz"
    "bcKZOHjmwke9k8dFcrkD24JVTx/Z6FLh9LGLE0V5/3zD7548Xaj7aqdfZ84v0a66/Z+W2w"
    "fTqwpB18uRWaP31GcpaFHVZJezek/wnm5SFaTRd92l8rcmikplSG1+TSxC8viyAeoAm3xR"
    "JVOek1O1zpNJOVVmffxTdGhRb1v2RYbhYb9g15Z3BlImzfynez9HfQBRqy8YGzQTIl+FIV"
    "+OkK/7ukCtmFjhz6fodBwdBCufkV+zx7ibw3GN7NDHnqXfFWWFcGRrNkCJzkcWaFAW+IE9"
    "P3T9quErZdLQALaPV5/p1qiTStfqzQS4lzQKdySF4fqvy8l5WS8gNsmBvHJggdeGpZNPLd"
    "vyye1hYt1Cka6avbwSvZ4bwTs66/+b5zo8nQwYhdR7t/QCgz0m2krpZfUfTbDoYg=="
)
