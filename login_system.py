import sqlite3 ,getpass
import hashlib
import os
from codecs import encode

def signup(userTableCursor):
    """add a user to the database after certain checks have been done"""
    
    print("[ SIGN UP]")
    user_name = str(input("USERNAME >> "))
    while user_name and user_name.strip():
        store_username = userTableCursor.execute("SELECT * FROM users WHERE usernames=?",(user_name,)).fetchall() #Check if username exists on database
        if not store_username:
            password = getpass.getpass("PASSWORD >> " )
            while password and password.strip():
                salt = os.urandom(32)    # generate a random byte string to use during hashing
                key =  hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000) #generates a hashcode with the salt generated above                
                userTableCursor.execute("INSERT INTO users values(?,?,?)",(user_name,key,salt)) #add the user to the database
                print("succesfully signed up")
                return
            else:
                print("password empty, please enter a valid password")
                password = str(getpass.getpass("PASSWORD >> ")) 
                if password and password.strip():
                    salt = os.urandom(32)   
                    key =  hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)                     
                    userTableCursor.execute("INSERT INTO users values(?,?,?)",(user_name,key,salt)) 
                    print("succesfully signed up")
                    return 
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
                salt= userTableCursor.execute("SELECT salt FROM users WHERE usernames=?",(user_name,)).fetchall() #get salt that corresponds to entered username
                if salt:
                    stored_salt = salt[0]
                    stored_salt = str(stored_salt)[3:len(str(stored_salt))-3]
                    #print("This is stored salt 1 \n"+stored_salt)
                    stored_salt = encode(stored_salt.encode().decode('unicode_escape'),"raw_unicode_escape")# byte encode the salt retrieved from database
                    enter_password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), stored_salt, 100000)
                    users_found = userTableCursor.execute("SELECT * FROM users WHERE usernames=? AND key=?",(user_name,enter_password_hash)).fetchall() 
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
                salt= userTableCursor.execute("SELECT salt FROM users WHERE usernames=?",(user_name,)).fetchall() #get salt from database and  
                #print("This is the salt:\n",salt)
                key = userTableCursor.execute("SELECT key FROM users WHERE usernames=?",(user_name,)).fetchall()
                print(key)
                if salt:
                    stored_salt = salt[0]
                    stored_salt = str(stored_salt)[3:len(str(stored_salt))-3]
                    #print("This is stored salt 1 \n"+stored_salt)
                    stored_salt = encode(stored_salt.encode().decode('unicode_escape'),"raw_unicode_escape")
                    enter_password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), stored_salt, 100000)
                    users_found = userTableCursor.execute("SELECT * FROM users WHERE usernames=? AND key=?",(user_name,enter_password_hash)).fetchall()
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

