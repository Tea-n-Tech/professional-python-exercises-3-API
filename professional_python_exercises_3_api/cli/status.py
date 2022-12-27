import typer

from ..api.github_api import GitHubAPI
from ..api.token import get_github_token

status_cmd = typer.Typer(name="status", no_args_is_help=True)


@status_cmd.command(name="tea")
def set_status_tea():
    """
    Sets the status of the user to drinking tea 🍵💚
    """
    github_token = get_github_token()

    api = GitHubAPI(github_token)

    api.set_status(":tea:", "Drinking Tea")
    typer.echo("Your status has been set to drinking tea 🍵")


@status_cmd.command(name="clear")
def clear_status():
    """
    Clears the status of the user
    """
    github_token = get_github_token()

    api = GitHubAPI(github_token)

    api.set_status("", "")
    typer.echo("Your status has been cleared 👍")


@status_cmd.command(name="status")
def get_status() -> dict:
    """
    Gets the status of the user
    """
    github_token = get_github_token()

    api = GitHubAPI(github_token)

    status = api.get_status()
    typer.echo(status)
    return status
