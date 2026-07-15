# Bengaluru House Price Prediction

A simple Streamlit app that predicts house prices in Bengaluru from a few user inputs:

- Location
- Total area in square feet
- Number of bedrooms (BHK)
- Number of bathrooms

The app loads a trained machine learning model and a column map from `columns.json` to build the input vector used for prediction.

## Project Structure

- `app.py` - Streamlit application entry point
- `Bengaluru_House_Data.csv` - Dataset used during model development
- `columns.json` - Encoded feature column names used by the model
- `main.ipynb` - Notebook for training and experimentation
- `requirements.txt` - Python dependencies

## Requirements

- Python 3.10 or newer
- pip

## Installation

1. Clone or open the project folder.
2. Create and activate a virtual environment.
3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

Start the Streamlit app with:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal, usually `http://localhost:8501`.

## How It Works

The app converts the selected location and numeric inputs into the feature format expected by the trained model, then displays the estimated house price in lakhs.

## Note

The app expects the trained model file referenced in `app.py` to be present in the project folder. If you rename or replace the model artifact, make sure the filename in `app.py` matches it.