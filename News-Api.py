import requests

apiKey = "Your Api Key"
subject = input("Subject : ")
language = input("Language : ") # eg = English
response = requests.get("https://newsapi.org/v2/everything?",params={
    "q":subject,
    "language":language,
    "apiKey":apiKey,
    "sortBy":"publishedAt"
})

title = response.json()["articles"]
try:    
    for haber in title:
        author = haber["author"]
        newsHeadline = haber["title"]
        newsDescription = haber["description"]
        newsUrl = haber["url"]
        print(f"The Author of The News :{author}\nThe Title of The News :{newsHeadline}\nDescription of The News :{newsDescription}\nThe url of the news :{newsUrl}")
        print("*"*100)
except Exception as e:
    print(e)
finally:
    print("done.")