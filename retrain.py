#Manejo de datos
import pandas as pd
import numpy as np
import os
import uuid

#Entrenamiento del modelo
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
import joblib

from prediction_model import PredictionModel


class RetrainModel:

    def __init__(self):
        numeric_features = ["TotalCharges", "MonthlyCharges", 'tenure']
        numeric_transformer = Pipeline(
            steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
        )

        categorical_features = ["gender", "SeniorCitizen", "Partner", "Dependents",
                                'PhoneService', "MultipleLines", 'InternetService',
                                'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                                'TechSupport', 'StreamingTV', 'StreamingMovies',
                                'Contract', 'PaperlessBilling', 'PaymentMethod']
        categorical_transformer = OneHotEncoder(handle_unknown="ignore")

        preprocessor = ColumnTransformer(
            transformers=[
                ("num", numeric_transformer, numeric_features),
                ("cat", categorical_transformer, categorical_features),
            ]
        )

        pipe = Pipeline(steps=[("preprocessor", preprocessor), ("rfc", RandomForestClassifier())])

        parameters = {
            "preprocessor__num__imputer__strategy": ["mean"],
            'preprocessor__num__scaler': [MinMaxScaler()],
            'rfc__n_estimators': [100],
            'rfc__max_depth': [10],
            'rfc__min_samples_leaf': [6]
        }

        self.grid_search = GridSearchCV(pipe, parameters, verbose=2, scoring='roc_auc', cv=5, n_jobs=-1)
        self.predicion_model = PredictionModel('random_forest')

    def retrain_model(self, X_train, y_train, X_test, y_test):
        self.grid_search.fit(X_train, y_train)
        best_lr = self.grid_search.best_estimator_
        y_pred_test = best_lr.predict(X_test)
        result_new = classification_report(y_test, y_pred_test, output_dict=True)
        y_pred_test_old, probability, name = self.predicion_model.make_predictions(X_test)
        result_old = classification_report(y_test, y_pred_test_old, output_dict=True)
        filename = str(uuid.uuid4())+'.sav'
        base_path = "models"
        fpath = os.path.join(base_path, filename)
        joblib.dump(best_lr, fpath)
        return result_new, result_old, filename