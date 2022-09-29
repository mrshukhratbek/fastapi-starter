from fastapi import FastAPI
import uvicorn
from config import APP_PORT

from src.routers import users

app = FastAPI()

app.include_router(users)



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=int(APP_PORT), reload=True)
