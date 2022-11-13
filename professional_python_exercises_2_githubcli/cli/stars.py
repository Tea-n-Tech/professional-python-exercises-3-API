import typer

from ..api.github_api import GitHubAPI
from ..api.token import get_github_token
from ..common.output import OutputFormat, print_output

stars_cmd = typer.Typer(name="stars", invoke_without_command=True)


@stars_cmd.callback()
def stars(
    user="",
    # pylint: disable=redefined-builtin
    format: OutputFormat = OutputFormat.text,
):
    """
    Counts the stars of a specified user and gives a nice comment to the user

    Args:
        user: Name of the user or org to count the stars of. If not specified,
              this is the authenticated user.
        json_format: Decides wether json or plain text format is required
    """
    github_token = get_github_token()

    api = GitHubAPI(github_token)

    if not user:
        user = api.get_authenticated_user()

    counter = api.count_repos_and_stars(user)
    output = counter.format_output(format)
    print_output(obj=output, format=format)
