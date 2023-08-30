from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title='REST API with FastApi and mongodb',
    description='This is a simple REST API using FastApi and mongodb'
)

app.include_router(user)