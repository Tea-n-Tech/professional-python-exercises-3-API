import enum
import sys

import typer


class OutputFormat(str, enum.Enum):
    """Enum defining allowed output types"""

    text = "text"
    json = "json"


def print_output(obj: object, format: OutputFormat):
    if format == OutputFormat.json:
        print(obj)
        return

    if format == OutputFormat.text:
        typer.echo(obj)
        return

    typer.echo(f"Unknown output format '{format}'")
    sys.exit(1)
