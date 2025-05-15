from fastapi import FastAPI
import asyncio

app = FastAPI()

app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/hello")
async def say_hello():
    await asyncio.sleep(5)
    return {"message": "hello world"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
