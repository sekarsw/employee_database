'''
This is a modified database based on the Employees Sample Database from MySQL.


Primary Key: ID
Name
Gender
Age
Job Title: Manager, Senior Staff, Staff, Engineer, Senior Engineer, Analyst, Senior Analyst
Department: Finance, Marketing, IT, Production, Sales, HR
Salary
Experience
'''
import csv

file = 'employees.csv'
header = []
emp_list = []

with open(file, 'r') as f:
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
print(emp_dict)