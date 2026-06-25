# River Water Level Forecasting – CM2420 Statistical Inference

**Name:** Ekanayake D.B  
**Index No:** 235514B  
**Module:** CM2420 Statistical Inference 

---

## Overview

This repository contains a complete regression analysis for the **River Water Level Forecasting Challenge** hosted as part of CM2420. The goal is to develop a statistical model that predicts river water levels **12 hours ahead** using current water level and 24-hour rainfall observations collected from gauging stations across Sri Lanka.

The dataset is derived from river monitoring data published by the Department of Irrigation, Sri Lanka, via the Disaster Management Centre (DMC), representing observations from major river basins during June 2026.

---

## Repository Structure

```
River_WaterLevel_Preliminary_Analysis/
│
├── River_WaterLevel_Task1&2_Full_Analysis.ipynb  ← Main analysis notebook (Tasks 1 & 2)
├── 235514B_River_WaterLevel_Preliminary_Analysis.ipynb  ← Preliminary EDA notebook
├── 235514B-River_WaterLevel_Preliminary_Analysis.html   ← Exported HTML of preliminary notebook
│
├── training_data.csv          ← Training dataset (78 gauging stations)
├── Assignment1.pdf            ← Original assignment specification
│
├── Lecture Slides/            ← CM2420 lecture materials (reference)
│   ├── Regression Analysis.pdf
│   ├── Multiple Linear Regression Analysis.pdf
│   └── ...
│
└── .gitignore
```

> **Note:** `test_data.csv` and `submission.csv` are excluded from version control (see `.gitignore`).  
> The test dataset will be released separately by the course instructor.

---

## Dataset Variables

| Variable | Description | Role |
|---|---|---|
| `Gauging_station` | Gauging station identifier | Identifier only (not a predictor) |
| `Water_Level_Xt_1` | River water level (mm) at time *t* | Predictor X₁ |
| `24HrRF_Xt_1` | Total rainfall (mm) in previous 24 hours at time *t* | Predictor X₂ |
| `Water_Level_Xt` | River water level (mm) at time *t* + 12 hours | **Target Y** |

**Training set:** 78 rows, 6 rows excluded (missing target) → **72 usable training observations**

---

## Methodology

### Task 1 – Model Development

The full analysis notebook (`River_WaterLevel_Task1&2_Full_Analysis.ipynb`) covers:

1. **Exploratory Data Analysis** – distributions, missing values, outlier inspection, correlation analysis
2. **Data Preprocessing** – remove rows with missing target, impute 2 missing rainfall values with the training median (15.65 mm)
3. **Univariate OLS Regression** – current water level as the sole predictor
4. **Multivariate OLS Regression** – current water level + 24-hour rainfall
5. **Model Diagnostics** – residuals vs fitted, Q-Q plot, Shapiro-Wilk test, Durbin-Watson, VIF
6. **Model Evaluation** – R², MSE, RMSE, MAE on training data
7. **Model Selection** – univariate model preferred on parsimony (AIC, BIC, adjusted R²)

### Final Model

$$\widehat{\text{Water Level}_{t+12h}} = -0.0467 + 0.9344 \times \text{Water Level}_{t}$$

| Metric | Value |
|---|---|
| R-squared | 0.980 |
| Adjusted R² | 0.980 |
| RMSE | 0.335 mm |
| MAE | 0.224 mm |
| MSE | 0.112 mm² |

### Task 2 – Generating Predictions

When `test_data.csv` is available, run the **Task 2** section of the main notebook to:
1. Load and inspect the test file
2. Apply identical preprocessing (impute missing rainfall with training median)
3. Generate predictions using the final univariate OLS model
4. Run automated sanity checks
5. Save `submission.csv` in the required format

**Required submission format:**
```
ID,Water_Level_Xt
1,1.234
2,0.876
...
```

---

## Key Findings

- The **current water level explains 98% of the variance** in the level 12 hours ahead (correlation ≈ 0.99). This reflects the physical persistence of river flow over short time horizons.
- **24-hour rainfall is not a statistically significant predictor** (p = 0.187) once the current level is included. Its effect is already embedded in the current water level.
- **VIF ≈ 1.13** confirms no multicollinearity between the two predictors.
- The residuals exhibit **mild heteroscedasticity** and **non-normality** (Shapiro-Wilk p < 0.001), consistent with the right-skewed nature of hydrological data. These are acknowledged limitations.
- The DW statistic (1.29) indicates some spatial autocorrelation between residuals of geographically nearby stations, which is expected in cross-sectional river data.

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

Open `River_WaterLevel_Task1&2_Full_Analysis.ipynb` in Jupyter and run:
- **Kernel → Restart & Run All** to execute everything cleanly from scratch.

### Generate the submission (Task 2)

1. Place `test_data.csv` in this directory.
2. Run the **Task 2** cells in the notebook.
3. Upload the generated `submission.csv` to the leaderboard.

---

## Evaluation Metric

Submissions are scored on **Mean Squared Error (MSE)**:

$$\text{MSE} = \frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)^2$$

Lower MSE = better performance.  
Training MSE of the final model: **0.112 mm²**

---

## License

This work is submitted as part of a university course assignment. The dataset is derived from publicly available data published by the Department of Irrigation, Sri Lanka.
