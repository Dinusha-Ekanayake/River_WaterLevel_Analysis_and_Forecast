# River Water Level Forecasting

**Name:** Ekanayake D.B  
**Index No:** 235514B  
**Module:** CM2420 Statistical Inference 

---

## Overview

This repository contains a complete regression analysis for the **River Water Level Forecasting Challenge** hosted as part of CM2420 course module. The goal is to develop a statistical model that predicts river water levels **12 hours ahead** using current water level and 24 hour rainfall observations collected from gauging stations across Sri Lanka.

The dataset is derived from river monitoring data published by the Department of Irrigation, Sri Lanka, via the Disaster Management Centre (DMC), representing observations from major river basins during June 2026.

---

## Repository Structure

```
River_WaterLevel_Preliminary_Analysis/
│
├── River_WaterLevel_Analysis_&_Forecasting.ipynb   ← Full analysis notebook (Task 1 & 2)
├── River_WaterLevel_Analysis_&_Forecasting.html    ← Exported HTML of the notebook
├── requirements.txt           ← Python dependencies
├── training_data.csv          ← Training dataset (78 gauging stations)
├── test_data.csv              ← Test dataset for Task 2 predictions
├── submission.csv             ← Generated forecast submission
├── README.md                  ← Project documentation
|
└── .gitignore                 ← Git ignore file
```

---

## Dataset Variables

| Variable | Description | Role |
|---|---|---|
| `Gauging_station` | Gauging station identifier | Identifier only (not a predictor) |
| `Water_Level_Xt_1` | River water level (mm) at time *t* | Predictor X₁ |
| `24HrRF_Xt_1` | Total rainfall (mm) in previous 24 hours at time *t* | Predictor X₂ |
| `Water_Level_Xt` | River water level (mm) at time *t* + 12 hours | **Target Y** |

**Training set:** 78 rows, 8 rows excluded (listwise deletion) → **70 usable training observations**

---

## Methodology

### Task 1 – Model Development

The full analysis notebook (`River_WaterLevel_Analysis_&_Forecasting.ipynb`) covers:

1. **Exploratory Data Analysis** – distributions, missing values, outlier inspection, correlation analysis
2. **Data Preprocessing** – listwise deletion of all rows with any missing value (6 missing target + 2 missing rainfall = 8 rows removed)
3. **Univariate OLS Regression** – current water level as the sole predictor
4. **Multivariate OLS Regression** – current water level + 24-hour rainfall
5. **Model Diagnostics** – residuals vs fitted, Q-Q plot, Shapiro-Wilk test, Durbin-Watson, VIF
6. **Model Evaluation** – R², MSE, RMSE, MAE on training data
7. **Model Selection** – univariate model preferred on parsimony (AIC, BIC, adjusted R²)

### Final Model

$$\widehat{\text{Water Level}_{t+12h}} = -0.0305 + 0.9358 \times \text{Water Level}_{t}$$

| Metric | Value |
|---|---|
| R-squared | 0.9834 |
| Adjusted R² | 0.9831 |
| RMSE | 0.3082 mm |
| MAE | 0.2074 mm |
| MSE | 0.0950 mm² |

### Task 2 – Generating Predictions

The same model that achieved an **R² of 0.983** on the training set is applied to the test data. 
Key preprocessing steps applied to the test set to avoid data leakage include:
- `Gauging_station` is used only as an identifier and is not a predictor.
- Missing `24HrRF_Xt_1` values are imputed with the **training median (15.65 mm)** (although rainfall is ultimately not used in the final univariate model, it ensures the dataset structure remains consistent).
- No rows are removed from the test set, ensuring a forecast is generated for every row.

**Output format:**
```
ID,Water_Level_Xt
1,1.234
2,0.876
...
```

---

## Key Findings & Insights

- **High Predictiveness**: The **current water level alone explains 98.3% of the variance** in the level 12 hours ahead (correlation ≈ 0.99). This reflects the physical persistence of river flow over short time horizons.
- **Rainfall Insignificance**: **24-hour rainfall is not a statistically significant predictor** (p = 0.187) once the current water level is included. Its effect is likely already embedded in the current water level.
- **No Multicollinearity**: **VIF ≈ 1.13** confirms there is no concerning multicollinearity between the predictors.

## Practical Usefulness

In the context of flood early warning and river management, this model provides:
- **Early Warning Lead Time**: A reliable 12-hour forecast gives authorities sufficient time to issue warnings and evacuate low-lying areas.
- **Simplicity & Robustness**: The model relies on a single telemetered input (current water level), reducing dependency on potentially uncertain rainfall forecasts.
- **Interpretability**: The physical interpretation is clear—the river level 12 hours later is roughly 0.94 times the current level minus a small constant.

## Strengths and Limitations

### Strengths
- **Low Input Data Requirement**: Only the current water level is required at forecast time.
- **Avoids Overfitting**: A single-predictor linear model has no tuning parameters, significantly reducing the risk of overfitting (high variance) compared to complex machine learning models on a small dataset.

### Limitations
- **Heteroscedasticity**: Residual spread increases at higher water levels; the model is slightly less precise for large river stations.
- **Small Cross-Sectional Sample**: With only 70 training observations, the model relies on a cross-sectional snapshot rather than capturing true temporal dynamics (e.g., seasonality or long-term trends).
- **Linear Assumption**: Assumes a linear relationship. During extreme flood events (bank overflow, backwater effects), river dynamics become non-linear.

---

## How to Run

### Requirements

You can install all dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Or activate the project virtual environment:
```bash
# PowerShell
.\.venv\Scripts\Activate.ps1

# Command Prompt
.venv\Scripts\activate
```

### Run the notebook

Open `River_WaterLevel_Analysis_&_Forecasting.ipynb` in Jupyter and run:
- **Kernel → Restart & Run All** to execute everything cleanly from scratch.

### Generate the submission (Task 2)

1. Place `test_data.csv` in this directory.
2. Run the **Task 2** cells in the notebook.
3. Upload the generated `submission.csv` to the leaderboard.

---

## Evaluation Metric

Scored on **Mean Squared Error (MSE)**:

$$\text{MSE} = \frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)^2$$

Lower MSE = better performance.  
Training MSE of the final model: **0.0950 mm²**

---

## License

This work is submitted as part of a university course assignment. The dataset is derived from publicly available data published by the Department of Irrigation, Sri Lanka.
