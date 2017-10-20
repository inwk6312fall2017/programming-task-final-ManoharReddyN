from weather import weather
weather = Weather()

location = weather.lookup_by_location('Halifax')
condition = location.condition('Halifax')
print(condition['text'])

forecast = location.forecast()
hightemp=[]
lowtemp=[]
print("current weather is ", condition['text'])
print("current temperature ",condition['temp'])
print("weather for the next 5 days")
for forecasts in location.forecast():
        hightemp = forecasts['high']
        lowtemp = forecasts['low']
        rain= forecast['text']
        if forecasts['text']== "Rain":
                print ("the day it will rain is",forecasts['day'])

