from sklearn.linear_model import LogisticRegression
import joblib


def train_model(X, y):
    model = LogisticRegression()
    model.fit(X, y)
    joblib.dump(model, 'analytics/nfl_model.pkl')
    return model