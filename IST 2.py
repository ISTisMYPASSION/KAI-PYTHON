import os
import sys
import time
from time import sleep

#PROGRAM TITLE - WITH EFFECT#
words = "WELCOME TO GOWAN BRAE PUBLIC SCHOOL PYTHON PROGRAM - PLEASE ENTER THE CORRECT USERNAME AND PASSWORD TO CONTINUE"
for char in words:
    sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()   
#PROGRAM CREDENTIALS - USERNAME = gowanbrae_admin - PASSWORD = 1234#
print("") 
username=input("Please enter the correct Username: ")
password=input("Please enter the correct Password: ")
print("") 
#THE USER HAS 3 ATTEMPTS#
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
    
#STUDENT NAMES AND SCORES FOR CLASS A#
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

#STUDENT NAMES AND SCORES FOR CLASS B#
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

#STUDENT NAMES AND SCORES FOR C#
#       0  1  2  3  4  5  6  7  8  9
scoreC=[99,40,30,20,50,90,70,80,60,10]
#                 0            1             2                 3            4             5               6             7         8          9                       
namesC=["HARRISON TARRANT","TJ JETHI","SOHAN TAKKALAPALI","ISAIH GV","WAYNE EDWARDS","TONY GEORGE","LAMAR MUKUNDI","ALI AJEL","HAN SAI","TOM SAVAGE"]
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

#STUDENT NAMES AND SCORES FOR D#
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

#MAIN MENU#
def menu():
    if username == "gowanbrae_admin" and password == "1234":
        words = "WELCOME TO GOWAN BRAE PUBLIC SCHOOL PYTHON PROGRAM"
        for char in words:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("")
        print("1. Enter scores of all classes")
        print("2. Print out class information")
        print("3. Edit scores for a class")
        print("4. Grade all students bands")
        print("5. The percentage of students who achieved a particular grade")
        print("6. Exit the program")
        print("")

        choice = int(input("What option would you like to select? Enter a number to continue. "))

        if choice ==1:
            scores()      
        elif choice ==2:
              information()
        elif choice ==3:
              edit()
        elif choice ==4:
              grade()
        elif choice ==5:
              percentage()
        elif choice ==6:
            print("")
            print("Program will now exit, Thank you for using Kai Muntons PYTHON PROGRAM.")
            time.sleep(1.0)
            print("3")
            time.sleep(1.0)
            print("2")
            time.sleep(1.0)
            print("1")
            time.sleep(0.3)
            sys.exit()
                  
        else:
         print('Invalid choice. Try again')
         menu()

#SCORES FUNCTION FOR MENU 1#
         
def scores():
    print('You have selected 1')
    print('10A')
    print('10B')
    print('10C')
    print('10D')
    print("")
    classletter=input("What class would you like to see? ")

#CLASS A#
    
    if classletter in ('A','a'):
        print("")
        print("What would you like to change their marks to?")
        for x in range(0,len(scoreA)):
            scoreA[x] = int(input("What would you like to change " + namesA[x] + "'s Mark to?"))
            if scoreA[x] < 101 > -1:
                print(str(namesA[x]) + "'s Mark has been made to" + str(scoreA[x]) +"/100")
                print("")
            else:
                print("That mark cannot be entered")
                scoreA[x] = int(input("Please re-enter the mark: "))
                print(str(namesA[x]) + "'s mark has been made to " + str(scoreA[x]) + "/100")
                print("")

#CLASS B#
                
    elif classletter in ('B','b'):
          print("")
          print("What would you like to change the marks to?")
          for x in range(0, len(scoreB)):
              scoreB[x] = int(input("What would you like to change" + namesB[x] + "'s Mark to?"))
              if scoreB[x] < 101 > -1:
                  print(str(namesB[x]) + "'s Mark has been made to" + str(scoreB[x]) +"/100")
                  print("Mark has been changed")
              else:
                  print("That mark cannot be entered")
                  scoreB[x] = int(input("Please re-enter the mark: "))
                  print(str(namesB[x]) + "'s mark has been made to " + str(scoreB[x]) + "/100")
                  print("")

#CLASS C#
                  
    elif classletter in ('C','c'):
          print("")
          print("What would you like to change the marks to?")
          for x in range(0, len(scoreC)):
              scoreC[x] = int(input("What would you like to change" + namesC[x] + "'s Mark to?"))
              if scoreC[x] < 101 > -1:
                  print(str(namesC[x]) + "'s Mark has been made to" + str(scoreC[x]) +"/100")
                  print("Mark has been changed")
              else:
                  print("That mark cannot be entered")
                  scoreC[x] = int(input("Please re-enter the mark: "))
                  print(str(namesC[x]) + "'s mark has been made to " + str(scoreC[x]) + "/100")
                  print("")

