import csv

#Create dictionary from csv file
file = 'employees.csv'
header = []
emp_list = []

with open(file, 'r', encoding='utf-8-sig') as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)
    header = data[0]
    for row in data[1:]:
        emp_list.append(row)


#Dictionary
dict_keys = [emp[0] for emp in emp_list]
dict_values = [emp[1:] for emp in emp_list]

for dict in dict_values:
    dict[2] = int(dict[2])
    dict[5] = int(dict[5])
    dict[6] = int(dict[6])
emp_dict = {int(k):v for k,v in list(zip(dict_keys, dict_values))}

len_name = 0
for value in emp_dict.values():
    name = len(value[0]) 
    if len_name < name:
        len_name = name
    else:
        continue

print(len_name)
def print_format():
    len_gender = 4
    len_age = 4
    len_salary = 10
    print(f'{header[0]:<5}{header[1]:<20}{header[2]:<{len_gender}}')
        
    
print_format()