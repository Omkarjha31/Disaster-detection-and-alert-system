# Disaster-detection-and-alert-system

A machine learning-powered real-time system to detect disaster-related tweets and generate alerts using data from Twitter, OpenWeather, and USGS APIs.

---

## 🚀 Features

- Detects disaster-related tweets using NLP and machine learning.
- Integrates:
  - **Twitter API**: Fetches live tweets for analysis.
  - **OpenWeather API**: Retrieves current weather conditions.
  - **USGS API**: Monitors earthquake and seismic activity.
- Flask-based API for prediction.
- Easy backend integration.

---

## 🌐 APIs Used

| API | Purpose |
|-----|---------|
| **Twitter API** | To fetch real-time tweets for disaster keyword monitoring. |
| **OpenWeather API** | To cross-check weather alerts and enhance accuracy. |
| **USGS API** | To access live earthquake and geological activity data. |

---

## 🧠 Dataset

- `sample_train.csv`: Labeled data for model training.
- `sample_test.csv`: For evaluation and predictions.

---

## ⚙️ Technologies Used

- Python, Flask
- Scikit-learn, Pandas, NumPy
- Twitter API (via Tweepy or similar)
- OpenWeather API
- USGS Earthquake API

---

## 🧪 Model Training

- Open: Trained_Model.py
- Preprocess text data.
- Train Logistic Regression on TF-IDF features.
- Evaluate and save model.

## 🔌 API Endpoint Usage

- /predict
    POST /predict
    {
    "text": "There’s a huge storm in the city, flooding has started!"
    }

- Response:
    {
    "prediction": 1
    }

- 1 → Disaster tweet
- 0 → Not disaster-related

## 🔗 Backend Integration

You can connect this model to any backend that requires real-time disaster detection:
- Integrate with a web or mobile app using REST API
- Fetch tweets or weather data → send to /predict → get result

## 📦 Installation
- pip install pandas scikit-learn joblib flask requests
- pip install tweepy

## 🌍 Environment Variables
Create a .env file for API keys:
   - TWITTER_API_KEY=your_key_here
   - OPENWEATHER_API_KEY=your_key_here
   - USGS_API_ENDPOINT=https://earthquake.usgs.gov/...
Use python-dotenv to load them.