from weather import weather
weather = Weather()
location = Location()

lookup = weather.lookup(560743)
condition = lookup.condition()
print(condition['text']

location = weather.lookuplocation('dublin')
condition = location.condition()
print(condition['text'])


forecasts = location.forecast()
for forecast in forecasts:
    print(forecasts.text())
    print(forecasts.date())
    print(forecasts.high())
    print(forecasts.low())
