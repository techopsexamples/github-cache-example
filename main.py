# main.py
import requests

def fetch_data(url):
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos/1"
    data = fetch_data(url)
    print(data)