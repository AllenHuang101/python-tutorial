from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "students" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "age" INT,
    "email" VARCHAR(100) UNIQUE
);
COMMENT ON COLUMN "students"."id" IS '學生 ID，主鍵';
COMMENT ON COLUMN "students"."name" IS '學生姓名';
COMMENT ON COLUMN "students"."age" IS '學生年齡，可為空值';
COMMENT ON COLUMN "students"."email" IS '學生電子郵件，唯一';
COMMENT ON TABLE "students" IS '學生模型，包含基本資訊。';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "students";"""


MODELS_STATE = (
    "eJzVmFFvmzAQx79KlKdO2iYCGJK9JW2nZVqbqU23acuEDDYJKpgMzLZqynffnQMh0BAlXb"
    "qmL4j872x8P9vnc/60o5jxMH19k/Kk/ab1py1oxOGlor9stel8XqooSOqGylE6WeHjpjKh"
    "ngTVp2HKQWI89ZJgLoNYgCqyMEQx9sAxENNSykTwI+OOjKdcztRIvn0HORCM/+Zp8XN+6/"
    "gBD1lloAHDbyvdkXdzpZ3OaPJWeeLnXMeLwywSpff8Ts5isXKH0aA65YInVHK2FgCOL4+0"
    "kJZjBUEmGV8NkpUC4z7NQrkW8I4UvFggwUDIVIUY0d9OyMVUzuCnYS2WwZShLr0wgk/9q9"
    "N3/asTw3qBkcQwDcvZucwtujItVBdU0mUnCmxJEudRve/Bc73Nc6RqmTtQtcxGqmhCqiVF"
    "HtEg3AfhqsFz5KcTsgNA8GokqGxVhEHqQBoJfm5YiYM4DjkVDZt7vV2NpgsNH4KzEEqeZW"
    "4rgK4IPwjoFn6D0egDDjpK0x+hEobjGsebi8H51UlH4QWnQCp5eDmuMaXTDTSHQm4mmXvX"
    "GMKIHwuh9g8LcoofeaV3TNvsGpbZBRc1kJVib0F8n5SXcAzOofI+sDOwyCDim6lVW9bgsb"
    "zp6+LlsVD+4/aGGNhIhHf5ut6Cbjy8OL8e9y8+VpboWX98jhZdqXc19aR+QK06aX0ejt+1"
    "8Gfr6+jyXBGMUzlN1BdLv/HXNo6JZjJ2RPzLoWwtyRVqAWaBZYN/u3bcoeBS7/YXTZhzzx"
    "LrcZPvfVOkR3WFCtg5LIeLw8zLqGuZMS7kpgqrMG0tstKlU7pTmdWeZMS1u5PMJh1/kllU"
    "74Bid91J5vuaB++GRuBp6i7qPgUfWwe963k2PKkGiqFpagbXV8zBOp4I7EOHnizigt3uGW"
    "CxXc+EdoRy8O1a+B2rayofDfRuj6vW+E1dB/+eZZmFYvqco6fRKxTL5gS/aenwbnoMfYhX"
    "BnbgkrMxlW6sODdk0nwFP8LRXpm21vCsmC2TGzBPPcMm9Yl+zETbXH/uW3setu58cGqt7Q"
    "rSYwbuAY3tSLVSTxFth3KKaI3VFJqe6uDPV+PhiXIb9nnPtzplnuGg25qLWYPa8CSa4f3P"
    "Vfxk9X4d8iFyAqZSH1O2SyDR9jSfYHLwrRVuovuoaNpDlnRH22VNg1fjola2xbGc5X2eBN"
    "5s01GeW7ae5LT0OZq/S4747PrPt4Dmw+knT1Ic0h4bfa3JEx9Rx3S5x62xB8Tc/XkCPFjq"
    "q9xPYyHzC0MV4vvr0WXDxbRsUgN5IyDAbyzw5MtWGKTy+3Fi3UIRo65cQAt4Jxf9L3Wupx"
    "9Gg/rNEjsYPPXxsvgLauty8Q=="
)
