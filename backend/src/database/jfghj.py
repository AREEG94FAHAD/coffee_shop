import sqlite3  
  
con = sqlite3.connect("/var/www/html/database/employee.db")  
print("Database opened successfully")  
  
# con.execute("INSERT into employees (name, email, address) values (?,?,?)",('name','emai99l','address'))  
# con.commit()  
conn= con.execute('select * from employees')
for i in conn:
    print(i)
  
print("Table created successfully")  
  
con.close()  