import logging

import pandas as pd
from zenml import step


class IngestData:
    """
    Ingest data from a given path.
    """
    def __init__(self, data_path: str):
        """
        Constructor for IngestData.

        Args:
            data_path: Path to the data.
        """
        self.data_path = data_path

    def get_data():
        """
        Get the data from the data path.

        Returns:
            pd.DataFrame: Dataframe containing the data.
        """
        logging.info(f"Reading data from {self.data_path}")
        return pd.read_csv(self.data_path)


@step
def ingest_data(data_path: str) -> pd.DataFrame:
    """
    Ingest data from a given path.

    Args:
        data_path: Path to the data.

    Returns:
        pd.DataFrame: Dataframe containing the data.
    """
    return IngestData(data_path).get_data()
