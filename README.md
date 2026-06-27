# 🌊 River Water Level Forecasting

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![Regression](https://img.shields.io/badge/Model-OLS_Regression-brightgreen.svg)
![License](https://img.shields.io/badge/License-Academic-blueviolet.svg)

> **Module:** CM2420 Statistical Inference  
> **Student Name:** Ekanayake D.B  
> **Index No:** 235514B  

---

## 📖 Table of Contents
- [Overview](#-overview)
- [Repository Structure](#-repository-structure)
- [Dataset Variables](#-dataset-variables)
- [Methodology](#-methodology)
  - [Task 1: Model Development](#task-1-model-development)
  - [Task 2: Generating Predictions](#task-2-generating-predictions)
- [Key Findings & Insights](#-key-findings--insights)
- [Strengths & Limitations](#-strengths--limitations)
- [Getting Started](#-getting-started)
- [Evaluation](#-evaluation)
- [License](#-license)

---

## 🎯 Overview

This repository contains a complete regression analysis for the **River Water Level Forecasting Challenge**, hosted as part of the CM2420 course module. The core objective is to develop a statistical model capable of predicting river water levels **12 hours ahead**. 

The predictions rely on the current water level and 24-hour rainfall observations collected from gauging stations across Sri Lanka. The dataset is derived from river monitoring data published by the **Department of Irrigation, Sri Lanka**, via the Disaster Management Centre (DMC), representing observations from major river basins during June 2026.

---

## 📂 Repository Structure

```text
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

## 📊 Dataset Variables

| Variable | Description | Role |
|:---|:---|:---|
| `Gauging_station` | Gauging station identifier | Identifier only (not a predictor) |
| `Water_Level_Xt_1` | River water level (mm) at time *t* | **Predictor X₁** |
| `24HrRF_Xt_1` | Total rainfall (mm) in previous 24 hours at time *t* | **Predictor X₂** |
| `Water_Level_Xt` | River water level (mm) at time *t* + 12 hours | **Target Y** |

> **Note on Training set:** Initially 78 rows. Listwise deletion was applied to handle missing values (6 missing targets + 2 missing rainfall = 8 rows removed) resulting in **70 usable training observations**.

---

## 🔬 Methodology

### Task 1: Model Development

The first part of the notebook (`River_WaterLevel_Analysis_&_Forecasting.ipynb`) covers the rigorous development of the statistical model:

1. **Exploratory Data Analysis (EDA)**: Analyzed distributions, missing values, outlier inspection, and correlation analysis.
2. **Data Preprocessing**: Executed listwise deletion to ensure a complete and reliable dataset.
3. **Univariate OLS Regression**: Modeled the target using the current water level as the sole predictor.
4. **Multivariate OLS Regression**: Modeled the target incorporating both current water level and 24-hour rainfall.
5. **Model Diagnostics**: Validated assumptions via residuals vs. fitted plots, Q-Q plots, Shapiro-Wilk tests, Durbin-Watson, and VIF scoring.
6. **Model Evaluation**: Assessed performance using R², MSE, RMSE, and MAE on training data.
7. **Model Selection**: The univariate model was selected based on parsimony (AIC, BIC, adjusted R²).

#### Final Model Equation

$$\widehat{\text{Water Level}_{t+12h}} = -0.0305 + 0.9358 \times \text{Water Level}_{t}$$

#### Performance Metrics
| Metric | Value |
|:---|:---|
| R-squared | 0.9834 |
| Adjusted R² | 0.9831 |
| RMSE | 0.3082 mm |
| MAE | 0.2074 mm |
| MSE | 0.0950 mm² |

---

### Task 2: Generating Predictions

The second part of the notebook generates forecasts on unseen data:

1. **Load and Inspect Test Dataset**: Verified variables and distribution.
2. **Data Preprocessing**: Applied the exact same preprocessing steps to prevent data leakage:
   - `Gauging_station` is retained as an identifier.
   - Missing `24HrRF_Xt_1` values are imputed with the **training median (15.65 mm)** to ensure the dataset structure remains consistent, even though rainfall is not used in the final univariate model.
   - Zero rows are removed, guaranteeing a forecast for every input row.
3. **Generate Predictions**: Applied the Univariate OLS model to the test data.
4. **Build Submission File**: Created sequential IDs and structured the output to match submission guidelines.
5. **Sanity Check**: Compared test predictions against training distributions to verify model behavior.

**Output format:**
```csv
ID,Water_Level_Xt
1,1.234
2,0.876
...
```

---

## 💡 Key Findings & Insights

- **High Predictiveness**: The **current water level alone explains 98.3% of the variance** in the level 12 hours ahead (correlation ≈ 0.99). This reflects the profound physical persistence of river flow over short time horizons.
- **Rainfall Insignificance**: **24-hour rainfall is not a statistically significant predictor** (p = 0.187) once the current water level is included. Its immediate effect is likely already embedded in the current water level.
- **No Multicollinearity**: A **VIF ≈ 1.13** confirms there is no concerning multicollinearity between the initial predictors.

### 🏭 Practical Usefulness

In the context of flood early warning and river management, this model provides immense real-world value:
- **Early Warning Lead Time**: A highly reliable 12-hour forecast gives authorities sufficient time to issue warnings, deploy resources, and evacuate low-lying areas.
- **Simplicity & Robustness**: Relying on a single telemetered input (current water level) reduces dependency on potentially uncertain rainfall forecasts and prevents system failures.
- **Interpretability**: The physical interpretation is exceptionally clear—the river level 12 hours later is simply ~0.94 times the current level.

---

## ⚖️ Strengths & Limitations

### ✅ Strengths
- **Low Input Data Requirement**: Only the current water level is required at forecast time.
- **Avoids Overfitting**: A single-predictor linear model has no tuning parameters, significantly mitigating the risk of overfitting (high variance) commonly seen when deploying complex machine learning models on a limited dataset.

### ⚠️ Limitations
- **Heteroscedasticity**: Residual spread increases at higher water levels; therefore, the model is slightly less precise for massive river stations during peak flow.
- **Small Cross-Sectional Sample**: With only 70 training observations, the model relies on a cross-sectional snapshot rather than capturing true temporal dynamics (e.g., seasonality or long-term trends).
- **Linear Assumption**: The model fundamentally assumes a linear relationship. During extreme flood events involving bank overflow or backwater effects, river dynamics become highly non-linear.

---

## 🚀 Getting Started

### Prerequisites

You can install all required dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Alternatively, if you are using a virtual environment:
```bash
# PowerShell
.\.venv\Scripts\Activate.ps1

# Command Prompt
.venv\Scripts\activate
```

### Run the Notebook

1. Open `River_WaterLevel_Analysis_&_Forecasting.ipynb` in Jupyter Notebook/Lab.
2. Navigate to **Kernel → Restart & Run All** to execute everything seamlessly from scratch.

### Generate the Submission (Task 2)

1. Ensure `test_data.csv` is located in the root directory.
2. Run the **Task 2** cells sequentially in the notebook.
3. The pipeline will output `submission.csv`, ready for upload.

---

## 🏅 Evaluation

Submissions are scored on **Mean Squared Error (MSE)**:

$$\text{MSE} = \frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)^2$$

A lower MSE indicates superior predictive performance.  
🏆 **Training MSE of the final model: 0.0950 mm²**

---

## 📜 License & Acknowledgments

This work is submitted as part of a university course assignment for **CM2420 Statistical Inference**. The dataset is derived from publicly available data published by the **Department of Irrigation, Sri Lanka**.
