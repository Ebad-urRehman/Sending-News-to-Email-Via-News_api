import os
import requests
from send_email import send_email

topic = "Python"
api_key = os.getenv("API-NEWS-KEY")
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      f"apiKey={api_key}" \
      "&language=en"
response = requests.get(url)
content = response.json()
body = f"Subject: Today's News from NewsAPI\n" \
            f"from NewsAPI\n" \
            f"Topic {topic}\n"
# access the title and description
for article in content["articles"][0:20]:
    titles = (article["title"])
    descriptions = (article["description"])
    url = article["url"]
    body += f"{titles}\n" \
            f"{url}\n" \
            f"{descriptions}\n\n\n"
message = body.encode('utf8')

send_email(message)
# print(descriptions)
# print(body)





"""There is no need of importing webpages to see in python
because the format is complex and not human understandable
news topic can be change in url q=topicname
content = request.test
the type of content is string

we need a dictionary or list to extract data properly
we use content = request.json for that"""