import csv 
with open("routers.csv") as data: 
    csv_list = csv.reader(data) 
    for row in csv_list: 
     device = row[2] 
     location = row[1] 
     ip = row[1] 
     print(f"{device} is in {location.rstrip()} and has IP {ip}.")