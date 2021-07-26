import csv
from collections import Counter

with open ('SOCR-HeightWeight.csv',newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

weight_list= []

for i in range(len(file_data)):
    weight = file_data[i][2]
    weight_list.append(weight)

data = Counter(weight_list)
mode_data_range = {
    '50-60':0,'60-70':0,'70-80':0
}

for weight, occurence in data.items():
    if(50 < float(weight)<60):
        mode_data_range['50-60']+= occurence
    elif(60 < float(weight)< 70):
        mode_data_range['60-70']+= occurence
    elif(70 < float(weight)< 80):
        mode_data_range['70-80']+= occurence

mode_range, mode_occurence = 0,0

for range,occurence in mode_data_range.items():
    if(occurence>mode_occurence):
        mode_range, mode_occurence = [int(range.split('-')[0]),int(range.split('-')[1])],occurence

mode = float((mode_range[0]+mode_range[1])/2)

print("The mode of the weights is ", mode)