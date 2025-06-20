from fastapi import FastAPI
from datetime import datetime
from dotenv import load_dotenv
import requests
import uvicorn
load_dotenv()

app = FastAPI()

CITY = "Douala"
API_KEY = "b56575bb2735754fa0455c45d4b5ed6e"


# on utilise openWeather pour nous donner meteo grace a API_KEY . https://openweathermap.org/
def get_weather():
    
    #Example de Weather Api endpoint
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(weather_url)
        data = response.json()
        
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
    except Exception as e:    
        weather = {
                'city': 'Unknown',
                'temperature': 'N/A',
                'description': 'Unable to get data'
            }
    return weather


@app.get("/info")
async def get_info():
    weather = get_weather()
    
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    formatted_time = current_datetime.strftime("%H:%M:%S")
    
    return{
        "date":formatted_date,
        "time": formatted_time,
        "weather":weather
    } 
     
       
    
    
    
    
    