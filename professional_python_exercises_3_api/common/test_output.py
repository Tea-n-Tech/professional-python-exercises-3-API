import unittest
from unittest.mock import Mock, patch

from .output import print_output, OutputFormat


class TestOutput(unittest.TestCase):
    @patch("professional_python_exercises_3_api.common.output.sys.exit")
    @patch("professional_python_exercises_3_api.common.output.typer.echo", autospec=True)
    @patch("builtins.print")
    def test_print_output_json(self, mock_print: Mock, mock_typer_echo: Mock, mock_sys_exit: Mock):
        msg = "yay"

        print_output(msg, OutputFormat.JSON)

        mock_print.assert_called_once_with(msg)
        mock_typer_echo.assert_not_called()
        mock_sys_exit.assert_not_called()

    @patch("professional_python_exercises_3_api.common.output.sys.exit")
    @patch("professional_python_exercises_3_api.common.output.typer.echo", autospec=True)
    @patch("builtins.print")
    def test_print_output_text(self, mock_print: Mock, mock_typer_echo: Mock, mock_sys_exit: Mock):
        msg = "yay"

        print_output(msg, OutputFormat.TEXT)

        mock_print.assert_not_called()
        mock_typer_echo.assert_called_once_with(msg)
        mock_sys_exit.assert_not_called()

    @patch("professional_python_exercises_3_api.common.output.sys.exit")
    @patch("professional_python_exercises_3_api.common.output.typer.echo", autospec=True)
    @patch("builtins.print")
    def test_print_output_unknown_format(
        self, mock_print: Mock, mock_typer_echo: Mock, mock_sys_exit: Mock
    ):
        msg = "yay"

        print_output(msg, "Unknown")

        mock_print.assert_not_called()
        mock_typer_echo.assert_called_once_with("Unknown output format 'Unknown'")
        mock_sys_exit.assert_called_once_with(1)
