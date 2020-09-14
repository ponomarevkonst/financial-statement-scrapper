from typing import List, Optional

import uvicorn as uvicorn
from fastapi import FastAPI, Query
from nalog_scrapper import main

app = FastAPI()


@app.get("/organisations/")
def read_items(inn: Optional[List[str]] = Query(['6704000505', '5321029508'])):
    return main(inn)

if __name__ == '__main__':
    uvicorn.run("server:app", host="127.0.0.1", port=80, log_level="info")