
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


""" 
 # to add a name candidian
  if action == '1':
     
    vote = input("Available candidates:\n'1.'Alice ,\n'2.'Bob,\n'3.'Charli,\n press enter to continue")
  break
  

vote={} 

 
 vote = input ("Enter the candidate ID you wish to vote for ")
 secure_vote = hash_vote(vote)
 print (secure_vote)

 

if action =='2':
 sum_votes = sum(votes)
    
  
     


if action == '3' :
    print ("you have chosen to quit , Good bye")
     
else:
    print("you have chosen a wrong number. Try again! ")
    
   
    # loop over tasks to disply them 
 for i in range(len(votes)):
      print(f"{i+ 1}.[{'x' if votes [i]['complete'] else ' '}] {votes[i]['vote']}")
    
      
 else :
      print ("No tasks on the list") 
      

   
    
 if action == '3' :
    print ("you have chosen to quit , Good bye")
     
 else:
    print("you have chosen a wrong number. Try again! ")

"""
    



 
  
  

  
 