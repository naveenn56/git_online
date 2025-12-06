import requests
url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)
data = response.json()
b = data["type"]
c = data["setup"]
d = data["punchline"]
a = data["id"]
print(f" {a}\n")
print(f"{b}\n")
print(f"{c}\n")
print(f"{d}\n")




