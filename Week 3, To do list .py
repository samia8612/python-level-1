# print the welcome message 
print("welcome to the sample to-do list!")

# creat the list empty list to store tasks 
tasks = []

# main loop for the sample to-do list
while True:
  
  #promot the user to choose an action
  action = input("enter  'a' to add a task, 'v' veiw to a task,'r' to remove a task, 'c' to complete a task, 'q' to quit ")
  
  # to add a task
  if action == 'a':
    task = input("Enter a task")
    tasks.append({"task":task, "complete":False})
    print ("task added succesfully")
    
  elif action =="v":
    if tasks:
        print ("tasks:")
    
    # loop over tasks to disply them 
    for i in range(len(tasks)):
      print(f"{i+ 1}.[{'x' if tasks [i]['complete'] else ' '}] {tasks[i]['task']}")
    
      
    else :
      print ("No tasks on the list")
      
    #remove a task  
  elif action == 'r':
    if tasks:
      index =int (input("Enter the task you want to remove: ")) -1
      
      if 0<=index<=len(tasks):
        del tasks [index]
        print ("iteam removed")
        
      else:
        print("incorrect index")
    else:
      print("No iteam on the list")
      
    #making the task as complete
  elif action == 'c':
    if tasks:
      index=int(input("enter the task you want to market as complete"))-1
      if 0<=index<=len(tasks):
        tasks[index]['complete']=True
        print("Task market complete")
        
      else:
       print("incorrect index")
        
        
    else:
        print("No tasks in the list")
      
      
    #quit from program
  elif action =='q':
      print ("exit program, Goodbye")
      break
    
    
    #error handling incorectly
  else:
      "Incorrect input please try again"

