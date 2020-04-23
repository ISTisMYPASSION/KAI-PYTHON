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
#THE USER HAS 3 ATTEMPTS BEFORE THE PROGRAM WILL SHUT DOWN#
attempts=3
gradeA_percentage = [0]

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
#PROGRAM STARTS WITH TITLE PLUS EFFECT AND OPENS MAIN MENU WITH THE 6 MENU OPTIONS#
def menu():
    if username == "gowanbrae_admin" and password == "1234": #IF STATEMENT MEANING THAT IF CORRECT USERNAME AND PASSWORD ARE ENTERED, PROGRAM ALLOWS USER TO ACCESS MAIN MENU#
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
#CHOICES#
        choice = int(input("What option would you like to select? Enter a number to continue. "))
        
#CHOICE 1 - OPENS THE FIRST FUNCTION WHICH IS THE 'SCORES' FOR ALL 4 CLASSES A, B, C, D#
        if choice ==1:
            scores()
#CHOICE 2 - OPENS THE SECOND FUNCTION WHICH IS THE CLASS 'INFORMATION' FOR ALL 4 CLASSES A, B, C, D#
        elif choice ==2:
              information()
#CHOICE 3 - OPENS THE THIRD FUNCTION WHICH IS THE 'EDIT' FOR ALL 4 CLASSES A, B, C, D#
        elif choice ==3:
              edit()
#CHOICE 4 - OPENS THE FOURTH FUNCTION WHICH IS THE 'GRADE' INTO BANDS FOR ALL 4 CLASSES A, B, C, D#
        elif choice ==4:
              grade()
#CHOICE 5 - OPENS THE FIFTH FUNCTION WHICH IS THE 'PERCENTAGE' FOR STUDENTS WHO ACHIEVED PARTICULAR BANDS IN ALL 4 CLASSES A, B, C, D#
        elif choice ==5:
              percentage()
#CHOICE 6 - OPENS THE SIXTH AND FINAL FUNCTION WHICH EXITS THE PROGRAM#
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
#ELSE STATEMENT - IN WHICH IF 1-6 IS NOT THE NUMBER SELECTED THE FOLLOWING MESSAGE APPEARS, THEN THE PROGRAM WILL RETURN TO MENU#                 
        else:
         print('Invalid choice. Try again')
         menu()

#SCORES FUNCTION FOR MENU 1#
#THIS IS THE FIRST FUNCTION, "SCORES", WHEN OPENED - CLASSES A,B,C,D APPEAR#
def scores():
    print('You have selected 1')
    print('10A')
    print('10B')
    print('10C')
    print('10D')
    print("")
#CLASSLETTER REFERRING TO THE ABOVE 'PRINT' CLASSES A,B,C,D#
    classletter=input("What class would you like to see? ")

#CLASS A#
#FIRST IF STATEMENT - WHEN OPENED THE USER HAS THE ABILITY TO EDIT MARKS FOR THE WHOLE CLASS#
#PROGRAM USES THE CODE FOR CLASSES AT THE BEGINNING OF THE PROGRAM TO REFERENCE - EG scoreA and nameA ARE ARRAYS AT THE TOP OF THE PAGE#
    if classletter in ('A','a'):
        print("")
        print("What would you like to change their marks to?")
#WHEN A OR a IS SELECTED USER HAS ABILITY TO UPDATE MARKS#
#IF STATEMENT MAKES SURE MARKS BELOW 101 ARE ENTERED INTO THE PROGRAM AND BECOME THE NEW MARK#
        for x in range(0,len(scoreA)):
            scoreA[x] = int(input("What would you like to change " + namesA[x] + "'s Mark to?"))
            if scoreA[x] < 101 > -1:
                print(str(namesA[x]) + "'s Mark has been made to" + str(scoreA[x]) +"/100")
                print("")
#ELSE STATEMENT MAKES SURE THAT MARKS ABOVE 100 ARE NOT ENTERED INTO THE PROGRAM AND THE USER HAS TO RE-ENTER MARK#
            else:
                print("That mark cannot be entered")
                scoreA[x] = int(input("Please re-enter the mark: "))
                print(str(namesA[x]) + "'s mark has been made to " + str(scoreA[x]) + "/100")
                print("")

