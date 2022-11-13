import json
import sys
from dataclasses import dataclass

import typer

from ..common.output import OutputFormat


@dataclass
class UserDetails:
    """Class for storing details about a user"""

    # We just wrap API output here which is very verbose
    # pylint: disable=too-many-instance-attributes
    username: str
    bio: str
    blog: str
    company: str
    contributions: str
    location: str
    hireable: str
    email: str
    avatar_url: str
    created: str
    organization_count: int
    starred_count: int
    subs_count: int
    watched_count: int
    star_count: int
    repo_count: int
    follower_count: int
    following_count: int

    def format_output(
        self,
        # pylint: disable=redefined-builtin
        format: OutputFormat,
    ) -> str:
        """Format the class for output

        Args:
            format: How to format the output

        Returns:
            Formatted string
        """
        if format == OutputFormat.TEXT:
            output = "\n".join(
                (
                    f"Details about user:{self.username}, created at {self.created}, "
                    f"bio: {self.bio}",
                    f"Stars: {self.star_count}, repos: {self.repo_count}, "
                    f"followers: {self.follower_count}, following: {self.following_count}",
                    f"Contributions: {self.contributions}, orgs: {self.organization_count},"
                    f" starred: {self.starred_count}, subs: {self.subs_count},"
                    f" watched: {self.watched_count}",
                    f"Get a visual impression at: {self.avatar_url}",
                    f"The blog: {self.blog}",
                    f"Mail: {self.email}, hireable: {self.hireable}, location: {self.location}, "
                    f"company: {self.company}",
                )
            )
            return output

        if format == OutputFormat.JSON:
            return json.dumps(self.__dict__)

        typer.echo(f"Unknown output format '{format}'")
        sys.exit(1)
