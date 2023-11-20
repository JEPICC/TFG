from contextlib import asynccontextmanager
from server.database import db
from decouple import config
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import ResponseValidationError
from server.users.router import users
from server.wells.routers.wells import wells
from server.wells.routers.meters import meters
from server.wells.routers.values import values
from server.wells.routers.services import services


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.connect_to_database()

app = FastAPI()

@app.exception_handler(ResponseValidationError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},)


app.add_middleware(
    CORSMiddleware, 
    allow_origins=[config('FRONTEND_URL')],
    # allow_methods=['*'],
    # allow_credentials=True,
    # allow_headers=['*']
)

app.include_router(users)
app.include_router(wells)
app.include_router(meters)
app.include_router(values)
app.include_router(services)


@app.get('/')
def home():
    return RedirectResponse(url='/docs')


