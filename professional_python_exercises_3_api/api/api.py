import os
from fastapi import FastAPI, HTTPException, status
from ..cli.user import user_cb
from ..cli.stars import stars
from ..cli.status import clear_status, set_status_tea, get_status
from ..common.output import OutputFormat

app = FastAPI()
ENV_GITHUB_TOKEN = "GITHUB_TOKEN"


@app.get("/api/v1/health/ping")
async def ping():
    """
    API method to check if the GITHUB Token was set
    """

    token = os.getenv(ENV_GITHUB_TOKEN)

    if not token:
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Please set the env var 'GITHUB_TOKEN', it is not set!",
        )
    if len(token) < 40:
        return HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Please set the env var 'GITHUB_TOKEN' to a valid token. Wrong lenght!",
        )
    return HTTPException(
        status_code=status.HTTP_200_OK,
        detail="Token is set and of valid length. If still not valid , please check!",
    )


@app.get("/api/v1/user")
async def get_self_user():
    """
    API method to get the details of the authenticated user
    """
    return user_cb(user="", format=OutputFormat.JSON)


@app.get("/api/v1/user/stars")
async def get_self_stars():
    """
    API method to get the stars of the authenticated user
    """
    return stars(user="", format=OutputFormat.JSON)


@app.get("/api/v1/user/status")
async def get_status_api():
    """
    API method to get the status of the authenticated user
    """
    return get_status()


@app.post("/api/v1/user/status")
async def post_status():
    """
    API method to set the status of the user to 'Drinking tea'
    """
    clear_status()
    set_status_tea()
    return HTTPException(
        status_code=status.HTTP_200_OK,
        detail="Status set to 'Drinking tea', it's what you should do now!",
    )


@app.get("/api/v1/users/{username}")
async def get_user(username: str):
    """
    API method to get the details of a specified user
    """
    return user_cb(user=username, format=OutputFormat.JSON)


@app.get("/api/v1/users/{username}/stars")
async def get_stars(username: str):
    """
    API method to get the stars of a specified user
    """
    return stars(user=username, format=OutputFormat.JSON)
