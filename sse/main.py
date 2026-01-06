import asyncio
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from openai import AsyncOpenAI

load_dotenv("../.env", override=True)

app = FastAPI()


@app.get("/stream")
async def main():
    async def data_generator():
        for i in range(10):
            yield f"data: fake data {i} \n\n"
            await asyncio.sleep(1)

    return StreamingResponse(data_generator(), media_type="text/event-stream")


@app.get("/llm-stream")
async def llm_stream():
    async def llm_generator():
        client = AsyncOpenAI()

        stream = await client.responses.create(
            model="gpt-5-mini",
            instructions="You are a assistant. 一率用繁體中文回應",  # 這個參數會插入當作第一個 develop message
            input="hello",
            stream=True,
        )

        async for event in stream:
            # 根據事件類型解析內容
            if hasattr(event, "type"):
                if event.type == "response.output_text.delta":
                    # 文字增量事件
                    if hasattr(event, "delta") and event.delta:
                        yield f"data: {event.delta}\n\n"
                elif event.type == "response.output_text.done":
                    # 文字完成事件
                    if hasattr(event, "text") and event.text:
                        yield f"data: [DONE] Final text: {event.text}\n\n"
                elif event.type == "response.completed":
                    # 整個回應完成
                    yield "data: [COMPLETED]"

    return StreamingResponse(llm_generator(), media_type="text/event-stream")
