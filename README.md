# 🛡️ Credit Card Fraud Detection Web App

This is a Streamlit-based machine learning web app that predicts fraudulent transactions using anonymized credit card data.

## ✅ How to Use

- Upload a sample CSV or manually enter transaction details
- Model returns whether it's a fraud or not

## ⚠️ Note

This app uses anonymized features (V1–V28) from PCA. It cannot predict on real card data.

## 🔗 Live Demo

👉 [Click here to try the live app](https://credit-card-fraud-detection-jeshmrr8faebczecwcxgzg.streamlit.app/)

## ⚙️ Technologies Used

- Python
- Scikit-learn
- Pandas
- Matplotlib
- Streamlit

---

## 🚀 Features

- Trains a machine learning model on anonymized credit card transaction data
- Predicts whether a transaction is **fraudulent or legitimate**
- Clean, responsive UI built with Streamlit
- Real-time input and prediction
- Visualizations for better insight

---

## 🛠 How to Run Locally

```bash
git clone https://github.com/Dipendra88/Credit-card-fraud-detection.git
cd Credit-card-fraud-detection
pip install -r requirements.txt
streamlit run app.py
