'''
Name, Department, Job Title, Age, Gender, Salary in $, Yearly Bonus -> 0 -> will be calculated later
'''

cols = ['ID', 'Name', 'Department', 'Job Title', 'Age', 'Gender', 'Salary ($)'  'Yearly Bonus']
emplst = [110101, 'Adam', 'Marketing', 'Marketing Analyst', 35, 'M', 40000, 0]
empdict = {k:v for k, v in list(zip(cols, emplst))}
empnest = {110101 : ['Adam', 'Marketing', 'Marketing Analyst', 35, 'M', 40000, 0] }


