def select_features(df):
    X = df.drop(columns=['Company', 'Rating'])
    y = df['Rating']
    return X, y
