import typer

from ..api.github_api import GitHubAPI
from ..api.token import get_github_token
from ..common.output import OutputFormat, print_output

user_cmd = typer.Typer(name="user", invoke_without_command=True)


@user_cmd.callback()
def user_cb(
    user="",
    # pylint: disable=redefined-builtin
    format: OutputFormat = OutputFormat.TEXT,
):
    """
    Gets the details for the authenticated user (default) or a specified user.

    Args:
        json_format: Decides wether nomal text output or json is required

    Returns:
        Details about the user
    """

    github_token = get_github_token()

    api = GitHubAPI(github_token)

    if not user:
        user = api.get_authenticated_user()

    user_details = api.user_details(username=user)
    output = user_details.format_output(format=format)
    print_output(obj=output, format=format)
