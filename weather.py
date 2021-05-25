import requests

# https://openweathermap.org/current


def get_weather_desc_and_temp():
    api_key = "e6e36b219097e5fe1459ef8404858336"
    city = "warsaw"
    url = (
        "http://api.openweathermap.org/data/2.5/weather?q="
        + city
        + "&appid="
        + api_key
        + "&units=metric"
    )

    response = requests.get(url)
    json = response.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {"description": description, "temp_min": temp_min, "temp_max": temp_max}


def main():
    weather_dict = get_weather_desc_and_temp()
    # Print the results
    print("Today's forecast is", weather_dict.get("description"))
    print("Min temperature:", weather_dict.get("temp_min"))
    print("Max temperature:", weather_dict.get("temp_max"))


main()
