from joblib import load
import os


class PredictionModel:

    def __init__(self, model='random_forest'):
        base_path = "models"
        self.model_name = model+".sav"
        fpath = os.path.join(base_path, str(model)+".sav")
        self.model = load(fpath)

    def make_predictions(self, data):
        result = self.model.predict(data)
        proba = self.model.predict_proba(data)
        return result, proba, self.model_name
