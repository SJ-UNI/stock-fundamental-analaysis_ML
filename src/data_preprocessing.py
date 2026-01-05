from sklearn.preprocessing import LabelEncoder
import pandas as pd

def preprocess_data(df):
    le = LabelEncoder()
    df['Rating'] = le.fit_transform(df['Rating'])
    return df

if __name__ == "__main__":
    df = pd.read_csv("dataset/stock_fundamental_data.csv")
    processed = preprocess_data(df)
    print(processed.head())
