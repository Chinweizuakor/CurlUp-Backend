from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Ota and Caroline!"}


@app.get("/dashboard")
def read_root():
    return {"message": "This is My Dashboard!"}