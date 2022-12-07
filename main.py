from typing import List

import pandas as pd

from fastapi import FastAPI
from sklearn.model_selection import train_test_split

from data_model import DataModel
from retrain_data_model import RetrainDataModel
from prediction_model import PredictionModel
from retrain import RetrainModel

app = FastAPI()


@app.get("/")
def read_root():
   return { "message": "Hello world" }

@app.post("/predict")
def make_predictions(X: List[DataModel], model: str = 'random_forest'):
    print(X)
    df = pd.DataFrame([x.dict() for x in X])
    predicion_model = PredictionModel(model)
    results, probability, model_name = predicion_model.make_predictions(df)
    df = pd.DataFrame(probability, columns=["No", "Yes"])
    df["Result"] = results
    return {"model":model_name, "result":df.to_dict()}

@app.post("/retrain")
def retrain(X: List[RetrainDataModel]):
    print(X)
    df = pd.DataFrame([x.dict() for x in X])
    retrain = RetrainModel()
    train, test = train_test_split(df, test_size=0.2, random_state=33)
    X_train, y_train = train.drop(['Churn'], axis=1), train['Churn']
    X_test, y_test = test.drop(['Churn'], axis=1), test['Churn']
    result_new, result_old, filename = retrain.retrain_model(X_train, y_train, X_test, y_test)
    return {"filename": filename, "result_new":result_new, "result_old":result_old}