import csv

my_list = [
    ["Top Gun", "Risky Business", "Minority Report"],
    ["Titanic", "The Revenant", "Inception"], 
    ["Training Day", "Man on Fire", "Flight"]
    ]

with open("movies.csv", "w") as f:
    write = csv.writer(f, delimiter=",")
    for list in my_list:
        write.writerow(list)
