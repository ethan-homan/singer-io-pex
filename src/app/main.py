from fastapi import FastAPI

import uvicorn

from app.config import SERVICE_HOST, SERVICE_PORT
from app.routes import router

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host=SERVICE_HOST, port=SERVICE_PORT, log_level="info")
