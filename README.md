# 🏘️ API de Predicción de Arriendo en Chile

Este proyecto demuestra cómo entrenar un modelo de machine learning con Python y Scikit-learn para predecir el precio estimado de arriendo de una propiedad, y cómo desplegarlo como una API REST usando **FastAPI**.

---

## 📁 Estructura del proyecto

```
proyecto_arriendo_ml/
├── app/
│   ├── main.py                    ← API FastAPI
│   ├── modelo_arriendo.pkl        ← Modelo serializado
├── data/
│   └── arriendos_chile_simulado.csv ← Dataset simulado
├── notebooks/
│   └── entrenamiento_modelo.ipynb ← Entrenamiento del modelo
├── requirements.txt              ← Dependencias del proyecto
├── README.md                     ← Instrucciones de uso
```

---

## 🚀 Requisitos

- Python 3.9+
- pip (gestor de paquetes)

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

## 🧠 Descripción del proyecto

El modelo fue entrenado con datos simulados de arriendos en distintas comunas de Chile.

**Variables utilizadas:**

- `comuna`, `tipo`, `superficie`, `habitaciones`, `baños`

El modelo fue guardado usando `joblib`.

---

## 🧪 Cómo ejecutar la API localmente

1. Asegúrate de estar en la carpeta del proyecto.
2. Ejecuta el siguiente comando:

```bash
uvicorn app.main:app --reload
```

3. Abre tu navegador y ve a:

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
