import os
from notify import NotifyTeams
import pandas as pd
import numpy as np
from keyvault import secrets_to_environment

secrets_to_environment("notify")
teams = NotifyTeams(webhook=os.environ.get("teams_webhook"))


def import_sample_dfs():
    stamdata = pd.DataFrame(
        [
            {"naam": "Melvin", "geb_datum": "12-03-1991", "telefoon": "0652652852"},
            {"naam": "Erfan ", "geb_datum": "02-07-1991", "telefoon": "0652652852"},
            {"naam": "Alejandra", "geb_datum": "01-07-1990", "telefoon": "0652652852"},
        ]
    )

    transacties = pd.DataFrame(
        {
            "2018-01": np.random.randint(1000, 10000, 5),
            "2018-03": np.random.randint(1000, 10000, 5),
            "2018-04": np.random.randint(1000, 10000, 5),
            "2019-02": np.random.randint(1000, 10000, 5),
            "2019-08": np.random.randint(1000, 10000, 5),
            "2020-05": np.random.randint(1000, 10000, 5),
            "2020-11": np.random.randint(1000, 10000, 5),
            "2020-12": np.random.randint(1000, 10000, 5),
        }
    )

    dfs = {"stamdata": stamdata, "transacties": transacties}

    return dfs


def test_teams_basic_message():
    """
    versturen van een simpel teams bericht
    """

    teams.basic_message(title="Pytest", message="This is a simple message, send with notify")


def test_teams_with_dfs():
    """
    versturen van een uitgebreid rapport over dataframes.
    inclusief buttons.
    """

    dfs = import_sample_dfs()
    teams.basic_message(
        title="Pytest",
        message=(
            "This is an extended message, send with notify.<br>"
            "This message has nice buttons.<br>"
            "And gives information about dataframes."
        ),
        buttons={
            "button 1": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "button 2": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "button 3": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        },
        dfs=dfs,
    )  # creates a report on the dataframes processed.


if __name__ == "__main__":
    test_teams_with_dfs()
