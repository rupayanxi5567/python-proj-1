from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pw = input("What's the master password? ")

key = load_key() + master_pw.encode()
fer = Fernet(key)





def see():
    # user_name = input("Enter your username: ")
    # pw = input("Enter your password to add it: ")

    with open("passwordss.txt", "r") as f:
        for lines in f.readlines():
            data = lines.rstrip()
            user, passw = data.split("|")
            print("User: " + user +"and Password: " + str(fer.decrypt(pw.encode())))
def add():
    user_name = input("Enter your username: ")
    pw = input("Enter your password to add it: ")

    with open("passwordss.txt", "a") as f:
        f.write(user_name + " | " + str(fer.encrypt(pw.encode())) + "\n")


while True:
    mode = input("Do you want to add a new password or see the existing passwords? (see, add), press 'q' to quit ").lower()

    if mode == "q":
        break;
    elif mode == "add":
        add()
    elif mode == "see":
        see()
    else:
        print("Invalid mode")
        continue
    
    
    
