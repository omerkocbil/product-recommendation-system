from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse

from api.api import api_router

app = FastAPI()
root_router = APIRouter()

@root_router.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Ömer</title>
        </head>
        <body>
            <h1>Hello, I am Product Recommendation System<h1>
            <h3>Please type "/recommend/{product_id}" for recommendation or "/docs" for documentation</h3>
        </body>
    </html>
    """

app.include_router(api_router)
app.include_router(root_router)