import unittest
from unittest.mock import Mock, patch

from typer.testing import CliRunner

from .status import status_cmd

runner = CliRunner()


class TestToken(unittest.TestCase):
    @patch("professional_python_exercises_2_githubcli.cli.status.get_github_token", autospec=True)
    @patch("professional_python_exercises_2_githubcli.cli.status.GitHubAPI", autospec=True)
    def test_status_tea(self, mock_api_cls: Mock, mock_token_fn: Mock):
        token = "abc123"

        mock_token_fn.return_value = token

        mock_api = mock_api_cls.return_value

        args = ["tea"]
        runner.invoke(status_cmd, args)

        mock_token_fn.assert_called_once_with()
        mock_api_cls.assert_called_once_with(token)
        mock_api.set_status.assert_called_once_with(":tea:", "Drinking Tea")

    @patch("professional_python_exercises_2_githubcli.cli.status.get_github_token", autospec=True)
    @patch("professional_python_exercises_2_githubcli.cli.status.GitHubAPI", autospec=True)
    def test_status_clear(self, mock_api_cls: Mock, mock_token_fn: Mock):
        token = "abc123"

        mock_token_fn.return_value = token

        mock_api = mock_api_cls.return_value

        args = ["clear"]
        runner.invoke(status_cmd, args)

        mock_token_fn.assert_called_once_with()
        mock_api_cls.assert_called_once_with(token)
        mock_api.set_status.assert_called_once_with("", "")
