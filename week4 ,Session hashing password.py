
import hashlib 
print ("Welcome to our manger password!")
#creat empaty dictionary to store the user name
passwords ={}

def hash_password(password):
#hash the password by sha256 algorithem  
  hash_password = hashlib.sha256(password.encode()).hexdigest()
  return hash_password


#asking the user to save username using the program
while True:
  website = input("Please enter a website/application you want to store a password for:")
  password=input (f"please enter password for:{website}")
  secure_password=hash_password(password)
  passwords[website]=secure_password
  print ("password saved successfully")
  
  
  
  another= input("Do you want to save another website/password? [yes/no]")
  if another == 'no':
    print("thank you")
   #print(passwords)
    break
  
  
 #ask the user to check what they are entered 
while True:  
  website_to_check = input("Please enter website or application you want to check:") 
  if website_to_check in passwords:
     entered_password =  input(f"please enter your password for{website_to_check}")
     secure_entered_password= hash_password(entered_password)
     if passwords[website_to_check]==secure_entered_password:
        print("password correct")
     else:
        print ("Incorect password")
  else:
    print("No password stored for that website/application!")
    
  another= input("Do you want to check another website/password? [yes/no]")
  if another == 'no':
    print("thank you")
   
    break  

