import json
import sys
from dataclasses import dataclass

import typer

from ..common.output import OutputFormat


def _user_rating_msg(star_count: int, repository_count: int) -> str:
    """
    Get a user rating message depending on the input args

    Args:
        star_count: The number of stars for all user repos combined
        repository_count: The number of repositories the user owns

    Returns:
        A message reflecting the rating
    """

    if star_count == 0 or repository_count == 0:
        return "This poor fellar. Work harder!"
    if star_count / repository_count > 100:
        return "Greetings, Mr. Starlord"
    if star_count / repository_count < 1:
        return "Keep doing what you're doing. But do more!"
    return "Not bad ey, not bad."


@dataclass
class RepoStarCount:
    """Class for holding information about repo star count"""

    username: str
    star_count: int
    repo_count: int

    def format_output(self, format: OutputFormat) -> str:
        if format == OutputFormat.json:
            output = {}
            output["username"] = self.username
            output["stars"] = self.star_count
            return json.dumps(output)

        if format == OutputFormat.text:
            output = (
                f"User '{self.username}' has {self.star_count}⭐ "
                f"in {self.repo_count} repositories.\n"
            )
            output += _user_rating_msg(self.star_count, self.repo_count)
            return output

        typer.echo(f"Unknown output format '{format}'")
        sys.exit(1)
