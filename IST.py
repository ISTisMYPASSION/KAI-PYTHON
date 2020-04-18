<<<<<<< HEAD
import os
import sys
import time
from time import sleep

#title for the program#
words = "GOWAN BRAE PUBLIC SCHOOL"
for char in words:
    sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
    
#username for program is gowanbrae_admin, password is 1234#
print("")
=======
############################
## Global variables 
############################



############################
## Functions
############################

def password():
    pass

def menu():
    pass

## Add more functions from here



## this code needs to be put into functions
>>>>>>> c592c19290669511e773e5ed8cdf138f28e04de2
username=input("Please enter your Username: ")
password=input("Please enter your Password: ")
#number of attempts given to access code
attempts=3
#arrays that were used to calculate percentages of grades
gradeA_percentage = [0]
gradeB_percentage = [0]
gradeC_percentage = [0]
gradeD_percentage = [0]
gradeP_percentage = [0]
gradeE_percentage = [0]

#resetting grade percentages
def reset():
    gradeA_percentage[0]=gradeA_percentage[0] * 0
    gradeB_percentage[0]=gradeB_percentage[0] * 0
    gradeC_percentage[0]=gradeC_percentage[0] * 0
    gradeD_percentage[0]=gradeD_percentage[0] * 0
    gradeP_percentage[0]=gradeP_percentage[0] * 0
    gradeE_percentage[0]=gradeE_percentage[0] * 0
    
#student names and scores CLASS A#
#       0  1  2  3  4  5  6  7  8  9
scoreA=[90,40,50,99,29,86,45,10,30,67]
#             0                1            2           3            4               5                6             7               8          9
namesA=["HAYDEN FOXWELL","YASH PRASAD","YASH LALA","KAI MUNTON","YASH PATIL","MICHAEL TZAKOS","PLAABON DAS","HARSHIL PAREEK","ADITYA NAIR","WILLIAM KENT"]
#hayden=90
#yash prasad=40
#yash lala=50
#kai=99
#yash patil=29
#michael=86
#plaabon=45
#harshil=10
#aditya=30
#will=67

#student names and scores CLASS B#
#       0  1  2  3  4  5  6  7  8  9
scoreB=[89,68,4,23,19,40,99,37,98,75]
#                0              1              2              3              4              5             6             7               8               9                 
namesB=["GREGORY CHIDGEY","SCOTT MANNOW","RILEY GREEN","PRANAV DIXIT","BEETLEJUICE","MADISON BEER","ADDIOSN RAE","CHASE HUDSON","CHARLI DAMELIO","DIXIE DAMELIO"]
#gregory=89
#scott=68
#riley=4
#pranav=23
#beetlejuice=19
#madison=40
#addison=99
#chase=37
#charli=98
#dixie=75

#student names and scores CLASS C#
#       0  1  2  3  4  5  6  7  8  9
scoreC=[99,40,30,20,50,90,70,80,60,10]
#                 0            1             2                 3            4             5               6             7         8          9                       
namesC=["HARRISON TARRANT","TJ JETHI","SOHAN TAKKALAPALI","ISAIH GV","WAYNE EDWARDS","TONY GEORGE","LAMAR MUKUNDI","ALI AJEL","HAN SAI","TOM SAVAGE"
#harrison=99
#tj=40
#sohan=30
#isaih=20
#wayne=50
#tony=90
#lamar=70
#ali=80
#han=60
#tom=10

#student names and scores CLASS D#
#       0  1  2  3  4  5  6  7  8  9
scoreD=[67,68,40,60,23,25,23,50,27,87]
#              0              1             2             3                4            5             6             7            8             9
namesD=["PETER MUNTON","RACHEL MUNTON","MAX MORGAN","JORDY MATHIEU","JONTE NOURRY","ALEX FRENCH","NICK RUSSEL","AVANI GREGG","AVA ROSE","SOMMER RAY"]
#peter=67
#rachel=68
#max=40
#jordy= 60
#jonte=23
#alex=25
#nick=23
#avani=50
#ava=27
#sommer=87


#menu list#
def menu():
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
#choosing what number#
#menu 1 - ENTER SCORES FOR CLASSES#
        if choice ==1 
            print('Please select class from the list below')
            print('10ISTA')
            print('10ISTB')
            print('10ISTC')
            print('10ISTD')
            print("")
            classletter=input("What class would you like to see")
            if classletter in ('A','a'):
                print("")
                print("What would you like to change the marks to?")
                for x in range(0, len(scoreA)):
                    scoreA[x] = int(input("What would you like to change" + namesA[x] + "'S Mark to?"))
                    if scoreA[x] < 101 > -1:
                        print(str(namesA[x]) + "'S Mark has been made to" + str(scoreA[x]) +"/100")
                        print("")
                    else:
                        print("That mark cannot be entered")
                        scoreA[x] = int(input("Please re-enter the mark: "))
                        print(str(namesA[x]) + "'S mark has been made to " + str(scoreA[x]) + "/100")
                        print("")
  
  if choice ==2
    print('Success')

  if choice ==3:
    print('Success')

  if choice ==4:
    print('Success')

  if choice ==5:
    print('Success')

  if choice ==6:
    print('Progam Exited')

  else:
    print('Failure')

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
<<<<<<< HEAD
=======



##########################
## Main fucntion
##########################

## this is where you should create your main function
>>>>>>> c592c19290669511e773e5ed8cdf138f28e04de2
