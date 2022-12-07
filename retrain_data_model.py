from pydantic import BaseModel

class RetrainDataModel(BaseModel):

    TotalCharges: float
    MonthlyCharges: float
    tenure: int
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    PhoneService: str
    MultipleLines: str
    InternetService: str
    TechSupport: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    Churn: str