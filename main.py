import requests
s_city="Moscow,Ru"
appid="c92fbfcea52a7495aa212eb294630d14"
res=requests.get("http://api.openweathermap.org/data/2.5/weather",params={'q':s_city,'units':'metric','lang':'ru','APPID':appid})
data=res.json()

print("Город: {}".format(s_city))
print("Погодные условия: {}".format(data['weather'][0]['description']))
print("Температура: {}".format(data['main']['temp']))
print("Мин температура: {}".format(data['main']['temp_min']))
print("Макс температура: {}".format(data['main']['temp_max']))
print("Видимость: {} м".format(data['visibility']))
print("Скорость ветра: {} м\с".format(data['wind']['speed']))
print("______")
res=requests.get("http://api.openweathermap.org/data/2.5/forecast",params={'q':s_city,'units':'metric','lang':'ru','APPID':appid})
data=res.json()

for i in data['list']:
    print("Дата {} \n Температура {} \n Погодные условия {}".format(i['dt_txt'],i['main']['temp'],i['weather'][0]['description']))
    print("______")

      
