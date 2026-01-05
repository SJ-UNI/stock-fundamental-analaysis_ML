#📊 ML-Based Fundamental Analysis System for Stock Market Companies

Author: Hariharan SJ
Internship: Bluestock
Project Type: Machine Learning | Financial Analysis

#📌 Project Overview

This project implements a machine learning–based fundamental analysis system to evaluate stock-market–listed companies using key financial indicators.
The system predicts an investment recommendation — Buy, Hold, or Sell — to assist investors and analysts in data-driven decision-making.

#🎯 Objectives

Analyze fundamental financial indicators of companies

Automate stock evaluation using machine learning

Classify stocks into Buy / Hold / Sell categories

Reduce manual analysis effort and human bias

#🛠️ Tech Stack

Programming Language: Python

Libraries: Pandas, NumPy, Scikit-learn, Joblib

ML Algorithm: Random Forest Classifier

Tools: VS Code, Jupyter Notebook

#📂 Project Structure
Stock_Fundamental_Analysis_ML/
│
├── src/
│   ├── data_collection.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   ├── prediction.py
│   └── utils.py
│
├── dataset/
│   └── stock_fundamental_data.csv
│
├── models/
│   └── trained_model.pkl
│
├── notebooks/
│   └── analysis.ipynb
│
├── screenshots/
│   ├── model_accuracy.png
│   └── prediction_output.png
│
├── documentation/
│   ├── Project_Overview.pdf
│   ├── Technical_Document.pdf
│   └── Functional_Document.pdf
│
├── requirements.txt
├── run_instructions.txt
└── README.md

#📊 Dataset Description

The dataset contains fundamental financial indicators collected from publicly available financial sources.

#Key Features:

P/E Ratio

Earnings Per Share (EPS)

Return on Equity (ROE)

Debt-to-Equity Ratio

Market Capitalization

Revenue Growth

#Target Variable:

Stock Rating → Buy / Hold / Sell

#⚙️ Installation & Setup
#1️⃣ Prerequisites

Python 3.9 or above

pip package manager

#2️⃣ Install Dependencies
pip install -r requirements.txt

#▶️ How to Run the Project
python src/data_collection.py
python src/model_training.py
python src/prediction.py

#📈 Model Details

Algorithm Used: Random Forest Classifier

Train-Test Split: 80% Training, 20% Testing

Evaluation Metric: Accuracy Score

The trained model is serialized using joblib and saved as:

models/trained_model.pkl

#🖥️ Output

Model Accuracy: Displayed in terminal

Prediction Output:

Buy

Hold

Sell

Screenshots of outputs are included in the screenshots/ folder.

#📘 Documentation

Complete documentation is available in the documentation/ folder:

Project Overview

Technical Documentation

Functional Documentation

#🔮 Future Enhancements

Integration with real-time stock APIs

Inclusion of technical indicators

Web or mobile application interface

Support for more ML algorithms

#✅ Conclusion

This project demonstrates the practical application of machine learning in fundamental stock analysis, enabling accurate and efficient investment recommendations.

#📬 Contact

Author: Hariharan SJ
Internship Organization: Bluestock
