import datetime as dt

import mysql.connector
import mysql.connector.errors as error

# Starts up connection with mysql
def connection_init():
    config = {
        "host": "127.0.0.1",
        "user": "root",
        "password": "password",
    }

    try: cnx = mysql.connector.connect(**config)
    except: print("Some kind of weird error happened.")
        
    return cnx

# Shortcut to running multiple commands at once
def run_commands(cmd_list):
    for cmd in cmd_list:
        try: cursor.execute(cmd)
        except error.DatabaseError as err:
            print(err)

def database_init():
    
    # Incase I want to reset database 
    # try: cursor.execute("DROP DATABASE banking;")
    # except: 
    #     print("Database banking does not exist or could not be deleted.")
    #     return False
        
    try: cursor.execute("CREATE DATABASE banking;")
    except error.DatabaseError as err:
        return False


    table_init_list = [
        "USE banking;",
        
        "CREATE TABLE users ("
        "id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
        "email VARCHAR(250) NOT NULL UNIQUE,"
        "hash VARCHAR(500) NOT NULL"
        ");",
        
        "CREATE TABLE user_data ("
        "id INT NOT NULL PRIMARY KEY,"
        "name VARCHAR(250) NOT NULL,"
        "birthdate DATE NOT NULL,"
        "acc_created DATE NOT NULL,"
        "balance DEC(50, 2) NOT NULL DEFAULT 0,"
        "FOREIGN KEY (id) REFERENCES users(id)"
        "ON UPDATE CASCADE ON DELETE CASCADE);",
    ]    
    
    describe_table_cmds = [
        "DESC users;",
        "DESC user_data;"
    ]

    run_commands(table_init_list)
            
    return True
            
      
def add_user(email, hash, name, birthdate):    
    cursor.execute("USE banking;")
    acc_created = dt.datetime.now().strftime("%Y-%m-%d")
    
    cursor.execute("INSERT INTO users (email, hash) VALUES (%s, %s);", (email, hash))
    
    cursor.execute("SELECT id FROM users WHERE email = %s;", (email, ))
    for i in cursor:
       id = i[0]
    
    cursor.execute("INSERT INTO user_data (id, name, birthdate, acc_created) VALUES (%s, %s, %s, %s)", (id, name, birthdate, acc_created))
    return id 
    
def delete_user(id):
    cursor.execute("USE banking;")
    cursor.execute("DELETE FROM users WHERE id=%s;", (id, ))

# Flexible function to update user info based on parameters and arguments passed in
def update_info(id, **kwargs):
    cursor.execute("USE banking;")
    
    for key in kwargs.keys():
        if key in ["email", "hash"]:
            if key == "email":
                cursor.execute("UPDATE users SET email=%(key_val)s WHERE id=%(id)s;", 
                    {"key_val": kwargs.get(key), "id": id})
            else:
                cursor.execute("UPDATE users SET hash=%(key_val)s WHERE id=%(id)s;", 
                    {"key_val": kwargs.get(key), "id": id})
        else:
            if key == "name":
                cursor.execute("UPDATE user_data SET name=%(key_val)s WHERE id=%(id)s;", 
                        {"key_val": kwargs.get(key), "id": id})
            elif key == "birthdate":
                cursor.execute("UPDATE user_data SET birthdate=%(key_val)s WHERE id=%(id)s;", 
                        {"key_val": kwargs.get(key), "id": id})
            elif key == "acc_created":
                cursor.execute("UPDATE user_data SET acc_created=%(key_val)s WHERE id=%(id)s;", 
                        {"key_val": kwargs.get(key), "id": id})
            elif key == "balance":
                cursor.execute("UPDATE user_data SET balance=%(key_val)s WHERE id=%(id)s;", 
                        {"key_val": kwargs.get(key), "id": id})
 
        
# Flexible function to get requested user info based on arguments passed in. returns a dictionary   
def get_info(id, *columns):
    cursor.execute("USE banking;")
    info = {}
    
    for col in columns:
        if col in ["email", "hash"]:
            if col == "email":
                cmd = "SELECT email FROM users WHERE id = %(id)s"
                cursor.execute(cmd, {"id": id})
            else:
                cmd = "SELECT hash FROM users WHERE id = %(id)s"
                cursor.execute(cmd, {"id": id})
        else:
            if col == "name":
                cmd = "SELECT name FROM user_data WHERE id = %(id)s"
                cursor.execute(cmd, {"id": id})
            elif col == "birthdate":
                cmd = "SELECT birthdate FROM user_data WHERE id = %(id)s"
                cursor.execute(cmd, {"id": id})
            elif col == "acc_created":
                cmd = "SELECT acc_created FROM user_data WHERE id = %(id)s"
                cursor.execute(cmd, {"id": id})
            elif col == "balance":
                cmd = "SELECT balance FROM user_data WHERE id = %(id)s"
                cursor.execute(cmd, {"id": id})
        
        for data in cursor:
            info[col] = data[0]
            
    return info if len(info) > 0 else None

# Used to get id from unique email value
def get_id(email):
    cursor.execute("USE banking;")
    cursor.execute("SELECT id FROM users WHERE email=%s;", (email,))
    
    for data in cursor:
        id = data[0]
        
        return id if id > 0 else None 

# Gets all emails. Used in transactions tab to populate email dropdown
def get_all_emails():
    names = []
    cursor.execute("USE banking;")
    cursor.execute("SELECT email FROM users;")
    
    for data in cursor:
        names.append(data[0])
        
    return names if len(names) > 0 else None

# This is where database is initialized for whole app
cnx = connection_init()
cnx.autocommit = True
cursor = cnx.cursor()
database_init()