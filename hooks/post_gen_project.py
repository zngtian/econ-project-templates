"""Hooks which are executed after the template is rendered."""
from __future__ import annotations

import shutil
import subprocess
import warnings
from contextlib import suppress
from pathlib import Path


def remove_file(*filepath: str | Path) -> None:
    """Remove a file."""
    with suppress(FileNotFoundError):
        Path(*filepath).unlink()


def remove_directory(*filepath: str | Path) -> None:
    """Remove a directory."""
    with suppress(FileNotFoundError):
        path = Path(*filepath)
        shutil.rmtree(path)


def main() -> None:
    """Apply post generation hooks."""
    project_path = Path.cwd()

    if "{{ cookiecutter.create_changelog }}" == "no":
        remove_file(project_path, "CHANGES.md")

    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_file(project_path, "LICENSE")

    if "{{ cookiecutter.add_github_actions }}" == "no":
        remove_directory(project_path, ".github", "workflows")
        remove_file(project_path, "codecov.yml")

    if "{{ cookiecutter.add_python_example }}" == "no":
        keep = ["__init__", "task_", "config"]
        python_files = project_path.rglob("*.py")
        for file in python_files:
            if all(k not in file.name for k in keep):
                remove_file(file)

    if "{{ cookiecutter.add_julia_example }}" == "no":
        julia_files = project_path.rglob("*.jl")
        for file in julia_files:
            remove_file(file)

    if "{{ cookiecutter.add_r_example }}" == "no":
        r_files = project_path.rglob("*.r")
        for file in r_files:
            remove_file(file)

    if "{{ cookiecutter.add_stata_example }}" == "no":
        stata_files = project_path.rglob("*.do")
        for file in stata_files:
            remove_file(file)

    subprocess.run(
        ("git", "init", "--initial-branch", "main"),
        check=True,
        capture_output=True,
    )

    if "{{ cookiecutter.git_remote_url }}":
        subprocess.call(
            ["git", "remote", "add", "origin", "{{ cookiecutter.git_remote_url }}"],
        )

    if "{{ cookiecutter.make_initial_commit }}" == "yes":
        # Create an initial commit on the main branch and restore global default name.
        subprocess.run(
            ("git", "config", "user.name", "'{{ cookiecutter.github_username }}'"),
            check=True,
        )
        subprocess.run(
            ("git", "config", "user.email", "'{{ cookiecutter.github_email }}'"),
            check=True,
        )
        subprocess.run(("git", "add", "."), check=True)
        subprocess.run(
            ("git", "commit", "-m", "'Initial commit.'"),
            check=True,
            capture_output=True,
        )

    if "{{ cookiecutter.create_conda_environment_at_finish }}" == "yes":
        if _mamba := shutil.which("mamba"):
            conda_exe = _mamba
        else:
            conda_exe = shutil.which("conda")

        if conda_exe:
            subprocess.run(
                (
                    conda_exe,
                    "env",
                    "create",
                    "-f",
                    (project_path / "environment.yml").absolute().as_posix(),
                    "--force",
                ),
                check=True,
                capture_output=True,
            )
        else:
            warnings.warn(
                "conda environment could not be created since no conda or mamba "
                "executable was found.",
                stacklevel=2,
            )


if __name__ == "__main__":
    main()
