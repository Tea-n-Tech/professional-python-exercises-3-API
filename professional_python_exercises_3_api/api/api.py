from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/health/ping")
async def ping():
    return {"ping": "pong!"}


@app.get("/api/v1/user")
async def get_self_user(username: str):
    pass


@app.get("/api/v1/user/stars")
async def get_self_stars(username: str):
    pass


@app.get("/api/v1/user/status")
async def get_status(username: str):
    pass


@app.post("/api/v1/user/status")
async def post_status(username: str, status: str):
    pass


@app.get("/api/v1/users/{username}")
async def get_user(username: str):
    pass


@app.get("/api/v1/users/{username}/stars")
async def get_stars(username: str):
    pass
