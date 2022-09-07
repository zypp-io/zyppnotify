import numpy as np
import pandas as pd

PDF_STORAGE_LINK = (
    "https://zyppsandboxstorage.blob.core.windows.net/sandbox/Notify/NotifySample.pdf"
    "?sv=2021-04-10&st=2022-09-07T09%3A40%3A55Z&se=2025-01-01T10%3A40%3A00Z&sr=b&sp=r&sig="
    "EQkqHZ7FI%2B%2FnD3C4Uo97l614hPtycKp%2BA1odhsvkprI%3D"
)


def import_sample_dfs(transactions: int = 7):
    """

    Parameters
    ----------
    transactions: int
        number of transactions to generate.

    Returns
    -------

    """
    df1 = pd.DataFrame({"numbers": [1, 2, 3], "colors": ["red", "white", "blue"]})

    transactions = transactions

    df2 = pd.DataFrame(index=range(transactions))
    df2["amount"] = [np.random.randint(1000, 10000) for x in range(transactions)]
    df2["date"] = [
        (pd.to_datetime("now") - pd.Timedelta(value=x, unit="days")).strftime("%Y-%m-%d") for x in range(transactions)
    ]

    dfs = {"Metadata": df1, "Transactions": df2}

    return dfs