#CLASS D#
                  
    elif classletter in ('D','d'):
          print("")
          print("What would you like to change the marks to?")
          for x in range(0, len(scoreD)):
              scoreD[x] = int(input("What would you like to change" + namesD[x] + "'s Mark to?"))
              if scoreD[x] < 101 > -1:
                  print(str(namesD[x]) + "'s Mark has been made to" + str(scoreD[x]) +"/100")
                  print("Mark has been changed")
              else:
                  print("That mark cannot be entered")
                  scoreD[x] = int(input("Please re-enter the mark: "))
                  print(str(namesD[x]) + "'s mark has been made to " + str(scoreD[x]) + "/100")
                  print("")
                  menu()
                  
#INFORMATION FUNCTION FOR MENU 2#
                  
def information():
    print('You have selected 2')
    print('10A')
    print('10B')
    print('10C')
    print('10D')
    print("")
    classletter=input("What class would you like to see? ")
    if classletter in ('A','a'):
        print("")
        print("Class Scores for Class A")
        for x in range(0,len(scoreA)):
            print(str(namesA[x]) + " -> " + str(scoreA[x]) + "/100")
            print("")

    elif classletter in ('B', 'b'):
          print("")
          print("Class Scores for Class B")
          for x in range(0,len(scoreB)):
              print(str(namesB[x]) + " -> " + str(scoreB[x]) + "/100")
              print("")

    elif classletter in ('C', 'c'):
          print("")
          print("Class Scores for Class C")
          for x in range(0,len(scoreC)):
              print(str(namesC[x]) + " -> " + str(scoreC[x]) + "/100")
              print("")

    elif classletter in ('D', 'd'):
          print("")
          print("Class Scores for Class D")
          for x in range(0,len(scoreD)):
              print(str(namesD[x]) + " -> " + str(scoreD[x]) + "/100")
              print("")
              
#EDIT FUNCTION FOR MENU 3#
              
def edit():
    print('You have selected 3')
    print('Classes A-D') 
    print('10A')
    print('10B')
    print('10C')
    print('10D')
    print("")
    classletter_3=input("What class would you like to see?")
    if classletter_3 in ('A','a'):
        print("")
        print("Class scores for Class 10A")
        print("1. " + namesA[0])
        print("2. " + namesA[1])
        print("3. " + namesA[2])
        print("4. " + namesA[3])
        print("5. " + namesA[4])
        print("6. " + namesA[5])
        print("7. " + namesA[6])
        print("8. " + namesA[7])
        print("9. " + namesA[8])
        print("10. " + namesA[9])
        print("11. Edit the entire classes marks")
        print("")
        editScoreA = int(input("What mark would you like to update?"))
        
