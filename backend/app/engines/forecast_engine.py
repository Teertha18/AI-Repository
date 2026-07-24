"""
Forecast Engine

Generic forecasting engine that predicts the
next N values for any numeric metric.
"""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


class ForecastEngine:

    @staticmethod
    def predict(
        dataframe: pd.DataFrame,
        column: str,
        days: int = 30,
    ):
        """
        Predict future values for any numeric column.
        """

        values = dataframe[column].values

        x = np.arange(len(values)).reshape(-1, 1)
        y = values

        model = LinearRegression()
        model.fit(x, y)

        future_x = np.arange(
            len(values),
            len(values) + days
        ).reshape(-1, 1)

        predictions = model.predict(future_x)

        return predictions.tolist()