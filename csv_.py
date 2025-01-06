# import csv

# students =[]

# with open("name.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"Name": row["name"], "Home": row["home"]})

# for student in sorted(students, key = lambda student : student["Name"]):
#     print(f"{student['Name']} is from {student['Home']}")





# import csv 
# name = input("What's your name? ")
# home = input("Where's your? ")

# with open("name.csv","a") as file:
#     writer = csv.DictWriter(file,fieldnames=["name","home"])
#     writer.writerow({"name": name, "home": home})

