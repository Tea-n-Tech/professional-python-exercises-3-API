import unittest
from datetime import datetime
from unittest.mock import Mock, patch

from ..common.output import OutputFormat
from .user_details import UserDetails

_example_user_details = UserDetails(
    username="username",
    bio="bio",
    blog="blog",
    company="company",
    contributions="contributions",
    location="location",
    hireable="hireable",
    email="email",
    avatar_url="avatar_url",
    organization_count=13,
    starred_count=13,
    subs_count=13,
    watched_count=13,
    star_count=13,
    repo_count=13,
    follower_count=13,
    following_count=13,
    created=datetime.now().isoformat(),
)


class TestUserDetails(unittest.TestCase):
    @patch("professional_python_exercises_2_githubcli.api.user_details.typer.echo", autospec=True)
    def test_format_output_text(self, mock_typer_echo: Mock):
        output = _example_user_details.format_output(OutputFormat.TEXT)
        assert output.startswith("Details about user")
        mock_typer_echo.assert_not_called()

    @patch("professional_python_exercises_2_githubcli.api.user_details.typer.echo", autospec=True)
    def test_format_output_json(self, mock_typer_echo: Mock):
        output = _example_user_details.format_output(OutputFormat.JSON)
        assert output.startswith("{")
        mock_typer_echo.assert_not_called()

    @patch("professional_python_exercises_2_githubcli.api.user_details.typer.echo", autospec=True)
    def test_format_output_unknown(self, mock_typer_echo: Mock):
        with self.assertRaises(SystemExit) as ex:
            _example_user_details.format_output("Wrong")
            assert ex.exception.code == 1
        mock_typer_echo.assert_called_once_with("Unknown output format 'Wrong'")
