import sqlite3 
def home():
    print("[ LOGIN SYSTEM ]\n[ 0 ] Exit\n[ 1 ] LOGIN\n[ 2 ] SIGN UP")

def signup(userTableCursor):
    """add a user to the database after certain checks have been done"""
    print("[ SIGN UP]")
    user_name = str(input("USERNAME >>"))
    while user_name and user_name.strip():
        store_username = userTableCursor.execute("SELECT * FROM users WHERE usernames=?",(user_name,)).fetchall() #Check if username exists on database
        if not store_username : # if the store_username list is empty, username has not been taken
            password = str(input("PASSWORD >>"))
            if password and password.strip():     # Try not to allow empty passwords into the table
                userTableCursor.execute("INSERT INTO users values(?,?)",(user_name,password)) #add the user to the database
                print("succesfully signed up")
                break
            else:
                print("invalid password,please try again.")
                password = password = str(input("PASSWORD >>"))
                userTableCursor.execute("INSERT INTO users values(?,?)",(user_name,password)) 
                print("succesfully signed up")
        else:
            print("username taken,please try again.")
            user_name = str(input("USERNAME >>"))
    main()
    


def login(userTableCursor):
    """Check user against a database and grant/deny access based on the results"""
    print("[ LOGIN ]")
    user_name = str(input("USERNAME >>"))
    count = 0 
    while user_name and user_name.strip():
        if count == 0: # count being greater than 0 means user has entered incorrect username/password atleast once
            if user_name and user_name.strip(): #Check if username is not empty, if not empty continue to password
                password = str(input("PASSWORD >>"))
                Users = userTableCursor.execute("SELECT * FROM users WHERE usernames=? AND password=?",(user_name,password)).fetchall()
                if Users:
                    print("login successful!")
                    break
                else:
                    count = count+1
                    print("login unsuccesful,try again.")
            
        else:
            user_name = str(input("USERNAME >>"))
            if user_name and user_name.strip():
                password = str(input("PASSWORD >>"))
                Users = userTableCursor.execute("SELECT * FROM users WHERE usernames=? AND password=?",(user_name,password)).fetchall()
                print(Users)
                if Users:
                    print("login successful!")
                    break
                else:
                    count = count+1
                    print("login unsuccesful,try again.")            
                    
def main():
    users = sqlite3.connect('users.db')
    database = users.cursor()
    
    home()
    user_input =  input("   >>")
    if user_input == '0':
        print("Goodbye")
        exit(0)
    elif user_input == '1':
        login(database)  
    elif user_input == '2':
        signup(database)
    else:
        print("Invalid command")
        main()
        
    users.commit()
    users.close()
    
    
if __name__=="__main__":
    main()    

    