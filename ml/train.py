import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    confusion_matrix
)

from preprocess import clean_text


df = pd.read_csv(
    "data/datasets/emails.csv"
)

df["text"] = df["text"].fillna("")
df["text"] = df["text"].apply(clean_text)

X_train, X_test, y_train, y_test = train_test_split(
    df["text"],
    df["label"],
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            max_features=50000,
            ngram_range=(1, 2),
            min_df=2,
            sublinear_tf=True
        )
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            class_weight="balanced"
        )
    )
])

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(
    classification_report(
        y_test,
        predictions
    )
)

print(
    confusion_matrix(
        y_test,
        predictions
    )
)

joblib.dump(
    model,
    "ml/model/phishing_model.joblib"
)