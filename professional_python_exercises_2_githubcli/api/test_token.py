import unittest
from unittest.mock import Mock, patch

from .token import get_github_token, ENV_GITHUB_TOKEN


class TestToken(unittest.TestCase):
    @patch("professional_python_exercises_2_githubcli.api.token.typer.echo", autospec=True)
    @patch("professional_python_exercises_2_githubcli.api.token.sys.exit")
    @patch("professional_python_exercises_2_githubcli.api.token.os.getenv")
    def test_get_github_token_success(
        self, mock_os_getenv: Mock, mock_sys_exit: Mock, mock_typer_echo: Mock
    ):
        expected_token = "abc123"
        mock_os_getenv.return_value = expected_token

        token = get_github_token()

        assert token == expected_token
        mock_os_getenv.assert_called_once_with(ENV_GITHUB_TOKEN)
        mock_typer_echo.assert_not_called()
        mock_sys_exit.assert_not_called()

    @patch("professional_python_exercises_2_githubcli.api.token.typer.echo", autospec=True)
    @patch("professional_python_exercises_2_githubcli.api.token.sys.exit")
    @patch("professional_python_exercises_2_githubcli.api.token.os.getenv")
    def test_get_github_token_no_env_set(
        self, mock_os_getenv: Mock, mock_sys_exit: Mock, mock_typer_echo: Mock
    ):
        mock_os_getenv.return_value = None

        get_github_token()

        mock_os_getenv.assert_called_once_with(ENV_GITHUB_TOKEN)
        mock_typer_echo.assert_called_once()
        mock_sys_exit.assert_called_once_with(1)
