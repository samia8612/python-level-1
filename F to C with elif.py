print ("this program will make ur convert")
convertChoice = input("1) Degree to F \n 2) F to Degree \n (chose the option")
if convertChoice=="1":
  Degree= float(input ("how many F do you want convert to degree\n write the number "))
  print ("The answer" , (Degree - 32) * 5/9, "C")
  
elif( convertChoice=="2"):
    F = float(input("how many Degree do you want to convert to convert to F\n write the number"))
    print("the answer" ,(F * 9/5) + 32 , "F")
    
else:
  print ("please tryagain")
  