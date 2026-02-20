from dotenv import load_dotenv
from pprint import pprint
import requests 
import os

load_dotenv()

def get_current_weather(city = "gorakhpur city"):
          try:
               api_key = os.getenv('API_KEY')
               if not api_key:
                    return {"cod": "401", "message": "API key not found in .env file"}
               
               requests_url = f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=imperial"
               
               response = requests.get(requests_url, timeout=5)
               weather_data = response.json()
               return weather_data
          except requests.RequestException as e:
               return {"cod": "503", "message": f"Network error: {str(e)}"}
          except Exception as e:
               return {"cod": "500", "message": f"Error: {str(e)}"}

if __name__ == "__main__":
          print("\n***get current weather condition***\n")

          city = input("\nEnter city name: ")

          #check for empty string and strings with only whitespace
          if not bool(city.strip()):
               city = "gorakhpur city"

          weather_data = get_current_weather(city)

          print("\n" )
          pprint(weather_data)    