import os
import sys
import time
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
    

scoreA=[90,40,50,99,29,86,45,10,30,67]
namesA=[" HAYDEN FOXWELL"," YASH PRASAD"," YASH LALA"," KAI MUNTON"," YASH PATIL"," MICHAEL TZAKOS"," PLAABON DAS"," HARSHIL PAREEK"," ADITYA NAIR"," WILLIAM KENT"]
scoreB=[89,68,4,23,19,40,99,37,98,75]              
namesB=[" GREGORY CHIDGEY"," SCOTT MANNOW"," RILEY GREEN"," PRANAV DIXIT"," BEETLEJUICE"," MADISON BEER"," ADDIOSN RAE"," CHASE HUDSON"," CHARLI DAMELIO"," DIXIE DAMELIO"]
scoreC=[99,40,30,20,50,90,70,80,60,10]                     
namesC=[" HARRISON TARRANT"," TJ JETHI"," SOHAN TAKKALAPALI"," ISAIH GV"," WAYNE EDWARDS"," TONY GEORGE"," LAMAR MUKUNDI"," ALI AJEL"," HAN SAI"," TOM SAVAGE"]
scoreD=[98,97,34,40,54,56,87,12,79,90]
namesD=[" LUCAS SINCLAIR"," EL ELEVEN"," MIKE WHEELER"," STEVE HARRINGTON"," DUSTIN HENDERSON"," WILL BYERS"," JIM HOPPER"," NANCY WHEELER"," JOYCE BYERS"," BILLY HARGROVE"]
from time import sleep
real_username="gowanbrae_admin"
real_password="1234"
logged_in=False

#menu system
while logged_in == False:

    print("Please log in with the correct username and password")
    username=input("Please enter the correct username to continue:")
    if real_username==username:
        password=input("Please enter the correct password to continue:")
        if real_password==password:
            print("")
            words = "WELCOME TO GOWAN BRAE PUBLIC SCHOOL"
            for char in words:
                sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
            logged_in=True

            while logged_in==True:
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
                    print('You have selected 1')
                    print('10A')
                    print('10B')
                    print('10C')
                    print('10D')
                    print("")
                    classletter=input("What class would you like to see")
                    if classletter in ('A','a'):
                     print("")
                    print("What would you like to change the marks to?")
                    for x in range(0, len(scoreA)):
                     scoreA[x] = int(input("What would you like to change" + namesA[x] + "'s Mark to?"))
                    if scoreA[x] < 101 > -1:
                        print(str(namesA[x]) + "'s Mark has been made to" + str(scoreA[x]) +"/100")
                        print("Mark has been changed")
                    else:
                        print("That mark cannot be entered")
                        scoreA[x] = int(input("Please re-enter the mark: "))
                        print(str(namesA[x]) + "'s mark has been made to " + str(scoreA[x]) + "/100")
                        print("")
                    if classletter in ('B','b'):
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
                    if classletter in ('C','c'):
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
                    if classletter in ('D','d'):
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
            
                
                if choice ==2:
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
                    print('Success')






