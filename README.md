# Pulse Pressure Predictor

This is a web application that predicts human pulse pressure based on various physiological features. The prediction is made using a Random Forest regression model trained on a dataset of human vital signs.

## Project Overview

This project takes a machine learning model developed in a Jupyter Notebook and deploys it as an interactive web application using the Flask framework. The user can input various health metrics, and the application will provide a real-time prediction of their pulse pressure.

## Features

-   **Interactive Interface:** A user-friendly web form for inputting physiological data.
-   **Real-time Predictions:** Get instant pulse pressure predictions from the trained Random Forest model.
-   **Machine Learning Integration:** Demonstrates the deployment of a scikit-learn model in a web environment.

## Technologies Used

-   **Python:** The core programming language.
-   **Flask:** A lightweight web framework for the backend.
-   **Scikit-learn:** For building and training the machine learning model.
-   **Pandas:** For data manipulation and analysis in the notebook.
-   **HTML/CSS:** For the frontend structure and styling.
-   **Pickle:** For serializing and deserializing the trained model and scaler.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.x
-   pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/Pulse_Rate_Predictor.git
    cd Pulse_Rate_Predictor
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Run the Flask application:**
    ```bash
    python app.py
    ```

2.  **Open your web browser** and navigate to `http://127.0.0.1:5000/`.

## How to Use

1.  Fill in all the fields in the web form with the required physiological data.
2.  Click the "Predict" button.
3.  The predicted pulse pressure will be displayed below the form.

## Project Structure

```
Pulse_Rate_Predictor/
|-- app.py
|-- model.pkl
|-- scaler.pkl
|-- requirements.txt
|-- templates/
|   |-- index.html
|-- static/
|   |-- styles.css
|-- Pulse_Rate_Predictor.ipynb
|-- README.md
```

## Acknowledgments

-   The dataset used for this project is the "Human Vital Sign Dataset".
