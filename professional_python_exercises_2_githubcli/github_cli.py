import os
import sys
import json
from typing import Optional
import dotenv
from github import Github
from github.NamedUser import NamedUser
import typer
import requests

app = typer.Typer()


def get_user_form_input() -> NamedUser:
    """
    Method used in the app commands to get the user from user input:

    Returns:
    user : NamedUser
    """
    name = input("User: ")
    if name == "":
        typer.echo("Empty Value inputted, try again")
        sys.exit("Failed to get user input")
    token = get_github_token()
    github_session = Github(token)
    if github_session.search_users(name).totalCount == 0:
        typer.echo("User not found, please try again.")
        sys.exit("Failed to find user.")
    user = github_session.get_user(name)
    return user


@app.command()
def countstars(json_format: Optional[bool] = False) -> int:
    """
    Counts the stars of a specified user and gives a nice comment to the user

    Parameters:
    json_format : Optional[bool] = False
      decides wether json or plain text format is required

    Returns:
    starCount : int
      number of stars
    """
    typer.echo("Enter user to count stars for.")
    user = get_user_form_input()
    name = user.name

    repositories = user.get_repos()
    star_count = 0
    for repo in repositories:
        stars = repo.stargazers_count
        star_count += stars
    if json_format:
        output = {}
        output["username"] = name
        output["stars"] = star_count
        print(json.dumps(output))
    else:
        typer.echo(f"User: {name} has {star_count}⭐ in {repositories.totalCount} repositories.")
        typer.echo(_rate_stars_to_repos(star_count, repositories.totalCount))
    return star_count


def _rate_stars_to_repos(star_count: int, repository_count: int) -> str:
    """
    Rates the star to repository count, a little fun never killed nobody.

    Parameters:
    star_count : int
      the number of stars for the user
    repository_count : int
      the number of repositories for the user

    Returns:
    message : str
      A message reflecting the rating
    """

    if star_count == 0 or repository_count == 0:
        return "This poor fellar. Work harder!"
    if star_count / repository_count > 100:
        return "Greetings, Mr. Starlord"
    if star_count / repository_count < 1:
        return "Keep doing what you're doing. But do more!"
    return "Not bad ey, not bad."


@app.command()
def getdetails(json_format: Optional[bool] = False) -> json:
    """
    Gets the details for a specified user.

    Parameters:
    json_format: Optional[bool] = False
      Decides wether nomal text output or json is required

    Returns:
    raw : json
      Raw details in json format fron the get details request
    """

    typer.echo("Enter user to get details for.")
    user = get_user_form_input()
    name = user.name
    typer.echo(f"Getting the detials for: {name}")

    bio = user.bio
    repocount = user.get_repos().totalCount
    star_count = 0
    for repo in user.get_repos():
        stars = repo.stargazers_count
        star_count += stars
    followers = user.get_followers()
    following = user.get_following()
    blog = user.blog
    company = user.company
    contributions = user.contributions
    created = user.created_at
    email = user.email
    organizations = user.get_orgs()
    avatar_url = user.avatar_url
    starred = user.get_starred()
    subs = user.get_subscriptions()
    watched = user.get_watched()
    location = user.location
    hireable = user.hireable

    raw = user.raw_data

    if json_format:
        print(raw)
    else:
        typer.echo(f"Details about user:{user}, created at {created}, bio: {bio}")
        typer.echo(
            f"Stars: {star_count}, repos: {repocount}, followers: {followers.totalCount}"
            f", following: {following.totalCount}"
        )
        typer.echo(
            f"Contributions: {contributions}, orgs: {organizations.totalCount},"
            f" starred: {starred.totalCount}, subs: {subs.totalCount},"
            f" watched: {watched.totalCount}"
        )
        typer.echo(f"Get a visual impression at:{avatar_url}")
        typer.echo(f"The blog: {blog}")
        typer.echo(f"Mail: {email}, hireable: {hireable}, location: {location}, company: {company}")
    return raw


@app.command()
def setstatus() -> bool:
    """
    Sets the status to something related to this repository: Drinking tea.
    Returns:
    success : bool
      success if successful status change could be accomplished
    """

    mutation = """mutation {
    changeUserStatus(input:{emoji:":tea:", message:"Drinking tea"}) {
        status{
            emoji
            message
        }
    }
    }
    """
    headers = {"Authorization": f"token {get_github_token()}"}
    request = requests.post(
        "https://api.github.com/graphql", json={"query": mutation}, headers=headers, timeout=30
    )
    if request.status_code == 200:
        typer.echo("Success")
        return True
    typer.echo(f"Mutation failed to run by returning code of {request.status_code}. {mutation}")
    return False


def get_github_token() -> str:
    """
    Checks, if API Key is set as an environment variable. If not, the user is
    asked to input it in the console. Length checks enabled for the API key. If
    key has non-valid length (!=32) the user is asked again to enter a valid key.
    The key is saved into a local .env file.
    Returns:
    github_token : str
      API Key for the Open Weather Map
    """

    dotenv_file = dotenv.find_dotenv()
    if dotenv_file == "":
        with open(os.getcwd() + "\\.env", mode="w", encoding="utf-8").close():
            pass
        dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)

    if "TNT_EX2_GITHUB_TOKEN" not in os.environ:
        print(
            "No API Key found in your environment variables. \nPlease look at "
            "https://github.com/settings/tokens for getting an API key and enter "
            "it in the following line:",
            file=sys.stderr,
        )
        os.environ["TNT_EX2_GITHUB_TOKEN"] = input("Please enter your API Key now: \n-->").strip()
    api_key = os.environ["TNT_EX2_GITHUB_TOKEN"]
    if len(api_key) != 40:
        print(
            "Wrong sized GitHub Accoss Token inputted (correct length: 40), "
            f"key found: {api_key}, \nplease look at https://github.com/settings/tokens "
            "for getting an API key and enter it in the following line:",
            file=sys.stderr,
        )
        os.environ["TNT_EX2_GITHUB_TOKEN"] = input("Please enter your API Key now:\n-->").strip()
        return get_github_token()

    dotenv.set_key(dotenv_file, "TNT_EX2_GITHUB_TOKEN", api_key)  # save the API key to .env file
    return api_key


if __name__ == "__main__":
    app()
