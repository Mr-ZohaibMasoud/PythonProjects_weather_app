import requests

def fetch_weather_data(city):
    
    key = "*************************"
    url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={city}"
    
    res = requests.get(url)

    wh_data = res.json()
    
    return wh_data
    

def res_handler(wh_data):
    
    print("**"*58)
    
    print(f"\nCity: {wh_data["location"]["name"]}, {wh_data["location"]["country"]} \n\n\tThe Weather is: {wh_data["current"]["condition"]["text"]} \n\tThe Temperature is: {wh_data["current"]["temp_c"]} \n\tThe Wind Speed is: {wh_data["current"]["wind_kph"]} \n\tThe Humidity is: {wh_data["current"]["humidity"]} \n\nat: {wh_data["location"]["localtime"]}\n")
    
    print("**"*58)
    


def main():
    
    print("\n\t\t**Wellcome to Weather Finder**\n")
    city = input("Enter The City to get weather: ")
    
    data = fetch_weather_data(city)
    
    res_handler(data)
    
    

if __name__ == "__main__":
    main()