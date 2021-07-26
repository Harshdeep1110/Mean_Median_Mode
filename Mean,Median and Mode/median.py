import csv
with open ('SOCR-HeightWeight.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

weight_list = []

for i in range(len(file_data)):
    weight = file_data[i][2]
    weight_list.append(weight)

total_elements = len(weight_list)
weight_list.sort()

if(total_elements%2 == 0):
    median1 = float(weight_list[total_elements//2])
    median2 = float(weight_list[total_elements//2-1])
    median = (median1+median2)/2
else:
    median = float(weight_list[total_elements//2])

print("The median of the given weights is ", median)
