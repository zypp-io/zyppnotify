import os

from notify import NotifyTeams
from notify.tests import import_sample_dfs


def test_teams_basic_message():
    """
    versturen van een simpel teams bericht
    """
    teams = NotifyTeams(webhook=os.environ.get("teams_webhook"))
    teams.basic_message(title="Pytest", message="This is a simple message, send with notify")


def test_teams_with_dfs():
    """
    versturen van een uitgebreid rapport over dataframes.
    inclusief buttons.
    """

    dfs = import_sample_dfs()
    # set dataframes to shapes
    dfs = {name: df.shape for name, df in dfs.items()}
    teams = NotifyTeams(webhook=os.environ.get("teams_webhook"))
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


def test_teams_with_df():
    """
    versturen van een uitgebreid rapport over dataframes.
    inclusief buttons.
    """

    df = import_sample_dfs().get("Transactions")

    teams = NotifyTeams(webhook=os.environ.get("teams_webhook"))
    teams.basic_message(
        title="Pytest with 1 dataframe",
        subtitle="With a subtitle",
        message="This is an test message, send with notify AC",
        warning_message="Own warning message",
        buttons={"button 1": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"},
        df=df,
    )  # adds the dataframe to the message as a table


def test_teams_with_extra():
    """
    Verstuur bericht inclusief extra element
    """

    df = import_sample_dfs().get("Transactions")

    teams = NotifyTeams(webhook=os.environ.get("teams_webhook"))
    extra_item = {"type": "TextBlock", "color": "good", "text": "This is extra text in green", "wrap": "true"}
    teams.basic_message(
        title="Pytest with extra element",
        subtitle="With a subtitle",
        message="This is a test message, send with notify AC",
        df=df,
        extra=[{"index": 3, "item": extra_item}],
    )  # adds the dataframe to the message as a table


if __name__ == "__main__":
    test_teams_with_df()
