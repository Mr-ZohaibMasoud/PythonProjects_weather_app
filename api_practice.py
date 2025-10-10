import requests

def get_user(id):
    
    url = f"https://api.freeapi.app/api/v1/public/randomusers/{id}"
    headers = {"accept": "application/json"}
    
    response = requests.get(url, headers=headers)
    data = response.json()
    
    return data
    
def data_handler(data):
    pass
    
    
def main():
    
    print("Get Users...\n")
    
    id = int(input("Enter User NUmber: "))
    
    user_data = get_user(id)
    print(f"The name is: {user_data["data"]["name"]["title"]} {user_data["data"]["name"]["first"]} {user_data["data"]["name"]["last"]}")
    
    
if __name__ == "__main__":
    main()