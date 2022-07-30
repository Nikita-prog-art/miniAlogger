import asyncio
import time
from typing import NamedTuple

from starlette import requests, responses
from starlette.applications import Starlette
from starlette.routing import Route


class LogEntity(NamedTuple):
    level: str
    time: str
    unix_time: float
    servise: str
    msg: str


logQ = asyncio.Queue()

async def log(request: requests.Request):
    data = await request.form()
    logEntity = LogEntity(
        data["level"], time.asctime(), time.time(), data["service"], data["msg"]
    )
    print(logEntity)
    await logQ.put(logEntity)
    return responses.PlainTextResponse(str((logEntity)))

app = Starlette(debug = True, routes = [
    Route('/', log, methods=['POST']
    )],
)
