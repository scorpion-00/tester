from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import asyncio

app = FastAPI()


@app.get("/hello")
async def say_hello():
    await asyncio.sleep(5)
    return {"message": "hello world"}

app.mount("/", StaticFiles(directory="static", html=True), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
