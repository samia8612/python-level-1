print ("Welcome to the Financial Tracker! ")
incomes = []
expenses=[]
final=[]
while True:
  
  action=input("\nenter your choice: \n'1' Add an income \n'2' Add expenses \n'3' View financial summary \n'4'  Quit\n")


# to add a task
  if action == '1':
    income = float(input("Enter a income"))
    incomes.append(income)
    print ("\nYour income =" ,income)
    
  elif action =="2":
    expense = float(input("how much your expenses"))
    expenses.append(expense)
    print ("\nYour expenses =", expense )
    
  elif action =="3":
    sum_incomes = sum(incomes)
    sum_expenses= sum(expenses)
   # sum_fin = float(input("you final summary",sum_incomes - sum_expenses))
   # final.append(sum_fin)
    print (f"\n Your final summary",sum_incomes - sum_expenses, "\n")
     
   
    
    
  
   # weight = 54.343
   # weight_rounded = round(weight, 2)
   # print(weight_rounded)
  
    
  elif action =="4":
      print ("exit program, Goodbye")
      break
    
  else:
    ("Incorrect input, TRY AGAIN!")
      
 
  

  