# 💊 Drug Classification with Decision Tree

Machine Learning API built with **FastAPI** to predict the appropriate drug based on patient medical data.  
The model is trained using **Decision Tree Classifier** from Scikit-learn and deployed as a REST API.

---

## 📌 Project Overview

This project:

- Trains a **Drug Classification** model using Decision Tree
- Saves the trained model as `.pkl`
- Serves predictions using **FastAPI**
- Uses **Pydantic** for input validation
- Loads environment variables using **python-dotenv**

---

## 🏗 Project Structure

```
DRUG_CLASSIFICATION/
│
├── src/
│   ├── models/
│   │   └── drug_classifier.pkl
│   ├── routers/
│   │   └── predict.py
│   ├── utils/
│   │   ├── DrugData.py
│   │   ├── config.py
│   │   └── inference.py
│   └── notebook/
│       └── notebook.ipynb
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🧠 Model Input Features

| Feature   | Type   | Allowed Values        |
|-----------|--------|-----------------------|
| Age       | int    | > 0                   |
| Sex       | string | F, M                  |
| BP        | string | HIGH, LOW, NORMAL     |
| Cholesterol | string | HIGH, NORMAL        |
| Na_to_K   | float  | > 0                   |

---

## ⚙ Installation

### 1️⃣ Clone the repository

```bash
git clone <your-repository-url>
cd DRUG_CLASSIFICATION
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate environment:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the API

From the project root directory:

```bash
uvicorn main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📥 How to Use the API

### Endpoint

```
POST /predict
```

### Example Request (JSON)

```json
{
  "Age": 45,
  "Sex": "F",
  "BP": "HIGH",
  "Cholesterol": "NORMAL",
  "Na_to_K": 15.2
}
```

### Example Response

```json
{
  "prediction": "drugX"
}
```

---

## 🧪 Testing the API

### Using Swagger UI

1. Open: `http://127.0.0.1:8000/docs`
2. Click **POST /predict**
3. Click **Try it out**
4. Enter request body
5. Click **Execute**

### Using cURL

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d "{\"Age\":45,\"Sex\":\"F\",\"BP\":\"HIGH\",\"Cholesterol\":\"NORMAL\",\"Na_to_K\":15.2}"
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
NAME_APP=Drug Classification API
```

---

## 🛠 Tech Stack

- **Python**
- **FastAPI**
- **Scikit-learn** — Decision Tree Classifier
- **Pydantic**
- **Uvicorn**
- **Joblib**
- **Pandas**
- **NumPy**

---

## 📦 Model Training

Model training is done inside:

```
src/notebook/notebook.ipynb
```

After training, save the model:

```python
import joblib
joblib.dump(model_pipeline, "drug_classifier.pkl")
```

Then move the model file to:

```
src/models/
```
