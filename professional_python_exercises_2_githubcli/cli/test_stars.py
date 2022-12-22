import unittest
from unittest.mock import Mock, patch

from typer.testing import CliRunner

from ..api.repo_star_count import RepoStarCount
from .stars import stars_cmd

runner = CliRunner()


class TestStarsCmd(unittest.TestCase):
    @patch("professional_python_exercises_2_githubcli.cli.stars.print_output", autospec=True)
    @patch("professional_python_exercises_2_githubcli.cli.stars.get_github_token", autospec=True)
    @patch("professional_python_exercises_2_githubcli.cli.stars.GitHubAPI", autospec=True)
    def test_stars(self, mock_api_cls: Mock, mock_token_fn: Mock, mock_print_fn: Mock):
        username = "login"
        token = "abc123"

        mock_token_fn.return_value = token

        mock_api = mock_api_cls.return_value
        mock_api.get_authenticated_user.return_value = username
        mock_api.count_repos_and_stars.return_value = RepoStarCount(
            repo_count=1, star_count=2, username=username
        )

        args = []
        runner.invoke(stars_cmd, args)

        mock_api_cls.assert_called_once_with(token)
        mock_api.get_authenticated_user.assert_called_once_with()
        mock_token_fn.assert_called_once_with()
        # We don't check the exact message as this is likely to change.
        mock_print_fn.assert_called_once()

    @patch("professional_python_exercises_2_githubcli.cli.stars.print_output", autospec=True)
    @patch("professional_python_exercises_2_githubcli.cli.stars.get_github_token", autospec=True)
    @patch("professional_python_exercises_2_githubcli.cli.stars.GitHubAPI", autospec=True)
    def test_stars_format_json(self, mock_api_cls: Mock, mock_token_fn: Mock, mock_print_fn: Mock):
        username = "login"
        token = "abc123"

        mock_token_fn.return_value = token

        mock_api = mock_api_cls.return_value
        mock_api.get_authenticated_user.return_value = username
        mock_api.count_repos_and_stars.return_value = RepoStarCount(
            repo_count=1, star_count=2, username=username
        )

        args = ["--format", "json"]
        runner.invoke(stars_cmd, args)

        mock_api_cls.assert_called_once_with(token)
        mock_api.get_authenticated_user.assert_called_once_with()
        mock_token_fn.assert_called_once_with()
        # We don't check the exact message as this is likely to change.
        mock_print_fn.assert_called_once()
