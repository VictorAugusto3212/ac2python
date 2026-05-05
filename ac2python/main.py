from fastapi import FastAPI
from database import create_table
from controller.produto_controller import router as produto_router


app = FastAPI()

create_table()

app.include_router(produto_router)