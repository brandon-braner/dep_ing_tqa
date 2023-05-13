from fastapi import FastAPI
from app.modules.payments.routes import router as payments_router

app = FastAPI()


app.include_router(payments_router)


@app.get("/")
def root():
    return {"message": "Hello World"}
