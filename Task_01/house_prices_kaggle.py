import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load dataset
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")  # optional if you want to predict on test set later

# Pick features for simplicity (you can choose more later)
features = ["GrLivArea", "BedroomAbvGr", "FullBath"]
train = train[features + ["SalePrice"]].dropna()

X = train[features]
y = train["SalePrice"]

# Split data for training/testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Coefficients:", dict(zip(features, model.coef_)))
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# Plot Actual vs Predicted
plt.scatter(y_test, y_pred)
plt.xlabel("Actual SalePrice")
plt.ylabel("Predicted SalePrice")
plt.title("Actual vs Predicted SalePrice")
plt.show()
