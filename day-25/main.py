import pandas

data = pandas.read_csv("./day-25/weather_data.csv")

# print(data["condition"])

print(data[data["day"] == "Monday"])
