from typing import List, Optional

import uvicorn as uvicorn
from fastapi import FastAPI, Query
from nalog_scrapper import main

app = FastAPI()


@app.get("/nalogru/")
def read_items(inn: Optional[List[str]] = Query(['6704000505', '5321029508'])):
    return main(inn)

if __name__ == '__main__':
    uvicorn.run("server:app", host="0.0.0.0", port=5000, log_level="info")
