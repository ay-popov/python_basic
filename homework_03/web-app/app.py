from fastapi import FastAPI
from datetime import datetime
from views import router as items_router

app = FastAPI()
app.include_router(items_router)


@app.get("/")
def root():
    return {"message": "Hello, Suren!", "now": datetime.now()}
