from fastapi import FastAPI
from app.modules.payments.routes import router as payments_router
from lagom.integrations.fast_api import FastApiIntegration
from lagom import Container

app = FastAPI()



app.include_router(payments_router)


@app.get("/")
def root():
    return {"message": "Hello World"}
