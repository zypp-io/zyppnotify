import os
import pathlib

from setuptools.config import read_configuration

from notify import __version__


def get_config():
    repo_path = pathlib.Path(__file__).parent.parent.absolute()
    config_setup = read_configuration(os.path.join(repo_path, "setup.cfg"))

    return config_setup, repo_path


def check_requirements():
    config_setup, repo_path = get_config()
    config_requirements = config_setup["options"]["install_requires"]

    with open(os.path.join(repo_path, "requirements.txt")) as f:
        requirements_txt = f.read().splitlines()

    assert sorted(config_requirements) == sorted(requirements_txt), "Requirements are not equal"
    print("Requirements and setup.cfg and both are equal")


def check_version():
    config_setup, repo_path = get_config()
    config_version = config_setup["metadata"]["version"]

    assert config_version == __version__, "Versions are not equal"
    print(f"Version in setup.py and __init__.py are equal: {__version__}")


if __name__ == "__main__":
    check_requirements()
    check_version()
