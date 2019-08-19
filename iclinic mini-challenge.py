import requests
from datetime import datetime
import calendar

request = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=ribeirao+preto,br&APPID=9d3af2b9a21e18f86558b9b400c6986f')

request_json = request.json()
days = []
wet_days = []

for i in range(0,len(request_json['list'])):
    curr_date = datetime.strptime(request_json['list'][i]['dt_txt'], '%Y-%m-%d %H:%M:%S')
    curr_day = curr_date.date().day  
    
    if curr_day not in days:
        days.append(curr_day)
        
        humidity = request_json['list'][i]['main']['humidity']
        
        if humidity > 70:
            wet_days.append(calendar.day_name[curr_date.weekday()])
        
        
        
if not wet_days:
    print('No need for umbrellas in the coming days.')
else:
    print('You should take an umbrella in these days: %s.' % ', '.join(wet_days))