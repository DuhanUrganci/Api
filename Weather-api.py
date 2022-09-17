import requests

api_key = "Your Api Key"
live= input("The place where you live : ")
lang = input("language : ") # Turkish = tr,Italy = it ,France = fr
response = requests.get("http://api.weatherapi.com/v1/current.json",params={
    "key":api_key,
    "lang":lang,
    "q":live
})
response_doc= response.json()
country= response_doc["location"]
weather = response_doc["current"]
print(f'Name of Your Country :{country["country"]}\nState :{country["name"]}\nWeather Information :{weather["condition"]["text"]}\Temperature :{weather["temp_c"]}\nhumidity : {weather["humidity"]}')

