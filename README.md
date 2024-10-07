<div style="text-align:center"><img alt="logo" src="https://www.zypp.io/static/assets/img/logos/zypp/white/500px.png" width="200"></div>
<br>

[![Downloads](https://pepy.tech/badge/zyppnotify)](https://pepy.tech/project/zyppnotify)
[![PyPI version](https://badge.fury.io/py/zyppnotify.svg)](https://badge.fury.io/py/zyppnotify)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

Notify
===
> Sending mails and teams messages in a smart way. This project makes it easy to send basic messages through Teams or Email.

# Installation

---

```commandline
pip install zyppnotify
```

## Notify Mail
When using the `NotifyMail` class, the environment variables `EMAIL_USER` (mailadress you want to mail with), `MAIL_TENANT_ID`, `MAIL_CLIENT_ID` and `MAIL_CLIENT_SECRET` (3x App registration credentials with User.Read.All permission with admin consent to authenticate to MS Graph) need to be set.
The initialization of this class will return an error if one of thes variables is not set.

```python
from notify import NotifyMail, NotifyTeams

# versturen van een basis bericht met onderwerp en tekst
mail = NotifyMail(to="reveiver@domain.com",
                  subject="Notify me!",
                  message="This is a test message, send through the notify package")

mail.send_email()
```

## Notify Teams
For the Notify for Teams (1.0.0) you can create a webhook as by following the steps in the [Microsoft documentation](https://support.microsoft.com/en-us/office/create-incoming-webhooks-with-workflows-for-microsoft-teams-8ae491c7-0394-4861-ba59-055e33f75498).

Requirement: Add member that sends the message to the channel

In the workflow app, make sure the message is sent as user, and not as Flowbot.
```python
from notify import NotifyTeams
from notify.tests import import_sample_dfs

webhook = ("REPLACE_ME")

teams = NotifyTeams(webhook=webhook)

# versturen van een basis bericht met onderwerp en tekst
teams.basic_message(title="Notify me!",
                    message="This is a test message, send through the notify package")

# versturen van een uitgebreid rapport over dataframes.
dfs = import_sample_dfs()
teams.basic_message(title="Notify me!",
                    message="This is optional",
                    buttons={"button_name": "https://www.my_link.nl"},
                    dfs=dfs) #  creates a report on the dataframes processed.
```
 ### Add extra elements to Teams message
With the parameter `extra` the user can add adaptive cards elements to the message. The `extra` parameter should be a
list of dictionaries. The dictionaries should contain the keys `index` and `item`. The `index` key should be an integer
and the `item` key should be a dictionary containing the adaptive card element. The `index` key determines the location
in the message.

```python
from notify import NotifyTeams

webhook = ("REPLACE_ME")

teams = NotifyTeams(webhook=webhook)

extra_item = {"type": "TextBlock", "color": "good", "text": "This is extra text in green", "wrap": "true"}
teams.basic_message(title="Notify me!",
                    message="This is optional",
                    buttons={"button_name": "https://www.my_link.nl"},
                    extra=[{"index": 3, "item": extra_item}]) #  creates a report on the dataframes processed.
```

With the method `create_adaptive_card_dataframe(df)` you can create an Adaptive Card dataframe to be added as an extra element.
```python
from notify import NotifyTeams
from notify.tests import import_sample_dfs

webhook = ("REPLACE_ME")

teams = NotifyTeams(webhook=webhook)
df = import_sample_dfs().get("Transactions")
extra_df = teams.create_adaptive_card_dataframe(df)
teams.basic_message(title="Notify me!",
                    message="This is optional",
                    buttons={"button_name": "https://www.my_link.nl"},
                    extra=[{"index": 3, "item": extra_df}]) #  creates a report on the dataframes processed.
```

## Notify utils
```python
from notify import format_numbers, dataframe_to_html
from notify.tests import import_sample_dfs

df = import_sample_dfs().get("Transactions")

# format numbers and currencies using dutch locale
df = format_numbers(df, currency_columns=["amount"], number_columns=[])
html_table = dataframe_to_html(df)
```
