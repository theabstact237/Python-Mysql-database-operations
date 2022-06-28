import mysql.connector
import json
import collections
from datetime import date


#start connecting my script to a mysql instance  
mydb = mysql.connector.connect(
  host=" 127.0.0.1",
  user="root",
  password="",
  database="employees"
)

mycursor = mydb.cursor()
# print("Let me grant you some priviledges \n")
# mycursor.execute("GRANT INSERT, SELECT, DELETE, UPDATE ON Employees.* TO 'root'@'127.0.0.1' IDENTIFIED BY '';")
# print("Priviledges granted \n ")
# print("Do you want to create the database of employee \n")
# answer =input("enter (y) for yes and (n) for no: ")
# if answer =='y':
#     mycursor.execute("CREATE TABLE employee (matricule_number VARCHAR(255) FOREIGN KEY ,name VARCHAR(255),first_name VARCHAR(255),month_total INT);")
# else:
#     exit()
# mycursor.execute("CREATE TABLE Employee (matricule_number VARCHAR(255) PRIMARY KEY,name VARCHAR(255),first_name VARCHAR(255),month_total INT);")
# mycursor.execute("CREATE TABLE List_of_operation (matricule_number VARCHAR(255),code_name VARCHAR(255) PRIMARY KEY,job_name VARCHAR(255),cost_per_hour INT,total_hour INT,job_cost INT,FOREIGN KEY(matricule_number) REFERENCES Employee(matricule_number) );")

# queryEmployee="INSERT INTO employee (matricule_number,name,first_name,month_total) VALUES (%s,%s,%s,%s)"
# matricule_number = input("enter the matricule number:\n")
# name = input("\n enter the employee's name: ")
# first_name = input("\n enter the first name: ")
# month_total = input("\n enter the total of the month: ")
# values = (matricule_number,name,first_name,month_total)
# mycursor.execute(queryEmployee,values)
# mydb.commit()

# queryOperations="INSERT INTO list_of_operation (matricule_number,code_name, job_name, cost_per_hour, total_hour, job_cost) VALUES (%s,%s, %s,%s, %s, %s)"
# matricule_number = input("enter the matricule number:\n")
# code_name = input("enter the code name:\n")
# job_name = input("enter the job name: ")
# cost_per_hour = input("enter the cost per hour: ")
# total_hour = input("enter the total hour: ")
# job_cost = input("enter the job cost: ")

# values =(matricule_number,code_name,job_name,cost_per_hour,total_hour,job_cost)
# mycursor.execute(queryOperations,values)
# mydb.commit()

querySelector = "SELECT * FROM Employee"

mycursor.execute(querySelector)
rows = mycursor.fetchall()
rowarray_list = []
for row in rows:
  d = collections.OrderedDict()
  d['matricule_number'] = row[0]
  d['name'] = row[1]
  d['first_name'] = row[2]
  d['month_total'] = row[3]
  rowarray_list.append(d)
 
querySelect = "SELECT * FROM List_of_operation"
mycursor.execute(querySelect) 
rows = mycursor.fetchall()
rowarray_list2 = []
for row in rows:
  e = collections.OrderedDict()
  e['matricule_number'] = row[0]
  e['code_name'] = row[1]
  e['job_name'] = row[2]
  e['cost_per_hour'] = row[3]
  e['total_hour'] = row[4]
  e['job_cost'] = row[5]
  rowarray_list2.append(e)
j = json.dumps(rowarray_list + rowarray_list2)
f = open("employee.json",'w')

f.write(j)

f.close()



#The portion of the code that is writing the date of today at the beginning of the json file
today = date.today()
d2 = today.strftime("%B %d, %Y")

f = open("employee.json",'r+')
lines = f.readlines()
f.seek(0)
f.write(d2)
for line in lines:
    f.write(line)

f.close()
