import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def train_linear_regression(X_train: np.ndarray, y_train: np.ndarray) -> LinearRegression:
    """Train and return a LinearRegression model."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def evaluate_model(model: LinearRegression, X_test: np.ndarray, y_test: np.ndarray) -> dict:
    """Return predictions and common regression metrics."""
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    return {"y_pred": y_pred, "r2": r2, "mse": mse}