import typer
from typing import Optional
from pathlib import Path

app = typer.Typer()


@app.command('run')
def main(extension: str,
         directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel chercher"),
         delete: bool = typer.Option(False, help="Supprime les fichiers trouvés")):
    """
    Affiche les fichiers trouvés avec l'extension donnée
    """
    if directory:
        directory = Path(directory)
    else:
        directory = Path.cwd()

    if not directory.exists():
        typer.secho(f"Le fichier {directory} n'existe pas !", fg=typer.colors.RED)
        raise typer.Exit()

    files = directory.rglob(f"*.{extension}")

    if delete:
        typer.confirm("Voulez-vous vraiment supprimer tous les fichiers trouvés ?", abort=True)
        for file in files:
            file.unlink()
            typer.secho(f"Suppression du fichier {extension}.", fg=typer.colors.RED)

    else:
        typer.secho(f"Fichier trouvés l'extension {extension}:", fg=typer.colors.CYAN)
        for file in files:
            typer.echo(file)


@app.command('search')
def search(extension: str):
    main(extension=extension, directory=None, delete=False)


@app.command('delete')
def delete(extension: str):
    main(extension=extension, directory=None, delete=True)


if __name__ == "__main__":
    typer.run(main)
