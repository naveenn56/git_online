import requests
def whole():
    ask = (input("Enter the any number (below 826) to find ricky and monty character: "))
    str = int(ask)
    url = f"https://rickandmortyapi.com/api/character/{ask}"
    if str <=826 and str != 0:
        response = requests.get(url)

        # convert to json dict
        data = response.json()

        print("Name:", data["name"])
        print("Status:", data["status"])
        print("Species:", data["species"])
        print("Gender:", data["gender"])
        print("Origin:", data["origin"]["name"])
        print("Location:", data["location"]["name"])
        print("Image:", data["image"])
        print("Created:", data["created"])
    else:
        print("please enter the valid input")
        whole()
whole()



