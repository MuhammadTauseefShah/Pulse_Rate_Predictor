**Pulse Rate Predictor**
📖 Project Description

The Pulse Rate Predictor is a machine learning project that analyzes human vital signs and predicts whether an individual’s pulse rate is within a normal range or indicates a potential health risk.

This project demonstrates an end-to-end ML workflow — from data exploration and visualization to preprocessing, model training, evaluation, and result interpretation. Four machine learning algorithms are implemented and compared for performance:

Initially we implement Logistic Regression

Secondly we use Random Forest Classifier

Thirdly we implement Gradient Boosting Classifier

Eventually Support Vector Machine Algorithm (SVM)

📊 Dataset

The project uses the Human Vital Signs Dataset, which includes key physiological measurements:

1. Age (years)
2. Gender (male/female)
3. Body Temperature (°C)
4. Blood Pressure (mmHg)
5. Pulse Rate (beats per minute)
6. Respiration Rate (breaths per minute)
7. Oxygen Saturation (%)

For classification problems, we define the target variable as:

0 → Normal pulse rate (≤ 100 bpm)

1 → High pulse rate risk (> 100 bpm)

📌 Dataset Source: Kaggle – Human Vital Signs Dataset(CSV file format)

⚙️ Project Workflow
1. **Data Exploration & Visualization**

***Dataset overview and descriptive statistics***

***Pulse rate distribution histogram***

***Scatter plot of age vs Pulse rate***

2. **Data Preprocessing**

***Handling categorical variables via encoding***

***Standardizing features using z-score scaling***

***Creating a binary target variable (risk classification)***

3. **Model Training**

Implementing four classification algorithms:

***Logistic Regression***

***Random Forest***

***Gradient Boosting***

***Support Vector Machine(SVM)***

4. **Model Evaluation**

***Accuracy Scores***

***Confusion matrices***

**Classification reports (precision, recall, F1-score)***

***Visualization of confusion matrix heatmaps***

📈 Results: 
Algorithm	Accuracy (example run)
Logistic Regression	~92%
Random Forest	~94%
Gradient Boosting	~93%
Support Vector Machine	~91%

✅ Random Forest performed best, but model performance may vary depending on dataset splits.
