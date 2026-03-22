# 🏠 House Price Prediction

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange?style=for-the-badge&logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> A Machine Learning web application that predicts house prices based on area demographics and property details using Linear Regression.

---

## 📸 Demo

> *Add screenshot of your Streamlit app here*

---

## 📌 Overview

This project builds an end-to-end Machine Learning pipeline to predict house prices in the USA. It includes data preprocessing, model training, evaluation, and a professional dark-mode web interface built with Streamlit.

---

## 🧠 ML Pipeline
```
Data Loading → EDA → Train-Test Split → Feature Scaling → Model Training → Evaluation → Deployment
```

> ✅ Train-Test Split is performed **before** scaling to avoid data leakage

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| R² Score | 0.91 |
| MAE | $80,859 |
| RMSE | ~$99,704 |
| Algorithm | Linear Regression |

---

## 📁 Project Structure
```
House-Price-Prediction/
│
├── app.py                 ← Streamlit Web App
├── LR_Model.ipynb         ← Model Training Notebook
├── USA_Housing.csv        ← Dataset
├── model.pkl              ← Saved Model
├── scaler.pkl             ← Saved Scaler
└── README.md              ← Project Documentation
```

---

## 🔧 Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core Language |
| Pandas & NumPy | Data Manipulation |
| Scikit-learn | ML Model & Preprocessing |
| Matplotlib & Seaborn | EDA Visualizations |
| Plotly | Interactive Charts |
| Streamlit | Web Interface |
| Pickle | Model Saving |

---

## 📦 Installation & Run

**1. Clone the repository**
```bash
git clone https://github.com/pkale9650-ai/House-Price-Prediction.git
cd House-Price-Prediction
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

---

## 📋 Dataset

- **Source** : [Kaggle - USA Housing Dataset]([https://www.kaggle.com/datasets](https://www.kaggle.com/datasets/vedavyasv/usa-housing))
- **Rows** : 5,000
- **Features** : 5 numerical features

| Feature | Description |
|---------|-------------|
| Avg. Area Income | Average income of the area |
| Avg. Area House Age | Average age of houses in area |
| Avg. Area Number of Rooms | Average number of rooms |
| Avg. Area Number of Bedrooms | Average number of bedrooms |
| Area Population | Population of the area |
| Price | 🎯 Target Variable |

---

## ✨ Features

- ✅ Clean dark mode professional UI
- ✅ Real-time price prediction
- ✅ Gauge chart visualization
- ✅ Feature impact bar chart
- ✅ Min / Max price range estimate
- ✅ No data leakage pipeline

---

## 👨‍💻 Author

**Pratik Kale**
- 🔗 [LinkedIn](https://www.linkedin.com/in/pratik-kale-400ba8327/)
- 🐙 [GitHub](https://github.com/pkale9650-ai)

---

## 📄 License

This project is licensed under the MIT License.
