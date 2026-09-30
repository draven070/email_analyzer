import joblib

from preprocess import clean_text


class PhishingClassifier:

    def __init__(self, model_path):

        self.model = joblib.load(
            model_path
        )

    def predict(self, subject, body):

        text = f"{subject}\n{body}"

        text = clean_text(text)

        prediction = self.model.predict(
            [text]
        )[0]

        probabilities = self.model.predict_proba(
            [text]
        )[0]

        phishing_probability = probabilities[1]

        return {
            "prediction": int(prediction),
            "phishing_probability":
                float(phishing_probability)
        }