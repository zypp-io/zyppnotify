class EnvironmentVariablesError(Exception):
    """Exception when not all env variables are set"""

    pass


class DataFrameTooLarge(Exception):
    """Exception when the dataframe is too large to be readable in the notification"""

    pass
