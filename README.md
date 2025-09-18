# Pulse Rate Prediction Project

This project focuses on predicting human pulse rate using machine learning. It encompasses a complete workflow from data loading and cleaning to model training and performance evaluation, all contained within the `Pulse_Rate_Predictor.ipynb` Jupyter Notebook.

This guide provides instructions on how to set up and run the project in a code editor like Visual Studio Code.

## Project Overview

This project serves as a practical guide to building a machine learning model for pulse rate prediction. It explores the use of various regression algorithms on a human vital signs dataset. The primary goal is to demonstrate a clear and effective machine learning pipeline suitable for a local development environment.

## Features

- **Data Preprocessing**: Cleans and prepares the vital signs dataset for modeling.
- **Exploratory Data Analysis (EDA)**: Includes a correlation heatmap to visualize feature relationships.
- **Model Training**: Implements four different regression algorithms:
    - Linear Regression
    - K-Nearest Neighbors (KNN)
    - Random Forest
    - Gradient Boosting
- **Performance Evaluation**: Compares models using R-squared and Mean Squared Error (MSE) metrics.
- **Visualization**: Plots model performance and prediction accuracy.

## Getting Started

Follow these instructions to set up the project on your local machine using a code editor.

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- A code editor like [Visual Studio Code](https://code.visualstudio.com/) (recommended)
- [Git](https://git-scm.com/downloads/) for cloning the repository

### Installation & Setup

1.  **Clone the Repository**
    Open your terminal or command prompt and clone the repository:
    ```bash
    git clone https://github.com/MuhammadTauseefShah/pulse-rate-prediction.git
    cd pulse-rate-prediction
    ```

2.  **Set Up a Virtual Environment**
    It's highly recommended to use a virtual environment to manage project dependencies.

    ```bash
    # Create a virtual environment
    python -m venv venv

    # Activate the virtual environment
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    A `requirements.txt` file is included to easily install all necessary libraries. Run the following command:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Open in Your Code Editor**
    Launch your code editor. If you are using VS Code, you can open the project folder with:
    ```bash
    code .
    ```

### Running the Notebook

1.  **Install the Jupyter Extension**
    If you are using VS Code, make sure you have the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) installed. It allows you to run `.ipynb` files directly in the editor.

2.  **Select the Python Interpreter**
    -   In VS Code, open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`).
    -   Type `Python: Select Interpreter`.
    -   Choose the interpreter associated with your virtual environment (`./venv/bin/python` or `.\venv\Scripts\python.exe`).

3.  **Run the Notebook Cells**
    -   Open the `Pulse_Rate_Predictor.ipynb` file in your editor.
    -   You can run cells individually by clicking the "Run Cell" (▶️) button next to each cell.
    -   To run the entire notebook, click the "Run All" (▶▶️) button at the top of the notebook editor.

## Project Structure
pulse-rate-prediction/
├── human_vital_sign_dataset.csv # The dataset file
├── Pulse_Rate_Predictor.ipynb # The main Jupyter Notebook with all the code
├── README.md # This README file
└── requirements.txt # List of Python dependencies
code
Code
## Results Summary

The Random Forest and Linear Regression models demonstrated the highest performance, achieving near-perfect R-squared scores on the test set.

| Model               | R-squared |       MSE |
| ------------------- | --------- | --------- |
| Linear Regression   | 1.000000  | 4.52e-28  |
| K-Neighbors         | 0.945613  | 5.90e+00  |
| Random Forest       | 1.000000  | 0.00e+00  |
| Gradient Boosting   | 0.999811  | 2.05e-02  |

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any issues, please feel free to open an issue or submit a pull request.
