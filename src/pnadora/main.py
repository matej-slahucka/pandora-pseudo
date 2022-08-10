from fastapi import APIRouter, FastAPI


app = FastAPI()
api_router = APIRouter()

@api_router.get("/")
def index():
    return "middlename42@middlename.com"

app.include_router(api_router)
