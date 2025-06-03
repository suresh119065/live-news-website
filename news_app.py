from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Use environment variable or replace with your key string
API_KEY = 'd5fd416f235740d481b92f0402a62101'

NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

@app.route('/', methods=['GET'])
def index():
    category = request.args.get('category', 'general')
    query = request.args.get('query', '')

    params = {
        'apiKey': API_KEY,
        'country': 'us',
        'category': category
    }

    if query:
        params['q'] = query

    articles = []
    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        articles = data.get('articles', [])
    except requests.RequestException as e:
        print(f"Error fetching news: {e}")

    return render_template('index.html', articles=articles, category=category, query=query)

# Only run the app if this script is run directly (useful for local dev)
if __name__ == "__main__" 
    app.run(debug=False, use_reloader=False)
