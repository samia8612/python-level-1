import csv

#function to write expenses to the CSV file
def display_menu():
  print("Expense Tracker Menu")
  print("1.Add sample expenses")
  print("2.Display expenses")
  print("3.Exit")
  
def add_sample_expense(file_path):
  sample_expenses = [
    ["Date", "Description","Amount"],
    ["21-05-2024","Groceries", 50.00],
    ["22-05-2024","Rent", 800.00],
    ["23-05-2024", "Tax",120.00],
    ["23-05-2024", "Clothes",50.00],
    ["25-05-2024", "Transport", 40.00]
    ]
    
  try:
      with open(file_path, mode='w', newline='')as file: #this will create the file and standered to add knew file 

       writer=csv.writer(file)  
       for expense in sample_expenses:
        writer.writerow(expense)
      print("\nSample printed successfully!\n")  
      
  except IOError:   #it should write like that with capitals
      print("\nAn error occured when writting to the file")
      
def display_expenses(file_path):   
  try:
    with open(file_path, mode='r')as file:
      reader = csv.reader(file)
      expenses =list(reader)
      if len(expenses) ==0:
        print("No expenses found")
        return
      for row in expenses:
        print(', '.join(row)) #just make it look nicer
  except FileNotFoundError:
    print("\nNo expenses found ,Please add some expenses first.")
  except IOError:
    print("\nAn error occured while reading the file.")
    
def main():
  path = "expenses.csv"
  
  while True:
    display_menu()
    choice = int(input("\nPlease enter your choice 1, 2 or 3:"))
    
    if choice ==1:
      add_sample_expense(path)
    elif choice ==2:
      display_expenses(path)
    elif choice ==3:
      print("\nExciting expense tracker , Thank you!")
      break
    else:
      print("\ninvalid option")
      
        
if __name__=="__main__": 
  main()
      
  
