import asyncio
import time
import uvicorn
from fastapi import FastAPI, Request, Query, Body

from hotels import router as router_hotels

app = FastAPI()
app.include_router(router_hotels)


if __name__=="__main__":
    uvicorn.run("main:app", reload=True)