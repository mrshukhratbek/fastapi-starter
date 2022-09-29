from fastapi import FastAPI
import uvicorn
from config import APP_PORT

app = FastAPI()

@app.get('/')
async def root():
  return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=int(APP_PORT), reload=True)
