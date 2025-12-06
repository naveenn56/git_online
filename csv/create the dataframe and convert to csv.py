import pandas as pd
raw_data =  {
    "family" : ["naveen", "gokul", "lakshmi", "ramasamy"],
    "age" : [24,20,45, 50]
}

create_to_dataframe = pd.DataFrame(raw_data)   # this keyword to create the data frame pd.DataFrame
dataframe_to_csvfie = create_to_dataframe.to_csv()  # this keyword to change raw to  data frame .to_csv()



create_to_dataframe.to_csv("saveas.csv", index=False) # this keyword as the file to floder the CSV

