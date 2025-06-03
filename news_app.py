from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Set your NewsAPI key here or use environment variable
API_KEY = 'd5fd416f235740d481b92f0402a62101'  # Replace with your actual API key

NEWS_API_BASE_URL = "https://newsapi.org/v2/top-headlines"

# Homepage route
@app.route('/', methods=['GET'])
def index():
    category = request.args.get('category', 'general')
    query = request.args.get('query', '')

    # Construct query parameters
    params = {
        'apiKey': API_KEY,
        'country': 'us',
        'category': category
    }

    if query:
        params['q'] = query

    try:
        response = requests.get(NEWS_API_BASE_URL, params=params)
        response.raise_for_status()
        news_data = response.json()
        articles = news_data.get('articles', [])
    except requests.RequestException as e:
        print(f"Error fetching news: {e}")
        articles = []

    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
