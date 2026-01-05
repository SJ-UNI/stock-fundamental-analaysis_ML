from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd
from feature_engineering import select_features
from data_preprocessing import preprocess_data

df = pd.read_csv("dataset/stock_fundamental_data.csv")
df = preprocess_data(df)

X, y = select_features(df)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

joblib.dump(model, "models/trained_model.pkl")
