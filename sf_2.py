from datetime import datetime
import requests

#Api

def fetch_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }
    
    try:
        # Step A: Send GET request with a 10-second timeout safety net
        response = requests.get(url, params=params, timeout=10)
        
        # Step B: Raise an exception if HTTP status code is NOT 200 OK (e.g., 404, 500)
        response.raise_for_status()
        
        # Step C: Parse raw JSON response into a Python dictionary
        return response.json()

    except requests.exceptions.Timeout:
        print("Error: Connection timed out. Check your internet connection.")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error encountered: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Network Error encountered: {req_err}")
    return None

#Report file
def save_weather_report(data):
    if not data:
        print("No data received to write the report.")
        return

    # Step A: Extract metrics using .get() to avoid KeyError crashes
    timezone = data.get("timezone", "Unknown")
    current = data.get("current_weather", {})
    
    temp = current.get("temperature", "N/A")
    windspeed = current.get("windspeed", "N/A")
    weathercode = current.get("weathercode", "N/A")

    # Step B: Format dynamic filename with current date: py_sf_YYYY-MM-DD.txt
    today_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"py_sf_{today_str}.txt"

    # Step C: Format output text
    report_content = (
        f"========================================\n"
        f"        WEATHER REPORT ({today_str})\n"
        f"========================================\n"
        f"Timezone:    {timezone}\n"
        f"Temperature: {temp} °C\n"
        f"Windspeed:   {windspeed} km/h\n"
        f"Weathercode: {weathercode}\n"
        f"========================================\n"
    )

    # Step D: Save file safely using 'with open' context manager
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(report_content)
        print(f"Success! Report saved directly to '{filename}'")
    except IOError as e:
        print(f"File Writing Error: {e}")


#Entry point
def main():
    # Example coordinates (Thane region: Lat 19.2, Lon 72.9)
    latitude, longitude = 19.2, 72.9
    
    print(f"Fetching weather data for Lat: {latitude}, Lon: {longitude}...")
    weather_data = fetch_weather(latitude, longitude)
    
    if weather_data:
        save_weather_report(weather_data)

if __name__ == "__main__":
    main()