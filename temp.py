import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

df = pd.read_csv('training_data.csv')
df_clean = df.dropna(subset=['Water_Level_Xt', '24HrRF_Xt_1', 'Water_Level_Xt_1'])
y = df_clean['Water_Level_Xt']
X_uni = sm.add_constant(df_clean[['Water_Level_Xt_1']])
X_mul = sm.add_constant(df_clean[['Water_Level_Xt_1', '24HrRF_Xt_1']])
m_uni = sm.OLS(y, X_uni).fit()
m_mul = sm.OLS(y, X_mul).fit()

metrics = {}
for name, m in [('Univariate', m_uni), ('Multivariate', m_mul)]:
    pred = m.fittedvalues
    r2 = r2_score(y, pred)
    mse = mean_squared_error(y, pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y, pred)
    metrics[name] = {'R-squared': r2, 'MSE': mse, 'RMSE': rmse, 'MAE': mae}

print(pd.DataFrame(metrics).T.to_string())
