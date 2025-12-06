import pandas as pd
data = pd.read_csv("weather.csv")

mt = data.loc[data.day == "Monday", ["temp"]]
print(mt)
