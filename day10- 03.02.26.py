#For this lab, imagine you are an IT Specialist at a medium-sized company. 
# The Human Resources Department at your company wants you to find out how many people are in each department.
#  You need to write a Python script that reads a CSV file containing a list of the employees in the organization,
#  counts how many people are in each department, and then generates a report using this information. 
# 
# The output of this script will be a plain text file.


# git init
# git add .
# git commit -m "mesaj"
# git branch -M master
# git push -u origin master
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

import csv
import os
accounts = [
    ["Full Name", "Username", "Department"],
    ["Audrey Miller", "audrey", "Development"],
    ["Arden Garcia", "ardeng", "Sales"],
    ["Bailey Thomas", "baileyt", "Human Resources"],
    ["Blake Sousa", "sousa", "IT infrastructure"],
    ["Cameron Nguyen", "nguyen", "Marketing"],
    ["Charlie Grey", "greyc", "Development"],
    ["Chris Black", "chrisb", "User Experience Research"],
    ["Courtney Silva", "silva", "IT infrastructure"],
    ["Darcy Johnsonn", "darcy", "IT infrastructure"],
    ["Elliot Lamb", "elliotl", "Development"],
    ["Emery Halls", "halls", "Sales"],
    ["Flynn McMillan", "flynn", "Marketing"],
    ["Harley Klose", "harley", "Human Resources"],
    ["Jean May Coy", "jeanm", "Vendor operations"],
    ["Kay Stevens", "kstev", "Sales"],
    ["Lio Nelson", "lion", "User Experience Research"],
    ["Logan Tillas", "tillas", "Vendor operations"],
    ["Micah Lopes", "micah", "Development"],
    ["Sol Mansi", "solm", "IT infrastructure"]
]




# with open ('employees.csv','w') as f:
#     writer = csv.writer(f,lineterminator='\n')
#     writer.writerows(accounts)
csv_path = os.path.abspath('employees.csv')
print(csv_path)

def read_employees(csv_file_location):
    csv.register_dialect('empdialect',skipinitialspace=True,strict=True)
    file = csv.DictReader(open(csv_file_location),dialect='empdialect')
    employee_list= []
    for row in file:
        employee_list.append(dict(row))
    return employee_list
emp_dict = read_employees('employees.csv')
print(emp_dict)

# The second function process_data() should now receive the list of dictionaries, 
# i.e., employee_list as a parameter and return a dictionary of department:amount.

def process_data(dict_list):
    dept_amnts={}
    for dicts in dict_list:
        # {'Full Name': 'Audrey Miller', 'Username': 'audrey', 'Department': 'Development'}
        
        pass

process_data(emp_dict)