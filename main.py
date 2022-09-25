import pandas
import csv

import pandas as pd

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
first_column = (data.iloc[0])



gray_squirrels = len(data[data["Primary Fur Color"] == "Gray" ])
cinamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels)
print(cinamon_squirrels)
print(black_squirrels)

data_dictonary = {
    "Fur Color": ["Gray", "Cinamon", "Black"],
    "Count": [gray_squirrels, cinamon_squirrels, black_squirrels],
}
my_data_csv = pd.DataFrame.from_dict(data_dictonary)
my_data_csv.to_csv("my_data_csv.csv")












