from pathlib import Path

from sklearn.model_selection import train_test_split

from src.utils import ensure_dirs, load_data, get_feature_target, PLOTS_DIR
from src.model import train_linear_regression, evaluate_model
from src.visualize import plot_actual_vs_predicted, plot_residuals


def main():
    ensure_dirs()

    # Load data (will generate if missing)
    df = load_data()

    # Prepare features and target
    X, y = get_feature_target(df)
    feature_names = ["square_feet", "bedrooms", "bathrooms"]

    # Train / test split (80/20)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = train_linear_regression(X_train, y_train)

    # Print coefficients and intercept
    coefs = model.coef_
    intercept = model.intercept_
    print("Linear Regression model trained.")
    print("Coefficients:")
    for name, coef in zip(feature_names, coefs):
        print(f"  {name}: {coef:.4f}")
    print(f"Intercept: {intercept:.4f}")

    # Evaluate
    results = evaluate_model(model, X_test, y_test)
    y_pred = results["y_pred"]
    r2 = results["r2"]
    mse = results["mse"]

    print(f"R² score: {r2:.4f}")
    print(f"Mean Squared Error: {mse:.4f}")

    # Ensure plots dir exists and save plots
    project_root = Path(__file__).resolve().parents[1]
    plots_dir = project_root / "plots"
    plots_dir.mkdir(exist_ok=True)

    avp_path = plots_dir / "actual_vs_predicted.png"
    resid_path = plots_dir / "residuals.png"

    plot_actual_vs_predicted(y_test, y_pred, avp_path)
    plot_residuals(y_test, y_pred, resid_path)

    print(f"Saved plots to: {avp_path} and {resid_path}")


if __name__ == "__main__":
    main()