#CLASS B#
#FIRST ELIF STATEMENT - WHEN OPENED THE USER HAS THE ABILITY TO EDIT MARKS FOR THE WHOLE CLASS#
#PROGRAM USES THE CODE FOR CLASSES AT THE BEGINNING OF THE PROGRAM TO REFERENCE - EG scoreB and nameB ARE ARRAYS AT THE TOP OF THE PAGE#       
    elif classletter in ('B','b'):
          print("")
          print("What would you like to change the marks to?")
#WHEN B OR b IS SELECTED USER HAS ABILITY TO UPDATE MARKS#
#IF STATEMENT MAKES SURE MARKS BELOW 101 ARE ENTERED INTO THE PROGRAM AND BECOME THE NEW MARK#
          for x in range(0, len(scoreB)):
              scoreB[x] = int(input("What would you like to change" + namesB[x] + "'s Mark to?"))
              if scoreB[x] < 101 > -1:
                  print(str(namesB[x]) + "'s Mark has been made to" + str(scoreB[x]) +"/100")
                  print("Mark has been changed")
#ELSE STATEMENT MAKES SURE THAT MARKS ABOVE 100 ARE NOT ENTERED INTO THE PROGRAM AND THE USER HAS TO RE-ENTER MARK#
              else:
                  print("That mark cannot be entered")
                  scoreB[x] = int(input("Please re-enter the mark: "))
                  print(str(namesB[x]) + "'s mark has been made to " + str(scoreB[x]) + "/100")
                  print("")

#CLASS C#
#FIRST ELIF STATEMENT - WHEN OPENED THE USER HAS THE ABILITY TO EDIT MARKS FOR THE WHOLE CLASS#
#PROGRAM USES THE CODE FOR CLASSES AT THE BEGINNING OF THE PROGRAM TO REFERENCE - EG scoreC and nameC ARE ARRAYS AT THE TOP OF THE PAGE#     
    elif classletter in ('C','c'):
          print("")
          print("What would you like to change the marks to?")
#WHEN C OR c IS SELECTED USER HAS ABILITY TO UPDATE MARKS#
#IF STATEMENT MAKES SURE MARKS BELOW 101 ARE ENTERED INTO THE PROGRAM AND BECOME THE NEW MARK#
          for x in range(0, len(scoreC)):
              scoreC[x] = int(input("What would you like to change" + namesC[x] + "'s Mark to?"))
              if scoreC[x] < 101 > -1:
                  print(str(namesC[x]) + "'s Mark has been made to" + str(scoreC[x]) +"/100")
                  print("Mark has been changed")
#ELSE STATEMENT MAKES SURE THAT MARKS ABOVE 100 ARE NOT ENTERED INTO THE PROGRAM AND THE USER HAS TO RE-ENTER MARK#
              else:
                  print("That mark cannot be entered")
                  scoreC[x] = int(input("Please re-enter the mark: "))
                  print(str(namesC[x]) + "'s mark has been made to " + str(scoreC[x]) + "/100")
                  print("")

#CLASS D#
#FIRST ELIF STATEMENT - WHEN OPENED THE USER HAS THE ABILITY TO EDIT MARKS FOR THE WHOLE CLASS#
#PROGRAM USES THE CODE FOR CLASSES AT THE BEGINNING OF THE PROGRAM TO REFERENCE - EG scoreD and nameD ARE ARRAYS AT THE TOP OF THE PAGE#                       
    elif classletter in ('D','d'):
          print("")
          print("What would you like to change the marks to?")
#WHEN D OR d IS SELECTED USER HAS ABILITY TO UPDATE MARKS#
#IF STATEMENT MAKES SURE MARKS BELOW 101 ARE ENTERED INTO THE PROGRAM AND BECOME THE NEW MARK#
          for x in range(0, len(scoreD)):
              scoreD[x] = int(input("What would you like to change" + namesD[x] + "'s Mark to?"))
              if scoreD[x] < 101 > -1:
                  print(str(namesD[x]) + "'s Mark has been made to" + str(scoreD[x]) +"/100")
                  print("Mark has been changed")
#ELSE STATEMENT MAKES SURE THAT MARKS ABOVE 100 ARE NOT ENTERED INTO THE PROGRAM AND THE USER HAS TO RE-ENTER MARK#
              else:
                  print("That mark cannot be entered")
                  scoreD[x] = int(input("Please re-enter the mark: "))
                  print(str(namesD[x]) + "'s mark has been made to " + str(scoreD[x]) + "/100")
                  print("")
                  menu()
                  
