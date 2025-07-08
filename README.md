# Flight Price Prediction Project

This project predicts flight ticket prices using machine learning. It includes data preprocessing, model training, hyperparameter tuning, evaluation, and a Flask web app for user interaction.

## Project Structure

```
flight_price_pre/
│
├── App/
│   ├── app.py                # Flask web application
│   ├── model/
│   │   └── model.pkl         # Trained ML model
│   ├── routes/
│   │   └── __init__.py       # (Reserved for route definitions)
│   ├── static/
│   │   ├── javascript.js     # Frontend JS
│   │   └── style.css         # Frontend CSS
│   └── templates/
│       └── index.html        # Main HTML template
│
├── Data/
│   ├── processed_data.csv    # Cleaned data for modeling
│   └── raw.csv               # Raw flight data
│
├── Evaluation/
│   ├── best_model_saving.ipynb        # Notebook: Save best model
│   └── evaluation_and_tuning.ipynb    # Notebook: Model tuning & evaluation
│
├── Training/
│   ├── preprocess_data.ipynb          # Notebook: Data preprocessing
│   └── training_notebook.ipynb        # Notebook: Model training & comparison
│
├── requirements.txt          # Python dependencies
├── python_version.txt        # Python version info
├── setup.exe                 # (Not used in ML pipeline)
└── README.md                 # Project documentation
```

## Notebooks Overview

- **Training/training_notebook.ipynb**: Compares multiple regression models and evaluates their performance.
- **Training/preprocess_data.ipynb**: Handles data cleaning and feature engineering (not shown above).
- **Evaluation/evaluation_and_tuning.ipynb**: Performs hyperparameter tuning (RandomizedSearchCV) and evaluates the best model.
- **Evaluation/best_model_saving.ipynb**: Retrains and saves the best model for deployment.

## Web Application

- **App/app.py**: Flask app that loads the trained model and predicts flight prices based on user input from the web form.
- **App/templates/index.html**: User interface for entering flight details and viewing predictions.

## How to Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the Flask app**:
   ```bash
   cd App
   python app.py
   ```
3. **Access the app**: Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Model Training & Evaluation

1. **Preprocess data**: Use `Training/preprocess_data.ipynb` to clean and prepare the data.
2. **Train models**: Use `Training/training_notebook.ipynb` to compare different regression models.
3. **Tune & evaluate**: Use `Evaluation/evaluation_and_tuning.ipynb` for hyperparameter tuning and performance evaluation.
4. **Save best model**: Use `Evaluation/best_model_saving.ipynb` to save the final model as `App/model/model.pkl`.

## Requirements

- Python (see `python_version.txt`)
- See `requirements.txt` for all dependencies (e.g., pandas, scikit-learn, flask, joblib, numpy)

## Notes

- The web app expects the model file at `App/model/model.pkl`.
- Data files should be placed in the `Data/` directory.
- Notebooks are provided for transparency and reproducibility of the ML workflow.
