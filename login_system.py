import sqlite3 ,getpass

def signup(userTableCursor):
    """add a user to the database after certain checks have been done"""
    
    print("[ SIGN UP]")
    user_name = str(input("USERNAME >> "))
    while user_name and user_name.strip():
        store_username = userTableCursor.execute("SELECT * FROM users WHERE usernames=?",(user_name,)).fetchall() #Check if username exists on database
        if not store_username:
            password = getpass.getpass("PASSWORD >> " )
            while password and password.strip():
                userTableCursor.execute("INSERT INTO users values(?,?)",(user_name,password)) #add the user to the database
                print("succesfully signed up")
                exit(0)
            else:
                print("password empty, please enter a valid password")
                password = str(getpass.getpass("PASSWORD >> ")) 
                if password and password.strip():
                    userTableCursor.execute("INSERT INTO users values(?,?)",(user_name,password)) 
                    print("succesfully signed up")
                    break   
                else:
                    print("Sign up unsuccesful,please start afresh")
                    print("goodbye")
                    exit(0)
                    
        else:
            print("username taken,please try again.")
            user_name = str(input("USERNAME >> ")) 
    else:
        print("username empty, please enter valid username")
    
    
def login(userTableCursor):
    """Check user against a database and grant/deny access based on the results,giving 
    the user 3 chances to enter correct password """
    print("[ LOGIN ]")
    user_name = str(input("USERNAME >> "))
    number_of_trials = 0 
    while user_name and user_name.strip():
        if number_of_trials == 0: # number_of_trials being greater than 0 means user has entered incorrect password atleast once
            
            if user_name and user_name.strip(): #Check if username is not empty, if not empty continue to password
                password = str(getpass.getpass("PASSWORD >> "))
                users_found = userTableCursor.execute("SELECT * FROM users WHERE usernames=? AND password=?",(user_name,password)).fetchall() 
                if users_found:
                    print("login successful!")
                    break
                else:
                    number_of_trials = number_of_trials+1
                    print("login unsuccesful,try again.")
        elif 0<number_of_trials<=2:
            user_name = str(input("USERNAME >> "))
            if user_name and user_name.strip():
                password = str(getpass.getpass("PASSWORD >> "))
                users_found = userTableCursor.execute("SELECT * FROM users WHERE usernames=? AND password=?",(user_name,password)).fetchall()
                if users_found:
                    print("login successful!")
                    break
                else:
                    number_of_trials = number_of_trials+1
                    print("login unsuccesful,try again..") 
        else:
            print("Please restart to attempt login,goodbye")
            exit(0)
    else: 
        print("Username empty,please enter valid username")  
    
    
def main():
    users = sqlite3.connect('users.db')
    database = users.cursor()
    
    print("[ LOGIN SYSTEM ]\n[ 0 ] Exit\n[ 1 ] LOGIN\n[ 2 ] SIGN UP")
    user_input =  input("   >>")
    if user_input == '0': # user input taken as string to accomodate users that may enter non-integer data
        print("Goodbye")
        exit(0)
    elif user_input == '1':
        login(database)  
    elif user_input == '2':
        signup(database)
    else:
        print("Invalid command...")
        main()
        
    users.commit()
    users.close()
if __name__=="__main__":
    main()    

    
