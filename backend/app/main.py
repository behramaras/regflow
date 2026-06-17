from fastapi import FastAPI

from app.routes.dsar import router as dsar_router

app = FastAPI(
    title="Regflow",
    version="0.1.0"
)

app.include_router(dsar_router)


@app.get("/")
def root():
    return {
        "message": "Regflow API is running"
    }