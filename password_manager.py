from cryptography.fernet import Fernet

# key + password + text to encrypt = random text
# random text + key + password = test to be encrypted
'''
def write_key():
     key = Fernet.generate_key() #The Fernet.generate_key() method generates a new random key. This key is a URL-safe base64-encoded 32-byte key, which will be used for encryption and decryption.
    with open("key.key", "wb") as key_file: # opens a file named "key.key" in write-binary mode ("wb"). This means the file is opened for writing, and any existing content will be truncated (i.e., erased). The with statement ensures that the file is properly closed after the block of code is executed, even if an exception is raised.
        key_file.write(key) #writes the generated key to the file. Since the key is in binary format (bytes), it matches the mode in which the file is opened ("wb"). 
write_key()'''  

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

# master_pwd = input("What is the master password")
key = load_key() 
fer = Fernet(key)
def view():
    with open ('password.txt', 'r') as f:
         for line in f.readlines(): #read lines in a file
            # print(line.rstrip()) 
            data = line.rstrip()
            user , passw = data.split("|") 
            print("User :", user, "| Password :" , passw, fer.decrypt(passw.encode()).decode())
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open('password.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
while True:
    mode = input("Would you like to add a new password or view existing ones(view/add/q)? ").lower()
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == "add":
        add()
    else :
        print("Invalid mode.")
        continue