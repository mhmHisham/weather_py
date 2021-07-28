import requests
from datetime import datetime

api_key = 'f71ff3a075d892969ee45022096ab5f3'
location = input("Enter the city : ")

# get json data from weather api
api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
api_data = requests.get(api_link).json()

city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-------------------------------------------------------------")
print("Weather Stats for " + (location.upper() + " || " + date_time))
print("-------------------------------------------------------------")

print(" temperature in " + location.capitalize() + "         : {:.2f} °C".format(city))
print(" weather description of " + location.capitalize() + " :", weather_desc)
print(" Humidity in " + location.capitalize() + "            :", hmdt, '%')
print(" wind speed in " + location.capitalize() + "          :", wind_spd * 0.539957, 'knots')

print("====================================================")

# making a list so that i can print the info to a txt
txtlist = [city, weather_desc, hmdt, wind_spd, date_time]
# using open() buit-in function to write to a text file
with open("textfile.txt", mode='w', encoding='utf-8') as f:
    # encoding = utf-8 for linux and cp1252 for win
    f.write("------------------------------------------------------------- \n ")
    f.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    f.write("\n ------------------------------------------------------------- \n")
    f.write("Current temperature is: {:.2f} deg C\n".format(txtlist[0]))

    f.write("{},{} \n".format("Current weather desc  :", txtlist[1]))
    f.write("{},{},{} \n".format("Current Humidity      :", txtlist[2], "%"))
    f.write("{},{},{} \n".format("Current wind speed    :", txtlist[3], "kmph"))
    f.write("====================================================")
