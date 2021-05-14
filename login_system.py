import sqlite3 
def home():
    print("[ LOGIN SYSTEM ]\n[ 0 ] Exit\n[ 1 ] LOGIN\n[ 2 ] SIGN UP")

def signup(userTableCursor):
    print("[ SIGN UP]")
    user_name = str(input("USERNAME >>"))
    while user_name and user_name.strip():
        store_username = userTableCursor.execute("SELECT usernames FROM users WHERE usernames=?",(user_name)).fetchall()
        if not store_username :
            password = password = str(input("PASSWORD >>"))
            userTableCursor.execute("INSERT INTO users values(?,?)",(user_name,password))
            userTableCursor.commit()
        else:
            print("username taken,please try again.")
            user_name = str(input("USERNAME >>"))        


def login(userTableCursor):
    print("[ LOGIN ]")
    user_name = str(input("USERNAME >>"))
    while user_name and user_name.strip():
        if user_name and user_name.strip(): #Check if username is not empty, if not empty continue to password
            password = str(input("PASSWORD >>"))
            Users = userTableCursor.execute("SELECT * FROM users WHERE usernames=? AND password=?",(user_name,password)).fetchall()
            print(Users)
            #if Users:
                #print("login successful!")
            #else:
                #print("login unsuccesful,try again.")
            
        else:
            user_name = str(input("USERNAME >>"))
        
        
        
        
        
def main():
    users = sqlite3.connect('users.db')
    database = users.cursor()
    
    home()
    user_input =  int(input("   >>"))
    if user_input == 0:
        print("Goodbye")
        exit(0)
    elif user_input == 1:
        login(database)  
    elif user_input == 2:
        exit(0)
    else:
        print("Invalid command")
        home()
    
if __name__=="__main__":
    main()    

    