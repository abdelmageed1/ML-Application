# Diabetes Prediction API

This project is a FastAPI-based web service for predicting diabetes risk using a machine learning model. The model uses various health-related features to predict whether a person has diabetes.

## Features

- **REST API** built with FastAPI.
- **Model**: A machine learning model (`SVM` or other) for diabetes prediction.
- **Input**: Health parameters like Glucose, Blood Pressure, BMI, etc.
- **Output**: A prediction indicating whether the person is diabetic or not.

## Requirements

### Python Version:
- Python 3.7 or higher

### Dependencies:
To run the project, you will need the following Python packages:

- `fastapi`
- `uvicorn`
- `pydantic`
- `scikit-learn`
- `requests`
- `pickle`

These dependencies are listed in `requirements.txt`. Install them using the following command:

```bash
pip install -r requirements.txt
