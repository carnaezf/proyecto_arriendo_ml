# 🏘️ API de Predicción de Arriendo en Chile

Este proyecto demuestra cómo entrenar un modelo de machine learning con Python y Scikit-learn para predecir el precio estimado de arriendo de una propiedad, y cómo desplegarlo como una API REST usando **FastAPI**.

---

## 📥 Pasos iniciales

### 1. Descargar y descomprimir el `.zip`
Descarga el archivo `proyecto_arriendo_ml.zip` y extrae su contenido.

Tu estructura debe verse así:

```
proyecto_arriendo_ml/
├── app/
├── data/
├── notebooks/
├── requirements.txt
├── README.md
```

---

### 2. Crear entorno virtual con `venv`

Desde la carpeta raíz `proyecto_arriendo_ml`, crea el entorno virtual:

```bash
python -m venv amb_proyecto_arriendo_ml
```

Actívalo según tu sistema operativo:

- **Windows:**
  ```bash
  amb_proyecto_arriendo_ml\Scripts\activate
  ```

- **macOS/Linux:**
  ```bash
  source amb_proyecto_arriendo_ml/bin/activate
  ```

---

### 3. Crear `.gitignore`

Crea un archivo `.gitignore` en la carpeta raíz con el siguiente contenido:

```
amb_proyecto_arriendo_ml/
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.log
*.pkl
*.csv
data/
.ipynb_checkpoints/
.vscode/
.idea/
.DS_Store
Thumbs.db
```

---

### 4. Inicializar Git

Desde la raíz del proyecto, ejecuta:

```bash
git init
git add .
git commit -m "Primer commit del proyecto"
```

---

### 5. Crear el archivo `main.py`

Crea el archivo `main.py` dentro de la carpeta `app/` y pega el siguiente contenido:

```python
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
```

También puedes descargar el archivo listo desde este enlace:  
👉 [Descargar main.py](sandbox:/mnt/data/main.py)

---

## 🧠 Descripción del proyecto

El modelo fue entrenado con datos simulados de arriendos en distintas comunas de Chile.

**Variables utilizadas:**
- `comuna`, `tipo`, `superficie`, `habitaciones`, `baños`

El modelo fue guardado usando `joblib`.

---

## 📁 Estructura del proyecto

```
proyecto_arriendo_ml/
├── app/
│   ├── main.py                    ← API FastAPI
│   ├── modelo_arriendo_chile.pkl  ← Modelo serializado
├── data/
│   └── arriendos_chile_simulado.csv ← Dataset simulado
├── notebooks/
│   └── entrenamiento_modelo.ipynb ← Entrenamiento del modelo
├── requirements.txt              ← Dependencias del proyecto
├── README.md                     ← Instrucciones de uso
├── .gitignore                    ← Archivos a excluir de Git
```

---

## 📦 Instalación de dependencias

Con el entorno virtual activado, instala los paquetes necesarios:

```bash
pip install -r requirements.txt
```

---

## 🚀 Cómo ejecutar la API localmente

1. Asegúrate de estar en la carpeta raíz del proyecto.
2. Ejecuta el siguiente comando:

```bash
uvicorn app.main:app --reload
```

3. Abre tu navegador en:

```
http://localhost:8000/docs
```

Ahí verás la documentación interactiva de Swagger para probar la API.

---

## 🧾 Ejemplo de uso

En `/docs`, haz clic en `POST /predecir` y usa este ejemplo:

```json
{
  "comuna": "Maipú",
  "tipo": "Departamento",
  "superficie": 60,
  "habitaciones": 2,
  "baños": 1
}
```

La respuesta será algo como:

```json
{
  "precio_estimado": 645312
}
```

---

## 📚 Recursos utilizados

- [FastAPI](https://fastapi.tiangolo.com/)
- [Scikit-learn](https://scikit-learn.org/)
- [Uvicorn](https://www.uvicorn.org/)
- [Joblib](https://joblib.readthedocs.io/en/latest/)

---
