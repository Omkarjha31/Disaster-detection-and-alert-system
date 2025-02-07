from flask import Flask, request, jsonify
import requests
import tweepy
from textblob import TextBlob

app = Flask(__name__)

# API Keys
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAKM1ywEAAAAAnt2TIqtLN62qSyREn10E8KluP5Y%3D4razYEHaXMdToguDGcR5UGbtO3e8kjJ5OCtrjxNXDRKVIASbzO"
NEWS_API_KEY = "6242744179024a4b9fbb77444c43977e"
WEATHER_API_KEY = "ce45ef9fe546adf905b3d3bd1274e1ed"

# Twitter Client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Function to Analyze Disaster Severity
def analyze_text(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment < -0.5:
        return "Critical Disaster Alert"
    elif sentiment < 0:
        return "Moderate Disaster Alert"
    else:
        return "No Disaster Detected"

# Home Route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Disaster Detection API is Running"})

# Route to Get Real-Time Disaster Tweets
@app.route("/get_tweets", methods=["GET"])
def get_tweets():
    query = "earthquake OR flood OR landslide OR Disaster-is:retweet"
    tweets = client.search_recent_tweets(query=query, max_results=5)

    results = []
    for tweet in tweets.data:
        results.append({"text": tweet.text, "alert": analyze_text(tweet.text)})

    return jsonify(results)

# Route to Get Disaster News
@app.route("/get_news", methods=["GET"])
def get_news():
    url = f"https://newsapi.org/v2/everything?q=disaster&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()

    results = []
    for article in response["articles"][:5]:
        results.append({"title": article["title"], "url": article["url"]})

    return jsonify(results)

# Route to Get Live Weather Alerts
@app.route("/get_weather", methods=["GET"])
def get_weather():
    city = request.args.get("city", default="India", type=str)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}"
    response = requests.get(url).json()

    return jsonify({"city": city, "weather": response["weather"][0]["description"]})

# Run Flask Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
