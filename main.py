import json
import requests

interest = str(input("What type of news are you interested in? "))
r = requests.get(f"https://newsapi.org/v2/everything?q={interest}&from=2023-10-25&sortBy=publishedAt&apiKey=5f273ab2092140119559be810cec4136")

# Check if the request was successful
if r.status_code == 200:
    # Parse the JSON data
    news = json.loads(r.text)

    # Print the top 10 news
    for index, article in enumerate(news["articles"][:10], start=1):
        print(f"{index}. {article['title']}")
        print(article["description"])
        print('-' * 50)
else:
    print(f"Error: {r.status_code}")
