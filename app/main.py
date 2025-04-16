from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

def entrenar_modelo():
    np.random.seed(42)
    n = 300
    comunas = ['Santiago', 'Providencia', 'Maipú', 'Las Condes', 'Puente Alto']
    tipos = ['Departamento', 'Casa']

    df = pd.DataFrame({
        'comuna': np.random.choice(comunas, n),
        'tipo': np.random.choice(tipos, n),
        'superficie': np.random.randint(30, 150, n),
        'habitaciones': np.random.randint(1, 5, n),
        'baños': np.random.randint(1, 3, n)
    })

    base_price = {
        'Santiago': 300000,
        'Providencia': 450000,
        'Maipú': 250000,
        'Las Condes': 500000,
        'Puente Alto': 220000
    }

    df['precio'] = (
        df['superficie'] * 4200 +
        df['habitaciones'] * 50000 +
        df['baños'] * 30000 +
        df['comuna'].map(base_price) +
        np.random.normal(0, 50000, n)
    ).astype(int)

    X = df.drop("precio", axis=1)
    y = df["precio"]

    preprocessor = ColumnTransformer([
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['comuna', 'tipo'])
    ], remainder='passthrough')

    pipeline = Pipeline([
        ('preprocess', preprocessor),
        ('model', LinearRegression())
    ])

    pipeline.fit(X, y)
    return pipeline

modelo = entrenar_modelo()

app = FastAPI(title="API de Predicción de Arriendo (modelo en memoria)")

class DatosArriendo(BaseModel):
    comuna: str
    tipo: str
    superficie: int
    habitaciones: int
    baños: int

@app.post("/predecir")
def predecir(data: DatosArriendo):
    entrada = pd.DataFrame([{
        "comuna": data.comuna,
        "tipo": data.tipo,
        "superficie": data.superficie,
        "habitaciones": data.habitaciones,
        "baños": data.baños
    }])
    pred = modelo.predict(entrada)
    return {"precio_estimado": round(pred[0])}