#MENU 3 - CLASS A SCORES#
        
        if editScoreA == 1:
            print("")
            scoreA[0] = int(input("What would you like edit " + namesA[0] + "'s mark as?"))
            if scoreA[0] <101 > -1:
                print(str(namesA[0]) +"'s mark has been updated to " +str(scoreA[0]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreA[0] = int(input("Please try again: "))
                print(str(namesA[0]) + "'s mark has been updated to " + str(scoreA[0]) + "/100")
                print("")

        elif editScoreA == 2:
            print("")
            scoreA[1] = int(input("What would you like edit " + namesA[1] + "'s mark as?"))
            if scoreA[1] <101 > -1:
                print(str(namesA[1]) +"'s mark has been updated to " +str(scoreA[1]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreA[1] = int(input("Please try again: "))
                print(str(namesA[1]) + "'s mark has been updated to " + str(scoreA[1]) + "/100")
                print("")

        elif editScoreA == 3:
            print("")
            scoreA[2] = int(input("What would you like edit " + namesA[2] + "'s mark as?"))
            if scoreA[2] <101 > -1:
                print(str(namesA[2]) +"'s mark has been updated to " +str(scoreA[2]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreA[2] = int(input("Please try again: "))
                print(str(namesA[2]) + "'s mark has been updated to " + str(scoreA[2]) + "/100")
                print("")

        elif editScoreA == 4:
            print("")
            scoreA[3] = int(input("What would you like edit " + namesA[3] + "'s mark as?"))
            if scoreA[3] <101 > -1:
                print(str(namesA[3]) +"'s mark has been updated to " +str(scoreA[3]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreA[3] = int(input("Please try again: "))
                print(str(namesA[3]) + "'s mark has been updated to " + str(scoreA[3]) + "/100")
                print("")

        elif editScoreA == 5:
            print("")
            scoreA[4] = int(input("What would you like edit " + namesA[4] + "'s mark as?"))
            if scoreA[4] <101 > -1:
                print(str(namesA[4]) +"'s mark has been updated to " +str(scoreA[4]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreA[4] = int(input("Please try again: "))
                print(str(namesA[4]) + "'s mark has been updated to " + str(scoreA[4]) + "/100")
                print("")

        elif editScoreA == 6:
            print("")
            scoreA[5] = int(input("What would you like edit " + namesA[5] + "'s mark as?"))
            if scoreA[5] <101 > -1:
                print(str(namesA[5]) +"'s mark has been updated to " +str(scoreA[5]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreA[5] = int(input("Please try again: "))
                print(str(namesA[5]) + "'s mark has been updated to " + str(scoreA[5]) + "/100")
                print("")

        elif editScoreA == 7:
            print("")
            scoreA[6] = int(input("What would you like edit " + namesA[6] + "'s mark as?"))
            if scoreA[6] <101 > -1:
                print(str(namesA[6]) +"'s mark has been updated to " +str(scoreA[6]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreA[6] = int(input("Please try again: "))
                print(str(namesA[6]) + "'s mark has been updated to " + str(scoreA[6]) + "/100")
                print("")

        elif editScoreA == 8:
            print("")
            scoreA[7] = int(input("What would you like edit " + namesA[7] + "'s mark as?"))
            if scoreA[7] <101 > -1:
                print(str(namesA[7]) +"'s mark has been updated to " +str(scoreA[7]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreA[7] = int(input("Please try again: "))
                print(str(namesA[7]) + "'s mark has been updated to " + str(scoreA[7]) + "/100")
                print("")

        elif editScoreA == 9:
            print("")
            scoreA[8] = int(input("What would you like edit " + namesA[8] + "'s mark as?"))
            if scoreA[8] <101 > -1:
                print(str(namesA[8]) +"'s mark has been updated to " +str(scoreA[8]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreA[8] = int(input("Please try again: "))
                print(str(namesA[8]) + "'s mark has been updated to " + str(scoreA[8]) + "/100")
                print("")

        elif editScoreA == 10:
            print("")
            scoreA[9] = int(input("What would you like edit " + namesA[9] + "'s mark as?"))
            if scoreA[9] <101 > -1:
                print(str(namesA[9]) +"'s mark has been updated to " +str(scoreA[9]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreA[9] = int(input("Please try again: "))
                print(str(namesA[9]) + "'s mark has been updated to " + str(scoreA[9]) + "/100")
                print("")

        elif editScoreA == 11:
            print("What would you like to update the whole classes score to?")
            for x in range(0, len(scoreA)):
                scoreA[x] = int(input("What would you like edit " +namesA[x] + "'s mark as? "))
                if scoreA[x] < 101 > -1:
                    print(str(namesA[x]) + "'s mark has been updated to " + str(scoreA[x]) + "/100")
                    print("")
                else:
                    print("That mark is invalid")
                    scoreA[x] = int(input("Please try again: "))
                    print(str(namesA[x]) + "'s mark has been updated to " + str(scoreA[x]) + "/100")
                print("")

#MENU 3 - CLASS B SCORES#
                
    elif classletter_3 in ('B','b'):
        print("")
        print("Class scores for Class 10B")
        print("1. " + namesB[0])
        print("2. " + namesB[1])
        print("3. " + namesB[2])
        print("4. " + namesB[3])
        print("5. " + namesB[4])
        print("6. " + namesB[5])
        print("7. " + namesB[6])
        print("8. " + namesB[7])
        print("9. " + namesB[8])
        print("10. " + namesB[9])
        print("11. Edit the entire classes marks")
        print("")
        editScoreB = int(input("What mark would you like to update?"))

        if editScoreB == 1:
            print("")
            scoreB[0] = int(input("What would you like edit " + namesB[0] + "'s mark as?"))
            if scoreB[0] <101 > -1:
                print(str(namesB[0]) +"'s mark has been updated to " +str(scoreA[0]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreB[0] = int(input("Please try again: "))
                print(str(namesB[0]) + "'s mark has been updated to " + str(scoreB[0]) + "/100")
                print("")

        elif editScoreB == 2:
            print("")
            scoreB[1] = int(input("What would you like edit " + namesB[1] + "'s mark as?"))
            if scoreB[1] <101 > -1:
                print(str(namesB[1]) +"'s mark has been updated to " +str(scoreB[1]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreB[1] = int(input("Please try again: "))
                print(str(namesB[1]) + "'s mark has been updated to " + str(scoreB[1]) + "/100")
                print("")

        elif editScoreB == 3:
            print("")
            scoreB[2] = int(input("What would you like edit " + namesB[2] + "'s mark as?"))
            if scoreB[2] <101 > -1:
                print(str(namesB[2]) +"'s mark has been updated to " +str(scoreB[2]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreB[2] = int(input("Please try again: "))
                print(str(namesB[2]) + "'s mark has been updated to " + str(scoreB[2]) + "/100")
                print("")

        elif editScoreB == 4:
            print("")
            scoreB[3] = int(input("What would you like edit " + namesB[3] + "'s mark as?"))
            if scoreB[3] <101 > -1:
                print(str(namesB[3]) +"'s mark has been updated to " +str(scoreB[3]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreB[3] = int(input("Please try again: "))
                print(str(namesB[3]) + "'s mark has been updated to " + str(scoreB[3]) + "/100")
                print("")

        elif editScoreB == 5:
            print("")
            scoreB[4] = int(input("What would you like edit " + namesB[4] + "'s mark as?"))
            if scoreB[4] <101 > -1:
                print(str(namesB[4]) +"'s mark has been updated to " +str(scoreB[4]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreB[4] = int(input("Please try again: "))
                print(str(namesB[4]) + "'s mark has been updated to " + str(scoreB[4]) + "/100")
                print("")

        elif editScoreB == 6:
            print("")
            scoreB[5] = int(input("What would you like edit " + namesB[5] + "'s mark as?"))
            if scoreB[5] <101 > -1:
                print(str(namesB[5]) +"'s mark has been updated to " +str(scoreB[5]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreB[5] = int(input("Please try again: "))
                print(str(namesB[5]) + "'s mark has been updated to " + str(scoreB[5]) + "/100")
                print("")

        elif editScoreB == 7:
            print("")
            scoreB[6] = int(input("What would you like edit " + namesB[6] + "'s mark as?"))
            if scoreB[6] <101 > -1:
                print(str(namesB[6]) +"'s mark has been updated to " +str(scoreB[6]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreB[6] = int(input("Please try again: "))
                print(str(namesB[6]) + "'s mark has been updated to " + str(scoreB[6]) + "/100")
                print("")

        elif editScoreB == 8:
            print("")
            scoreB[7] = int(input("What would you like edit " + namesB[7] + "'s mark as?"))
            if scoreB[7] <101 > -1:
                print(str(namesB[7]) +"'s mark has been updated to " +str(scoreB[7]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreB[7] = int(input("Please try again: "))
                print(str(namesB[7]) + "'s mark has been updated to " + str(scoreB[7]) + "/100")
                print("")

        elif editScoreB == 9:
            print("")
            scoreB[8] = int(input("What would you like edit " + namesB[8] + "'s mark as?"))
            if scoreB[8] <101 > -1:
                print(str(namesB[8]) +"'s mark has been updated to " +str(scoreB[8]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreB[8] = int(input("Please try again: "))
                print(str(namesB[8]) + "'s mark has been updated to " + str(scoreB[8]) + "/100")
                print("")

        elif editScoreB == 10:
            print("")
            scoreB[9] = int(input("What would you like edit " + namesB[9] + "'s mark as?"))
            if scoreB[9] <101 > -1:
                print(str(namesB[9]) +"'s mark has been updated to " +str(scoreB[9]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreB[9] = int(input("Please try again: "))
                print(str(namesB[9]) + "'s mark has been updated to " + str(scoreB[9]) + "/100")
                print("")

        elif editScoreB == 11:
            print("What would you like to update the whole classes score to?")
            for x in range(0, len(scoreB)):
                scoreB[x] = int(input("What would you like edit " +namesB[x] + "'s mark as? "))
                if scoreB[x] < 101 > -1:
                    print(str(namesB[x]) + "'s mark has been updated to " + str(scoreB[x]) + "/100")
                    print("")
                else:
                    print("That mark is invalid")
                    scoreB[x] = int(input("Please try again: "))
                    print(str(namesB[x]) + "'s mark has been updated to " + str(scoreB[x]) + "/100")
                print("")

            

                    
                        
                          
while(attempts > 1):
    if username != "gowanbrae_admin" and password != "1234":
        attempts = attempts - 1
        print("Username and Password Incorrect. You have " + str(attempts) + " attempts remaining. Please try again.")
        print("")
        username = input("Please enter the correct Username: ")
        password = input("Please enter the correct Password: ")

    if username == "gowanbrae_admin" and password == "1234":
        menu()
        pass

    elif username == "gowanbrae_admin" and password != "1234":
        attempts = attempts - 1
        print("Password Incorrect. You have " + str(attempts) + " attempts remaining. Please try again.")
        print("")
        username = input("Please enter the correct Username: ")
        password = input("Please enter the correct Password: ")

    if username == "gowanbrae_admin" and password == "1234":
        menu()
        pass

    elif username != "gowanbrae_admin" and password == "1234":
        attempts = attempts - 1
        print("Username Incorrect. You have " + str(attempts) + " attempts remaining. Please try again.")
        print("")
        username = input("Please enter the correct Username: ")
        password = input("Please enter the correct Password: ")

    if username == "gowanbrae_admin" and password == "1234":
        menu()
        pass

    if attempts == 1:
        print("3 attempts used. Shutting down program.")
         
