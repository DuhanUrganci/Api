import requests

url2 = "http://api.weatherapi.com/v1/forecast.json"
url = "http://api.weatherapi.com/v1/current.json"
api = "api key"

sehir = input("Hava durumunu görmek istediğiniz şehir : ")
response2 = requests.get(url2,params={
    "key":api,
    "q":sehir,
    "lang":"tr",
    "days":"3"
}) 
response = requests.get(url,params={
    "key":api,
    "q":sehir,
    "lang":"tr",
})


text = response2.json()

name = text["location"]["name"]
country = text["location"]["country"]
print(country)
cel = text["current"]["temp_c"]
textinfo = text["current"]["condition"]["text"]
print(f"Görüntülenen ülke :{country} Görüntülenen şehir :{name} şehrin sıcaklığı :{cel} şehrin hava durumu :{textinfo} ")

tahmin = text["forecast"]["forecastday"]
for a in tahmin:
    date = a["date"]
    estimate = a["day"]["condition"]["text"]
    print(f"Görüntülenen şehir :{name} tarihler :{date} tahminler :{estimate}")