import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

df = pd.read_csv(".venv/data/dataset_model.csv")

target = 'Emisii_Totale_tone_CO2'
x = df.drop(columns=[target])
y = df[target]

colNumerice = x.select_dtypes(include=['int64','float64']).columns
x[colNumerice] = x[colNumerice].fillna(0)

colCategorice = x.select_dtypes(include=['object']).columns
x[colCategorice] = x[colCategorice].fillna('Nu_se_aplica')

X_encoded = pd.get_dummies(x, columns=colCategorice, drop_first=True)

preprocessed_df = pd.concat([y, X_encoded], axis=1)
preprocessed_df.to_csv("dataset_preprocesat.csv", index=False)

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_encoded, y)

imp = rf.feature_importances_
nume = X_encoded.columns

impDataFrame = pd.DataFrame({'Variabila':nume, 'Importanta':imp}).sort_values(by='Variabila', ascending=False)

print("Top 15 cele mai importante variabile:")
print(impDataFrame.head(15))

plt.figure(figsize=(10,6))
top_10 = impDataFrame.head(10)

plt.barh(top_10['Variabila'][::-1], top_10['Importanta'][::-1], color='#2E86C1')
plt.xlabel('Scor Importanță')
plt.ylabel('Variabilă (Întrebare)')
plt.title('Top 10 Variabile Predictoare pentru Amprenta de Carbon')
plt.tight_layout()
plt.savefig("feature_importance.png")