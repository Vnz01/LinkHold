from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles   
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn

app = FastAPI()

app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get("/", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
    with open("home.html") as html:
        return HTMLResponse(content=html.read())
    
@app.get("/lists", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
    with open("holdinglinks.html") as html:
        return HTMLResponse(content=html.read())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6543)