#INFORMATION FUNCTION FOR MENU 2#
#THIS IS THE SECOND FUNCTION, "INFORMATION", WHEN OPENED - CLASSES A,B,C,D APPEAR#                 
def information():
    print('You have selected 2')
    print('10A')
    print('10B')
    print('10C')
    print('10D')
    print("")
    classletter=input("What class would you like to see? ")
#CLASSLETTER REFERRING TO THE ABOVE 'PRINT' CLASSES A,B,C,D#
    if classletter in ('A','a'):
#IF STATEMENT REFERRING TO CLASSLETTER, WHEN CORRECT LETTER A or a IS ENTERED, USER CAN VIEW UPDATED CLASS SCORES#
#WHEN USER UPDATES SCORES THROUGH FUNCTION 1 OR 3, THE SCORES WILL UPDATE IN FUNCTION 2 AS WELL#
        print("")
        print("Class Scores for Class A")
        for x in range(0,len(scoreA)):
            print(str(namesA[x]) + " -> " + str(scoreA[x]) + "/100")
            print("")
#THE RANGE FUNCTION HERE RETURNS THE LIST AND THE STR FUNCTION CONVERTS THE VALUE INTO STRINGS#

    elif classletter in ('B', 'b'):
#ELIF STATEMENT REFERRING TO CLASSLETTER, WHEN CORRECT LETTER B or b IS ENTERED, USER CAN VIEW UPDATED CLASS SCORES#
#WHEN USER UPDATES SCORES THROUGH FUNCTION 1 OR 3, THE SCORES WILL UPDATE IN FUNCTION 2 AS WELL#
          print("")
          print("Class Scores for Class B")
          for x in range(0,len(scoreB)):
              print(str(namesB[x]) + " -> " + str(scoreB[x]) + "/100")
              print("")
#THE RANGE FUNCTION HERE RETURNS THE LIST AND THE STR FUNCTION CONVERTS THE VALUE INTO STRINGS#

    elif classletter in ('C', 'c'):
#ELIF STATEMENT REFERRING TO CLASSLETTER, WHEN CORRECT LETTER C or c IS ENTERED, USER CAN VIEW UPDATED CLASS SCORES#
#WHEN USER UPDATES SCORES THROUGH FUNCTION 1 OR 3, THE SCORES WILL UPDATE IN FUNCTION 2 AS WELL#
          print("")
          print("Class Scores for Class C")
          for x in range(0,len(scoreC)):
              print(str(namesC[x]) + " -> " + str(scoreC[x]) + "/100")
              print("")
#THE RANGE FUNCTION HERE RETURNS THE LIST AND THE STR FUNCTION CONVERTS THE VALUE INTO STRINGS#

    elif classletter in ('D', 'd'):
#ELIF STATEMENT REFERRING TO CLASSLETTER, WHEN CORRECT LETTER D or d IS ENTERED, USER CAN VIEW UPDATED CLASS SCORES#
#WHEN USER UPDATES SCORES THROUGH FUNCTION 1 OR 3, THE SCORES WILL UPDATE IN FUNCTION 2 AS WELL#
          print("")
          print("Class Scores for Class D")
          for x in range(0,len(scoreD)):
              print(str(namesD[x]) + " -> " + str(scoreD[x]) + "/100")
              print("")
#THE RANGE FUNCTION HERE RETURNS THE LIST AND THE STR FUNCTION CONVERTS THE VALUE INTO STRINGS#
              
#EDIT FUNCTION FOR MENU 3#
#THIS IS THE THIRD FUNCTION, "EDIT", WHEN OPENED - CLASSES A,B,C,D APPEAR#               
def edit():
    print('You have selected 3')
    print('Classes A-D') 
    print('10A')
    print('10B')
    print('10C')
    print('10D')
    print("")
    classletter_3=input("What class would you like to see?")
#CLASSLETTER REFERRING TO THE ABOVE 'PRINT' CLASSES A,B,C,D#
    if classletter_3 in ('A','a'):
#WHEN EITHER A,B,C,D IS SELECTED PROGRAM WILL PRINT OUT THE 10 PEOPLE IN THAT CLASS#
#USER CAN NOW SELECT A PERSON TO INDIVIDUALLY UPDATE THEIR MARKS OR THEY CAN EDIT THE ENTIRE CLASSES#
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
#EDITSCORE REFERS TO THE SELECTION NUMBER OF A PERSON, WHEN 1 IS SELECTED, THE FIRST NAME IN 'PRINT' WILL BE OPENED AND AVALIABLE FOR USER TO UPDATE#
        
