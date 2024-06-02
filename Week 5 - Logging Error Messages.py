
import datetime 

def add_entries():

  date = input("")
  
  if date =="" :
    date = datetime.date.now().strftime("[%Y-%m-%d %H:%M:%S]")
  

def add_entries():
    
  entry = input("Enter your error message:")
  date= ""
  if date =="" :
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  
  with open("errormessage.tex", "a") as file:
   file.write(f"[{date}]-{entry}\n")
   
  print ("\n Error logged.\n") 
  
def view_entries():
  try:
    with open("errormessage.tex", "r")as file:
      entries = file.readlines()
      if entries:
        for entry in entries:
          print(entry.strip())
      else:
          print ("no message entries were find!")
  except FileNotFoundError:
    print("No message entries were found!")

  
while True:
  print("\nPlease choose an option:")
  print("1 .Log a new error message")
  print("2 .View all error messages")
  print("3 .Quit the program")
  
  choice = input("\nEnter your choice:")
  if choice == "1":
    
    add_entries()
    
  elif choice == "2":
    print("\nYou chose to view the error messages\n")
    view_entries() 
    
  elif choice == "3" :
    print ("\nYou have chosen to quit , Good bye")
    break
  else:
    print("you chose the wrong option,thank you for using the Error Logger.Try again! ")
    
    
    
   
    
    