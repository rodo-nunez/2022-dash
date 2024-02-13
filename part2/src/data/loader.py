import pandas as pd

def load_transaction_data(path: str) -> pd.DataFrame:
    # load the data from the CSV file
    data = pd.read_csv(
        path,
        dtype={
            "amount": float,
            "category": str,
        },
        parse_dates=["date"],
    )

    return data
