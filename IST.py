username=input("Please enter your Username: ")
password=input("Please enter your Password: ")
attempts=3

if username == "gowanbrae_admin" and password == "1234":
  print("")
  print("1. ENTER SCORES FOR ALL CLASSES")
  print("2. PRINT OUT CLASS INFORMATION")
  print("3. EDIT SCORES FOR A CLASS")
  print("4. GRADE ALL STUDENTS INTO BANDS")
  print("5. CALCULATE THE PERCENTAGE OF STUDENTS IN A BAND")
  print("6. EXIT THE PROGRAM")
  print("")
  choice = int(input("What option would you like to select? "))
  if choice ==1:
    print('Success')

  else:
    print('Fail')

while(attempts > 1):
    if username != "gowanbrae_admin" and password != "1234":
        attempts = attempts - 1
        print("Username and Password Incorrect. You have " + str(attempts) + " attempts remaining. Please try again.")
        print("")
        username = input("Please enter your Username: ")
        password = input("Please enter your Password: ")

    if username == "gowanbrae_admin" and password == "1234":
        menu()
        pass

    elif username == "gowanbrae_admin" and password != "1234":
        attempts = attempts - 1
        print("Password Incorrect. You have " + str(attempts) + " attempts remaining. Please try again.")
        print("")
        username = input("Please enter your Username: ")
        password = input("Please enter your Password: ")

    if username == "gowanbrae_admin" and password == "1234":
        menu()
        pass

    elif username != "gowanbrae_admin" and password == "1234":
        attempts = attempts - 1
        print("Username Incorrect. You have " + str(attempts) + " attempts remaining. Please try again.")
        print("")
        username = input("Please enter your Username: ")
        password = input("Please enter your Password: ")

    if username == "gowanbrae_admin" and password == "1234":
        menu()
        pass

    if attempts == 1:
        print("Login failed. Shutting down.")