from fastapi import FastAPI

from parser import parse_tenders

app = FastAPI()


@app.get('/tenders')
async def get_tenders():
    return parse_tenders()
