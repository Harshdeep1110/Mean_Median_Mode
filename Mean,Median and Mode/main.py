import csv 
with open ("SOCR-HeightWeight.csv",newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

weight_data = []

for i in range(len(file_data)):
    weight = file_data[i][2]
    weight_data.append(float(weight)) 

total_elements = len(weight_data)
total = 0

for i in weight_data:
    total = total + i

mean = total/total_elements

print("The mean of the following weights is ",mean)
