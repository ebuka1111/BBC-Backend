from decouple import config
import requests
from news.models import News


url = f"https://newsdata.io/api/1/news?apikey={config('API_KEY')}&q=pegasus&language=en"

def generate_news(url):
    response = requests.get(url)
    all_news = dict(response.json())

    for news in all_news['results']:
        headline = news.get('title', '')
        content = news.get('content', '')
        category = news.get('category', '')
        link = news.get('link', '')
        video_url = news.get('video_link', ' ')
        reporter = news.get('creator', '')
        image = news.get('image_url', '')
        date_posted = news.get('pubDate', '')

 
        News.objects.create(headline=headline, content=content, category=category, link=link,
                        video_url=video_url, reporter=reporter, image=image, 
                        date_posted=date_posted)
    return("News has been created, check your admin")

# print(generate_news(url))


