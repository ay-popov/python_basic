from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "ok"}

@app.get("/ping")
def root():
    return {"message": "poooong"}
