import requests,json
api_key="5282b31811a61dbf567d528220f2dd8f"
city=input("Enter City:")
parameter={"q":city}
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
#print(url)
res=requests.get(url)
weather_data=json.loads(res.text)
#print(weather_data)
minTemp=weather_data['main']['temp_min']
maxTemp=weather_data['main']['temp_max']
print(minTemp,maxTemp)
