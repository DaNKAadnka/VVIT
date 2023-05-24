import requests

city = "Moscow,RU"
app_id = "49cd0d48255340477ea916c54e7f74f2"


res1 = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
data1 = res1.json()

print("Город:", city)
print("Погодные условия:", data1['weather'][0]['description'])
print("Температура:", data1['main']['temp'])
print("Минимальная температура:", data1['main']['temp_min'])
print("Максимальная температура", data1['main']['temp_max'])
print("Видимость", data1['visibility'])
print("Скорость ветра", data1['wind']['speed'])



res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
data = res.json()

print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <", i['weather'][0]['description'], "> \r\nВидимость <", i['visibility'], "> \r\nСкорость ветра <", i['wind']['speed'] ,">")
    print("____________________________")
