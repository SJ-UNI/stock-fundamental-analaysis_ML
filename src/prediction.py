import joblib
import pandas as pd

model = joblib.load("models/trained_model.pkl")

sample = pd.DataFrame([[22.5, 70.2, 26.1, 0.13, 650000, 6.9]],
columns=['PE_Ratio','EPS','ROE','Debt_to_Equity','Market_Cap','Revenue_Growth'])

prediction = model.predict(sample)
print("Predicted Stock Rating:", prediction)