#MENU 3 - CLASS A SCORES#
#THE IF STATEMENT HERE FOR EDITSCOREA EQUALS 1, SO, HAYDEN FOXWELL IS THE FIRST NAME ON THE LIST AND IS OPENED#
#MUCH LIKE FUNCTION 1 AND 2, USER CAN EDIT SCORES, WITH THE ARRAYS USED FROM scoreA and nameA#
        if editScoreA == 1:
            print("")
            scoreA[0] = int(input("What would you like edit " + namesA[0] + "'s mark as?"))
            if scoreA[0] <101 > -1:
#IF STATEMENT MAKES SURE MARKS BELOW 101 ARE ENTERED INTO THE PROGRAM AND BECOME THE NEW MARK#
                print(str(namesA[0]) +"'s mark has been updated to " +str(scoreA[0]) + "/100")
                print("")
            else:
#ELSE STATEMENT MAKES SURE THAT MARKS ABOVE 100 ARE NOT ENTERED INTO THE PROGRAM AND THE USER HAS TO RE-ENTER MARK#
                print("That mark is invalid")
                scoreA[0] = int(input("Please try again: "))
                print(str(namesA[0]) + "'s mark has been updated to " + str(scoreA[0]) + "/100")
                print("")
#THE CODE NOW REPEATS FOR EVERY NAME IN CLASS 10A#
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
#HERE THE CODE IS REPEATED FOR CLASS 10B#
                
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
                

        #MENU 3 - CLASS C SCORES#
