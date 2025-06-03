import streamlit as st
import requests

st.set_page_config(page_title="Live News", layout="wide")

NEWS_API_KEY = 'd5fd416f235740d481b92f0402a62101'

st.title("📰 Live News Portal")

category = st.selectbox("Choose a category", [
    'general', 'business', 'technology', 'health', 'sports', 'science', 'entertainment'
])

query = st.text_input("Search keyword (optional):")

url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={NEWS_API_KEY}"
if query:
    url += f"&q={query}"

response = requests.get(url)
articles = response.json().get('articles', [])

if articles:
    for article in articles:
        st.markdown("### " + article.get('title', ''))
        st.image(article.get('urlToImage', 'https://via.placeholder.com/400x200'), width=600)
        st.write(article.get('description', 'No description'))
        st.markdown(f"[Read more]({article.get('url')})", unsafe_allow_html=True)
        st.markdown("---")
else:
    st.warning("No news found. Try a different keyword or category.")
