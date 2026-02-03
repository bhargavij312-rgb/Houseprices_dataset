<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>House Prices - Advanced Regression Techniques</title>

  <style>
    body {
      font-family: "Segoe UI", Arial, sans-serif;
      background: #f4f6f8;
      margin: 0;
      padding: 0;
      color: #333;
    }

    .container {
      max-width: 900px;
      margin: 40px auto;
      background: #ffffff;
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    }

    h1 {
      text-align: center;
      color: #2c3e50;
      margin-bottom: 10px;
    }

    h2 {
      color: #34495e;
      margin-top: 30px;
      border-left: 5px solid #3498db;
      padding-left: 10px;
    }

    p {
      line-height: 1.7;
      font-size: 16px;
    }

    ul {
      margin-top: 10px;
      padding-left: 20px;
    }

    li {
      margin-bottom: 8px;
    }

    .badge {
      display: inline-block;
      background: #3498db;
      color: #fff;
      padding: 6px 12px;
      border-radius: 20px;
      font-size: 14px;
      margin-right: 8px;
      margin-top: 8px;
    }

    .footer {
      text-align: center;
      margin-top: 40px;
      font-size: 14px;
      color: #777;
    }

    button {
      margin-top: 20px;
      padding: 10px 18px;
      border: none;
      border-radius: 6px;
      background: #2ecc71;
      color: white;
      font-size: 15px;
      cursor: pointer;
    }

    button:hover {
      background: #27ae60;
    }

    .highlight {
      background: #ecf6ff;
      padding: 15px;
      border-radius: 8px;
      margin-top: 15px;
    }
  </style>
</head>

<body>
  <div class="container">

    <h1>🏠 House Prices – Advanced Regression Techniques</h1>
    <p style="text-align:center;">
      A machine learning regression project based on the Ames Housing dataset
    </p>

    <div style="text-align:center;">
      <span class="badge">Machine Learning</span>
      <span class="badge">Regression</span>
      <span class="badge">Python</span>
      <span class="badge">Kaggle</span>
    </div>

    <h2>📌 Project Overview</h2>
    <p>
      This project aims to predict house sale prices using advanced regression
      techniques. The dataset contains detailed information about residential
      homes, including structural features, location, quality, and condition.
    </p>

    <h2>📊 Dataset</h2>
    <ul>
      <li>Ames Housing Dataset</li>
      <li>79 explanatory variables</li>
      <li>Combination of numerical and categorical features</li>
    </ul>

    <h2>⚙️ Methodology</h2>
    <ul>
      <li>Data cleaning and missing value handling</li>
      <li>Feature engineering and encoding</li>
      <li>Log transformation of the target variable</li>
      <li>Model training and cross-validation</li>
    </ul>

    <h2>🤖 Models Used</h2>
    <ul>
      <li>Linear Regression</li>
      <li>Ridge & Lasso Regression</li>
      <li>ElasticNet</li>
      <li>Ensemble-based models</li>
    </ul>

    <h2>📈 Evaluation Metric</h2>
    <div class="highlight">
      <p>
        Root Mean Squared Error (RMSE) on the logarithmic scale of house prices
        is used to evaluate model performance.
      </p>
    </div>

    <h2>🚀 Outcome</h2>
    <p>
      The final model successfully predicts house prices for unseen data,
      demonstrating effective application of machine learning techniques
      for real-world regression problems.
    </p>

    <button onclick="showMessage()">Click for Project Tip</button>

    <p id="tip" style="font-weight:bold; margin-top:15px;"></p>

    <div class="footer">
      <p>Created by Bhargavi • AI & ML Enthusiast 🤍</p>
    </div>

  </div>

  <script>
    function showMessage() {
      document.getElementById("tip").innerText =
        "💡 Tip: Feature engineering and log transformation significantly improve regression accuracy!";
    }
  </script>
</body>
</html>
