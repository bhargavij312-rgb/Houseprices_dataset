from pathlib import Path
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
DATA_FILE = DATA_DIR / "house_prices.csv"
PLOTS_DIR = PROJECT_ROOT / "plots"


def ensure_dirs():
    """Create data and plots directories if they do not exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)


def generate_dataset_if_missing(seed: int = 42, rows: int = 200):
    """
    Generate a realistic synthetic house prices dataset if data/house_prices.csv is missing.

    Columns: square_feet, bedrooms, bathrooms, price
    """
    if DATA_FILE.exists():
        return

    np.random.seed(seed)

    # Realistic ranges
    square_feet = np.linspace(600, 2600, rows).astype(int)  # 600 - 2600 sqft
    bedrooms = (np.arange(rows) % 5) + 1  # 1..5 bedrooms repeating
    bath_cycle = np.array([1.0, 1.5, 2.0, 2.5, 3.0])
    bathrooms = bath_cycle[np.arange(rows) % bath_cycle.size]

    # Deterministic price model + minor periodic noise for realism
    base = 30000
    price_per_sqft = 145
    bedroom_value = 12000
    bathroom_value = 8500

    price = (
        base
        + square_feet * price_per_sqft
        + bedrooms * bedroom_value
        + bathrooms * bathroom_value
    )

    noise = ((np.arange(rows) * 37) % 1000) - 500  # small bounded pattern noise
    price = price + noise

    df = pd.DataFrame(
        {
            "square_feet": square_feet,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "price": price.astype(int),
        }
    )

    df.to_csv(DATA_FILE, index=False)
    print(f"Generated dataset: {DATA_FILE} ({rows} rows)")


def load_data(path: Path = None):
    """
    Load dataset from CSV. If missing, generate a dataset.
    Returns pandas DataFrame.
    """
    ensure_dirs()
    if path is None:
        path = DATA_FILE

    if not path.exists():
        generate_dataset_if_missing()

    df = pd.read_csv(path)
    # coerce dtypes
    df["square_feet"] = df["square_feet"].astype(float)
    df["bedrooms"] = df["bedrooms"].astype(float)
    df["bathrooms"] = df["bathrooms"].astype(float)
    df["price"] = df["price"].astype(float)
    return df


def get_feature_target(df):
    """Return feature matrix X and target vector y."""
    X = df[["square_feet", "bedrooms", "bathrooms"]].values
    y = df["price"].values
    return X, y