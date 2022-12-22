import unittest
from unittest.mock import Mock, patch

from typer.testing import CliRunner

from ..common.output import OutputFormat
from .user import user_cmd

runner = CliRunner()


class TestUserCmd(unittest.TestCase):
    @patch("professional_python_exercises_2_githubcli.cli.user.print_output", autospec=True)
    @patch("professional_python_exercises_2_githubcli.cli.user.get_github_token", autospec=True)
    @patch("professional_python_exercises_2_githubcli.cli.user.GitHubAPI", autospec=True)
    def test_user(self, mock_api_cls: Mock, mock_token_fn: Mock, mock_print_fn: Mock):
        username = "login"
        token = "abc123"
        expected_user_details = "Pewpew"

        mock_token_fn.return_value = token

        mock_api = mock_api_cls.return_value
        mock_api.get_authenticated_user.return_value = username
        user_details_mock = mock_api.user_details.return_value
        user_details_mock.format_output.return_value = expected_user_details

        args = []
        runner.invoke(user_cmd, args)

        mock_api_cls.assert_called_once_with(token)
        mock_api.get_authenticated_user.assert_called_once_with()
        mock_token_fn.assert_called_once_with()
        mock_api.user_details.assert_called_once_with(username)
        user_details_mock.format_output.assert_called_once_with(format=OutputFormat.TEXT)
        # # We don't check the exact message as this is likely to change.
        mock_print_fn.assert_called_once()

    @patch("professional_python_exercises_2_githubcli.cli.user.print_output", autospec=True)
    @patch("professional_python_exercises_2_githubcli.cli.user.get_github_token", autospec=True)
    @patch("professional_python_exercises_2_githubcli.cli.user.GitHubAPI", autospec=True)
    def test_user_format_json(self, mock_api_cls: Mock, mock_token_fn: Mock, mock_print_fn: Mock):
        username = "login"
        token = "abc123"
        expected_user_details = "Pewpew"

        mock_token_fn.return_value = token

        mock_api = mock_api_cls.return_value
        mock_api.get_authenticated_user.return_value = username
        user_details_mock = mock_api.user_details.return_value
        user_details_mock.format_output.return_value = expected_user_details

        args = ["--format", "json"]
        runner.invoke(user_cmd, args)

        mock_api_cls.assert_called_once_with(token)
        mock_api.get_authenticated_user.assert_called_once_with()
        mock_token_fn.assert_called_once_with()
        mock_api.user_details.assert_called_once_with(username)
        user_details_mock.format_output.assert_called_once_with(format=OutputFormat.JSON)
        # # We don't check the exact message as this is likely to change.
        mock_print_fn.assert_called_once()
