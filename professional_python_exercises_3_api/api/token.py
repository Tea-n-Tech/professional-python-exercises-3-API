import os
import sys

import typer

ENV_GITHUB_TOKEN = "GITHUB_TOKEN"


def get_github_token() -> str:
    """Get the GitHub authentication token from the environment variables

    Returns:
        GitHub token
    """
    token = os.getenv(ENV_GITHUB_TOKEN)

    if not token:
        typer.echo(f"Please set the env var '{ENV_GITHUB_TOKEN}'")
        sys.exit(1)

    return token
