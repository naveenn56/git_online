

import requests
response = requests.get(url = "https://www.gov.uk/bank-holidays.json")
js = response.json()

# Ask user for date
search_date = input("Enter date (YYYY-MM-DD): ")

# Access events list
events = js["england-and-wales"]["events"]

found = False

for event in events:
    if event["date"] == search_date:
        print("Title   :", event["title"])
        print("Bunting :", event["bunting"])
        print("Notes   :", event["notes"])
        found = True
        break

if not found:
    print("No event found for this date.")
