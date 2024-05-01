import requests


response = requests.get("https://newsapi.org/v2/top-headlines",params={"apiKey":"<api key>","countr":"tr","language":"tr"})

text = response.json()
for t in text["articles"]:
    title = t["title"]
    url = t["url"]
    author = t["author"]
    print(f"Haberin başlığı :{title} Haberin yazarı : {author}\n{url}")
    print("*"*100)


response = requests.get("https://newsapi.org/v2/everything",params={"apiKey":"<api key>","q":"atama","language":"tr","sortBy":"publishedAt"})
text = response.json()
for t in text["articles"]:
    title = t["title"]
    url = t["url"]
    author = t["author"]
    print(f"Haberin başlığı :{title} Haberin yazarı : {author}\n{url}")
    print("*"*100)
