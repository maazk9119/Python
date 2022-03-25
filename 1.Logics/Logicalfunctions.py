#Qn1: program to convert the given mnumber into years and week. get the user input?
def IntoYearsAndWeeks(days):
    years = int(days/365)
    weeks = int(days / 7)
    print("Number of Years is:", years)
    print("Number of weeks is:", weeks)


#Qn:02 write a program which find the factor of a given numbers. the factor should be prime number.
def prime_fac(number):   
    print("Prime factors")
    start = 1
    while(start <= number):
        count = 0
        if(number % start == 0):
            innerstart = 1
            while(innerstart <= start):
                if(start % innerstart == 0):
                    count = count+1  
                innerstart = innerstart + 1

        if(count ==2):
            print(start)
        start = start + 1
        

#Qn:03:if today is saturday, it will be saturday again in 7 days. suppose you and your friends are going to meet in 10 days. what day is in 10 days?write a pprogram to compute a day
def find_Day(days):
    meetafterdays = 10
    index = meetafterdays % 7
    print("The meetup day is:",days[index])


#Qn:04 GAME( scissor rock paper )who wins computer or user
from random import randint
def Game():
    compchoice = randint(0,2)
    print("0:scissor\n1:paper\n2:rock")
    userenter = int(input("Enter your choice:"))

    if(userenter>2):
        print("Wrong choice:")
    else:
        if(compchoice ==0 and userenter ==2):
            print("The computer is scissor")
            print("User is rock")
            print("User Won!")
        elif(compchoice == 2 and userenter ==1):
            print("The computer is rock")
            print("User is paper")
            print("Computer Won!")
        elif(compchoice == 1 and userenter == 0):
            print("The computer is rock")
            print("User is paper")
            print("Computer Won!")
        else:
            print("Game Draw same choice:")
    


#-----Main---------#
#---Write code here--------#




