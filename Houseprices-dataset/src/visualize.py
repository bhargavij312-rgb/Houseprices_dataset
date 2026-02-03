from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from src.utils import PLOTS_DIR


def plot_actual_vs_predicted(y_true: np.ndarray, y_pred: np.ndarray, save_path: Path):
    """Scatter plot: actual vs predicted with y=x reference line."""
    plt.figure(figsize=(8, 6))
    plt.scatter(y_true, y_pred, c="tab:blue", alpha=0.6, edgecolors="k")
    min_val = min(np.min(y_true), np.min(y_pred))
    max_val = max(np.max(y_true), np.max(y_pred))
    plt.plot([min_val, max_val], [min_val, max_val], "r--", label="Ideal (y = x)")
    plt.xlabel("Actual Price")
    plt.ylabel("Predicted Price")
    plt.title("Actual vs Predicted House Prices")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()


def plot_residuals(y_true: np.ndarray, y_pred: np.ndarray, save_path: Path):
    """Residuals vs predicted values."""
    residuals = y_true - y_pred
    plt.figure(figsize=(8, 6))
    plt.scatter(y_pred, residuals, c="tab:green", alpha=0.6, edgecolors="k")
    plt.axhline(0, color="r", linestyle="--")
    plt.xlabel("Predicted Price")
    plt.ylabel("Residual (Actual - Predicted)")
    plt.title("Residuals vs Predicted Prices")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()