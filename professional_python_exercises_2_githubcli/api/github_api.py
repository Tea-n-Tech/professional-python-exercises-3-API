import sys
from http import HTTPStatus

import requests
import typer
from github import Github

from .repo_star_count import RepoStarCount
from .token import get_github_token
from .user_details import UserDetails


class GitHubAPI:
    """Class as interface to the GitHub API"""

    def __init__(self, token: str) -> None:
        self.session = Github(token)

    def get_authenticated_user(self) -> str:
        """Get the name of the authenticated user

        Returns:
            Name of the authenticated user
        """
        gh_user = self.session.get_user()
        return gh_user.login

    def count_repos_and_stars(self, username: str) -> RepoStarCount:
        """Count the stars and repos of a user

        Returns:
            Count of stars and repos for the user
        """
        stars = 0
        repos = 0

        repos_iterator = self.session.get_user(username).get_repos()
        for repo in repos_iterator:
            stars += repo.stargazers_count
            repos += 1

        return RepoStarCount(username=username, star_count=stars, repo_count=repos)

    def user_details(self, username: str) -> UserDetails:
        """Retrieve details about a specific user

        Returns:
            Details about the specified user
        """
        gh_user = self.session.get_user(username)

        star_count = 0
        repo_count = 0
        for repo in gh_user.get_repos():
            stars = repo.stargazers_count
            star_count += stars
            repo_count += 1
        followers = gh_user.get_followers()
        following = gh_user.get_following()
        organizations = gh_user.get_orgs()
        starred = gh_user.get_starred()
        subs = gh_user.get_subscriptions()
        watched = gh_user.get_watched()

        details = UserDetails(
            username=gh_user.login,
            bio=gh_user.bio,
            star_count=star_count,
            repo_count=repo_count,
            avatar_url=gh_user.avatar_url,
            follower_count=followers.totalCount,
            following_count=following.totalCount,
            blog=gh_user.blog,
            company=gh_user.company,
            contributions=gh_user.contributions,
            created=gh_user.created_at.isoformat(),
            email=gh_user.email,
            organization_count=organizations.totalCount,
            starred_count=starred.totalCount,
            subs_count=subs.totalCount,
            watched_count=watched.totalCount,
            location=gh_user.location,
            hireable=gh_user.hireable,
        )
        return details

    def set_status(self, emoji_name: str, message: str):
        """Set the status message of the authenticated user

        Args:
            emoji_name: Emoji name as string such as ':tea:' for 🍵
            message: Status message to display
        """
        payload = {}
        payload[
            "query"
        ] = """
        mutation($emoji_name: String, $message: String) {
            changeUserStatus(input:{emoji: $emoji_name, message: $message}) {
                status{
                    emoji
                    message
                }
            }
        }
        """
        payload["variables"] = {"emoji_name": emoji_name, "message": message}

        headers = {"Authorization": f"token {get_github_token()}"}
        response = requests.post(
            "https://api.github.com/graphql", json=payload, headers=headers, timeout=30
        )

        if response.status_code != HTTPStatus.OK:
            typer.echo(f"Mutation failed to run by returning code of {response.status_code}.")
            sys.exit(1)

        response_body = response.json()
        if isinstance(response_body, dict) and "errors" in response_body:
            for msg_obj in response_body["errors"]:
                typer.echo(f"{msg_obj['type']}: {msg_obj['message']}")
            sys.exit(1)
