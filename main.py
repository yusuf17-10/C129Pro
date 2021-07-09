import csv

data_1 = []
data_2 = []

with open("bright_stars.csv","r")as f:
    csvReader = csv.reader(f)

    for i in csvReader:
        data_1.append(i)

with open("brown_dwarf_stars.csv","r")as f:
    csvReader = csv.reader(f)

    for i in csvReader:
        data_2.append(i)


headers_1 = data_1[0]
stars_data_1 = data_1[1:]

headers_2 = data_2[0]
stars_data_2 = data_2[1:]

print(headers_1)
print(headers_2)

headers = headers_1+headers_2

print(headers)

stars_data = []

for i in stars_data_1:
    stars_data.append(i)

for j in stars_data_2:
    stars_data.append(j)

with open("data_set2_merged.csv","w")as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(stars_data)




