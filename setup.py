from setuptools import find_packages, setup
from notify import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as fp:
    install_requires = fp.read()

setup(
    name="zyppnotify",
    version=__version__,
    author="Erfan Nariman, Melvin Folkers",
    author_email="erfan@zypp.io, melvin@zypp.io",
    description="Send users notifications through various platforms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="python, notifications, teams, e-mail",
    url="https://github.com/zypp-io/zyppnotify",
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    project_urls={
        "Bug Reports": "https://github.com/zypp-io/zyppnotify/issues",
        "Source": "https://github.com/zypp-io/zyppnotify",
    },
)
