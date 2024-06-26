import os
import sys
import typer


def main(python_file: str = typer.prompt("Enter the path to your Python file")):
    """
    Create a bat file to run the specified Python script on Windows.
    """
    absolute_path = os.path.abspath(python_file)
    file_name = os.path.splitext(os.path.basename(python_file))[0]
    bat_file = f"{file_name}.bat"
    python_interpreter_path = sys.executable

    # Write the bat file
    with open(bat_file, "w") as f:
        f.write(f'@echo off\n')
        f.write(f'"{python_interpreter_path}" "{absolute_path}"\n')
        f.write('pause\n')

    typer.echo(f"Bat file '{bat_file}' has been created successfully.")


if __name__ == "__main__":
    typer.run(main)
