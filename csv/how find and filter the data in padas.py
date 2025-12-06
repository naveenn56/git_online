import pandas as pd
data = pd.read_csv("weather.csv")


fter_sunny =(data[data["condition"] == "sunny"])
print(fter_sunny)


fter_sunnyoftemp = (data[data["condition"] == "sunny"]["temp"])
print(fter_sunnyoftemp)