#HERE THE CODE IS REPEATED FOR CLASS 10C#
                
    elif classletter_3 in ('C','c'):
        print("")
        print("Class scores for Class 10C")
        print("1. " + namesC[0])
        print("2. " + namesC[1])
        print("3. " + namesC[2])
        print("4. " + namesC[3])
        print("5. " + namesC[4])
        print("6. " + namesC[5])
        print("7. " + namesC[6])
        print("8. " + namesC[7])
        print("9. " + namesC[8])
        print("10. " + namesC[9])
        print("11. Edit the entire classes marks")
        print("")
        editScoreC = int(input("What mark would you like to update?"))

        if editScoreC == 1:
            print("")
            scoreC[0] = int(input("What would you like edit " + namesC[0] + "'s mark as?"))
            if scoreC[0] <101 > -1:
                print(str(namesC[0]) +"'s mark has been updated to " +str(scoreC[0]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreC[0] = int(input("Please try again: "))
                print(str(namesC[0]) + "'s mark has been updated to " + str(scoreC[0]) + "/100")
                print("")

        elif editScoreC == 2:
            print("")
            scoreC[1] = int(input("What would you like edit " + namesC[1] + "'s mark as?"))
            if scoreC[1] <101 > -1:
                print(str(namesC[1]) +"'s mark has been updated to " +str(scoreC[1]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreC[1] = int(input("Please try again: "))
                print(str(namesC[1]) + "'s mark has been updated to " + str(scoreC[1]) + "/100")
                print("")

        elif editScoreC == 3:
            print("")
            scoreC[2] = int(input("What would you like edit " + namesC[2] + "'s mark as?"))
            if scoreC[2] <101 > -1:
                print(str(namesC[2]) +"'s mark has been updated to " +str(scoreC[2]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreC[2] = int(input("Please try again: "))
                print(str(namesC[2]) + "'s mark has been updated to " + str(scoreC[2]) + "/100")
                print("")

        elif editScoreC == 4:
            print("")
            scoreC[3] = int(input("What would you like edit " + namesC[3] + "'s mark as?"))
            if scoreC[3] <101 > -1:
                print(str(namesC[3]) +"'s mark has been updated to " +str(scoreC[3]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreC[3] = int(input("Please try again: "))
                print(str(namesC[3]) + "'s mark has been updated to " + str(scoreC[3]) + "/100")
                print("")

        elif editScoreC == 5:
            print("")
            scoreC[4] = int(input("What would you like edit " + namesC[4] + "'s mark as?"))
            if scoreC[4] <101 > -1:
                print(str(namesC[4]) +"'s mark has been updated to " +str(scoreC[4]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreC[4] = int(input("Please try again: "))
                print(str(namesC[4]) + "'s mark has been updated to " + str(scoreC[4]) + "/100")
                print("")

        elif editScoreC == 6:
            print("")
            scoreC[5] = int(input("What would you like edit " + namesC[5] + "'s mark as?"))
            if scoreC[5] <101 > -1:
                print(str(namesC[5]) +"'s mark has been updated to " +str(scoreC[5]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreC[5] = int(input("Please try again: "))
                print(str(namesC[5]) + "'s mark has been updated to " + str(scoreC[5]) + "/100")
                print("")

        elif editScoreC == 7:
            print("")
            scoreC[6] = int(input("What would you like edit " + namesC[6] + "'s mark as?"))
            if scoreC[6] <101 > -1:
                print(str(namesC[6]) +"'s mark has been updated to " +str(scoreC[6]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreC[6] = int(input("Please try again: "))
                print(str(namesC[6]) + "'s mark has been updated to " + str(scoreC[6]) + "/100")
                print("")

        elif editScoreC == 8:
            print("")
            scoreC[7] = int(input("What would you like edit " + namesC[7] + "'s mark as?"))
            if scoreC[7] <101 > -1:
                print(str(namesC[7]) +"'s mark has been updated to " +str(scoreC[7]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreC[7] = int(input("Please try again: "))
                print(str(namesC[7]) + "'s mark has been updated to " + str(scoreC[7]) + "/100")
                print("")

        elif editScoreC == 9:
            print("")
            scoreC[8] = int(input("What would you like edit " + namesC[8] + "'s mark as?"))
            if scoreC[8] <101 > -1:
                print(str(namesC[8]) +"'s mark has been updated to " +str(scoreC[8]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreC[8] = int(input("Please try again: "))
                print(str(namesC[8]) + "'s mark has been updated to " + str(scoreC[8]) + "/100")
                print("")

        elif editScoreC == 10:
            print("")
            scoreC[9] = int(input("What would you like edit " + namesC[9] + "'s mark as?"))
            if scoreC[9] <101 > -1:
                print(str(namesC[9]) +"'s mark has been updated to " +str(scoreC[9]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreC[9] = int(input("Please try again: "))
                print(str(namesC[9]) + "'s mark has been updated to " + str(scoreC[9]) + "/100")
                print("")

        elif editScoreC == 11:
            print("What would you like to update the whole classes score to?")
            for x in range(0, len(scoreC)):
                scoreC[x] = int(input("What would you like edit " +namesC[x] + "'s mark as? "))
                if scoreC[x] < 101 > -1:
                    print(str(namesC[x]) + "'s mark has been updated to " + str(scoreC[x]) + "/100")
                    print("")
                else:
                    print("That mark is invalid")
                    scoreC[x] = int(input("Please try again: "))
                    print(str(namesC[x]) + "'s mark has been updated to " + str(scoreC[x]) + "/100")
                print("")

        #MENU 3 - CLASS D SCORES#
#HERE THE CODE IS REPEATED FOR CLASS 10D#
    elif classletter_3 in ('D','d'):
        print("")
        print("Class scores for Class 10D")
        print("1. " + namesD[0])
        print("2. " + namesD[1])
        print("3. " + namesD[2])
        print("4. " + namesD[3])
        print("5. " + namesD[4])
        print("6. " + namesD[5])
        print("7. " + namesD[6])
        print("8. " + namesD[7])
        print("9. " + namesD[8])
        print("10. " + namesD[9])
        print("11. Edit the entire classes marks")
        print("")
        editScoreD = int(input("What mark would you like to update?"))

        if editScoreD == 1:
            print("")
            scoreD[0] = int(input("What would you like edit " + namesD[0] + "'s mark as?"))
            if scoreD[0] <101 > -1:
                print(str(namesD[0]) +"'s mark has been updated to " +str(scoreD[0]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreD[0] = int(input("Please try again: "))
                print(str(namesD[0]) + "'s mark has been updated to " + str(scoreD[0]) + "/100")
                print("")

        elif editScoreD == 2:
            print("")
            scoreD[1] = int(input("What would you like edit " + namesD[1] + "'s mark as?"))
            if scoreD[1] <101 > -1:
                print(str(namesD[1]) +"'s mark has been updated to " +str(scoreD[1]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreD[1] = int(input("Please try again: "))
                print(str(namesD[1]) + "'s mark has been updated to " + str(scoreD[1]) + "/100")
                print("")

        elif editScoreD == 3:
            print("")
            scoreD[2] = int(input("What would you like edit " + namesD[2] + "'s mark as?"))
            if scoreD[2] <101 > -1:
                print(str(namesD[2]) +"'s mark has been updated to " +str(scoreD[2]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreD[2] = int(input("Please try again: "))
                print(str(namesD[2]) + "'s mark has been updated to " + str(scoreD[2]) + "/100")
                print("")

        elif editScoreD == 4:
            print("")
            scoreD[3] = int(input("What would you like edit " + namesD[3] + "'s mark as?"))
            if scoreD[3] <101 > -1:
                print(str(namesD[3]) +"'s mark has been updated to " +str(scoreD[3]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreD[3] = int(input("Please try again: "))
                print(str(namesD[3]) + "'s mark has been updated to " + str(scoreD[3]) + "/100")
                print("")

        elif editScoreD == 5:
            print("")
            scoreD[4] = int(input("What would you like edit " + namesD[4] + "'s mark as?"))
            if scoreD[4] <101 > -1:
                print(str(namesD[4]) +"'s mark has been updated to " +str(scoreD[4]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreD[4] = int(input("Please try again: "))
                print(str(namesD[4]) + "'s mark has been updated to " + str(scoreD[4]) + "/100")
                print("")

        elif editScoreD == 6:
            print("")
            scoreD[5] = int(input("What would you like edit " + namesD[5] + "'s mark as?"))
            if scoreD[5] <101 > -1:
                print(str(namesD[5]) +"'s mark has been updated to " +str(scoreD[5]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreD[5] = int(input("Please try again: "))
                print(str(namesD[5]) + "'s mark has been updated to " + str(scoreD[5]) + "/100")
                print("")

        elif editScoreD == 7:
            print("")
            scoreD[6] = int(input("What would you like edit " + namesD[6] + "'s mark as?"))
            if scoreD[6] <101 > -1:
                print(str(namesB[6]) +"'s mark has been updated to " +str(scoreB[6]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreD[6] = int(input("Please try again: "))
                print(str(namesD[6]) + "'s mark has been updated to " + str(scoreD[6]) + "/100")
                print("")

        elif editScoreD == 8:
            print("")
            scoreD[7] = int(input("What would you like edit " + namesD[7] + "'s mark as?"))
            if scoreD[7] <101 > -1:
                print(str(namesD[7]) +"'s mark has been updated to " +str(scoreD[7]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreD[7] = int(input("Please try again: "))
                print(str(namesD[7]) + "'s mark has been updated to " + str(scoreD[7]) + "/100")
                print("")

        elif editScoreD == 9:
            print("")
            scoreD[8] = int(input("What would you like edit " + namesD[8] + "'s mark as?"))
            if scoreD[8] <101 > -1:
                print(str(namesD[8]) +"'s mark has been updated to " +str(scoreD[8]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreD[8] = int(input("Please try again: "))
                print(str(namesD[8]) + "'s mark has been updated to " + str(scoreD[8]) + "/100")
                print("")

        elif editScoreD == 10:
            print("")
            scoreD[9] = int(input("What would you like edit " + namesD[9] + "'s mark as?"))
            if scoreD[9] <101 > -1:
                print(str(namesD[9]) +"'s mark has been updated to " +str(scoreD[9]) + "/100")
                print("")
            else:
                print("That mark is invalid")
                scoreD[9] = int(input("Please try again: "))
                print(str(namesD[9]) + "'s mark has been updated to " + str(scoreD[9]) + "/100")
                print("")

        elif editScoreD == 11:
            print("What would you like to update the whole classes score to?")
            for x in range(0, len(scoreD)):
                scoreD[x] = int(input("What would you like edit " +namesD[x] + "'s mark as? "))
                if scoreD[x] < 101 > -1:
                    print(str(namesD[x]) + "'s mark has been updated to " + str(scoreD[x]) + "/100")
                    print("")
                else:
                    print("That mark is invalid")
                    scoreD[x] = int(input("Please try again: "))
                    print(str(namesD[x]) + "'s mark has been updated to " + str(scoreD[x]) + "/100")
                print("")

def 


#WHILE LOOP FOR LOGIN, AS LONG AS THE GIVEN CONDITION IS TRUE, WHILE LOOP WILL REPEAT, OR, AS LONG AS ATTEMPTS ARE GREATER THAN 1#
#ONCE ATTEMPTS ARE LESS THAN 1, WHILE LOOP CONDITION IS FALSE AND PROGRAM THEREFORE EXITS#

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
#HERE THE WHILE LOOP BECOMES FALSE AS ATTEMPTS ARE LESS THAN 1#
    #PROGRAM SHUTS DOWN#
    
    if attempts == 1:
        print("3 attempts used. Shutting down program.")
         
