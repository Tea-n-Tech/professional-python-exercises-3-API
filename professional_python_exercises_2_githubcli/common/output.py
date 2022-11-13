import enum
import sys

import typer


class OutputFormat(str, enum.Enum):
    """Enum defining allowed output types"""

    TEXT = "text"
    JSON = "json"


def print_output(
    obj: object,
    # pylint: disable=redefined-builtin
    format: OutputFormat,
):
    """Print the output object according to the formatting rule.
    For user output it prints to stdout otherwise stderr.

    Args:
        obj: Object to pring
        format: Format specified by the user
    """
    if format == OutputFormat.JSON:
        print(obj)
        return

    if format == OutputFormat.TEXT:
        typer.echo(obj)
        return

    typer.echo(f"Unknown output format '{format}'")
    sys.exit(1)
