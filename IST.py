print('Enter correct username and password to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='1234' and username=='gowanbrae_admin':
        print('Welcome To Gowan Brae School,')
        break
    
    else:
        print('Access denied. Try again.')
        count += 1
ans=True
while ans:
    print ("""
    1.Add a Student
    2.Delete a Student
    3.Look Up Student Record
    4.Exit/Quit
    """)
    ans= input ("What would you like to do? ") 
    if ans=="1": 
      print("\n Student Added") 
    elif ans=="2":
      print("\n Student Deleted") 
    elif ans=="3":
      print("\n Student Record Found") 
    elif ans=="4":
      print("\n Goodbye") 
    elif ans !="":
      print("\n Not Valid Choice Try again")
    
