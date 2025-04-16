from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Cargar el modelo serializado
modelo = joblib.load("app/modelo_arriendo_chile.pkl")

# Instancia de FastAPI
app = FastAPI(title="API de Predicción de Arriendo en Chile")

# Modelo de datos de entrada
class DatosArriendo(BaseModel):
    comuna: str
    tipo: str
    superficie: int
    habitaciones: int
    baños: int

# Ruta para predicción
@app.post("/predecir")
def predecir(data: DatosArriendo):
    entrada = [[
        data.comuna,
        data.tipo,
        data.superficie,
        data.habitaciones,
        data.baños
    ]]
    pred = modelo.predict(entrada)
    return {"precio_estimado": round(pred[0])}
