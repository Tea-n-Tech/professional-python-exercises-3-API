import typer
from .stars import stars_cmd
from .status import status_cmd
from .user import user_cmd
from .api import api_cmd

app = typer.Typer(no_args_is_help=True)
app.add_typer(stars_cmd)
app.add_typer(user_cmd)
app.add_typer(status_cmd)
app.add_typer(api_cmd)
