from venv import create
from os.path import join, abspath
from subprocess import run
import sys

use_uv = True

def create_venv(path: str = ".venv", path_to_requirements_txt: str = None) -> None:
    create(path, with_pip=True)

    if path_to_requirements_txt is None:
        return

    pip_executable = "uv pip" if use_uv else f"{sys.executable} -m pip"

    print(f". {join(path, 'bin', 'activate')} && {pip_executable} install -r {path_to_requirements_txt}")
    run(f". {join(path, 'bin', 'activate')} && {pip_executable} install -r {path_to_requirements_txt}", start_new_session=True, shell=True)
