# House Price Regression — Setup & Run

This project trains a linear regression model to predict house price from:
- square_feet
- bedrooms
- bathrooms

Prerequisites: Python 3.10+

Project structure
- data/house_prices.csv        # dataset (generated if missing)
- src/                         # package with training, model and utilities
  - __init__.py
  - utils.py
  - model.py
  - visualize.
  - train.py
- plots/                       # saved plots (created at runtime)
- requirements.txt
- .gitignore

Setup (Windows)
1. Open a terminal in the project root:
   C:\Users\Lokesh\Desktop\Task_01

2. Create and activate virtual environment

PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Command Prompt:
```cmd
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Run
From the project root run:
```bash
python -m src.train
```

What this does
- Generates dataset if missing
- Splits data (80/20)
- Trains LinearRegression using scikit-learn
- Prints coefficients, intercept, R² and MSE
- Shows and saves two plots to ./plots/: actual_vs_predicted.png and residuals.png

Example output (truncated)
```
Generated dataset: C:\Users\Lokesh\Desktop\Task_01\data\house_prices.csv (200 rows)
Linear Regression model trained.
Coefficients:
  square_feet: 145.0000
  bedrooms: 12000.0000
  bathrooms: 8500.0000
Intercept: 30000.0000
R² score: 0.9999
Mean Squared Error: 2134.5678
Saved plots to: C:\Users\Lokesh\Desktop\Task_01\plots\actual_vs_predicted.png and C:\Users\Lokesh\Desktop\Task_01\plots\residuals.png
```