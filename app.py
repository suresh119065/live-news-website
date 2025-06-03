from flask import Flask, render_template, request
import requests

app = Flask(__name__)

NEWS_API_KEY = 'd5fd416f235740d481b92f0402a62101'  # Replace with your actual NewsAPI key
BASE_URL = 'https://newsapi.org/v2/'

@app.route('/', methods=['GET'])
def home():
    category = request.args.get('category', 'general')
    query = request.args.get('q', '')

    url = f"{BASE_URL}top-headlines?country=us&apiKey={NEWS_API_KEY}&category={category}"
    if query:
        url += f"&q={query}"

    response = requests.get(url)
    news = response.json().get('articles', [])

    return render_template('index.html', news=news, selected_category=category)

if __name__ == '__main__':
    app.run(debug=True)
