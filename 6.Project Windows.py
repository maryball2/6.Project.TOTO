'''
Title: Best Quadratic Problem
Authors: Riley Carpenter, Liam Kiely, Bosah Mbajekwe
TODO: Find an online compiler, make it funnier
'''
#This is the area where we do our Psuedocode
'''
a is first input
if a is 0
    output an error
if a is not 0
    b is second input
    c is third input
set discriminate as (b ^ 2) - ((4 * a * c))
output discriminate
if discriminate is less than 0
    output that it has complex roots
if d is greater than 0
    set rootofd as squareroot of discriminate
    set firstanswer as (-b) + rootofd
    set secondanswer as (-b) - rootofd
    set firstanswer as firstanswer / (2 * a)
    set secondanswer as secondanswer / (2 * a)
    set every variable we've done to strings
    output "There are two roots"
    output "The roots of",a + "x² + ",b + "x + ",c,"are",firstanswer,secondanswer
otherwise
    output "There is one repeated root"
'''
import cmath
import math
import time
import sys
import os
import decimal
decimal.getcontext().prec=8
import winsound
print("Is this being run on replit?")
replit = input("Is this running on Repl.it? (Acceptable answers are yes or no) ")
if replit == "yes":
	print("DISCLAIMER: Running this on repl.it will cause somethings (screen clearing and background music) to not happen. If you would like to run this on your desktop go here https://bit.ly/2HCskUu")
if replit == "yes":
    time.sleep(5)
if sys.platform == "linux" or sys.platform == "posix":
    clearorcls = "clear"
else:
    clearorcls = "cls"
def stopsound():
    if replit == "no":
        winsound.PlaySound(None, winsound.SND_ASYNC)
def playsound(musicfile):
        winsound.PlaySound(musicfile, winsound.SND_ASYNC)
def title():
    print("""
         ====================================================
         |    ____                  __           __  _      |
         |   / __ \__  ______ _____/ /________ _/ /_(_)____ |
         |  / / / / / / / __ `/ __  / ___/ __ `/ __/ / ___/ |
         | / /_/ / /_/ / /_/ / /_/ / /  / /_/ / /_/ / /__   |
         | \___\_\__,_/\__,_/\__,_/_/   \__,_/\__/_/\___/   |
         |                                                  |
         ====================================================
         """)
def manyspace():
    if replit == "no":
        os.system(clearorcls)
    else:
        print("""

























        """)
def intro():
    title()
    playedbefore = "no"
    playsound("Main-Menu.wav")
    print(""" 
    
    What would you like to do?
    
    1. Roots
    2. Credits
    3. Exit
    
    """)
    introchoice = input("What do you want to do? ")
    if introchoice == "credits" or introchoice == "Credits" or introchoice == '2':
        credits()
    elif introchoice == "exit" or introchoice == "Exit" or introchoice == '3':
        exit()
    else:
        if playedbefore == "no":
            playsound("Song003.wav")
            playedbefore = "yes"
        program()
def restartmaybe():
    manyspace()
    print("Do you want to do another equation? Go to the home screen? Or exit.")
    print("")
    restart = input("What do you want to do (acceptable inputs are another equation, homescreen, and exit) ")
    if restart == "another equation" or restart == "Another Equation" or restart == "Another Restart" or restart == "another Equation" or restart == "Another" or restart == "another" or restart == "equation" or restart == "Equation":
        manyspace()
        program()
    elif restart == "Home screen" or restart == "home Screen" or restart == "Home Screen" or restart == "home screen" or restart == "home" or restart == "Home" or restart == "homescreen":
        manyspace()
        intro()
    else:
        manyspace()
        exit()
def credits():
    if replit == "no":
        playsound("song001.wav")
        os.system(clearorcls)
    print("")
    print("Quadratic was made possible by the great members on our team")
    print("")
    time.sleep(3)
    manyspace()
    print("Project Leader")
    print("Riley Carpenter")
    time.sleep(3)
    manyspace()
    print("Programmer and head of research development")
    print("Bosah Mbajekwe")
    time.sleep(3)
    manyspace()
    print("Second in Command/Playtester/Graphic Designer")
    print("Liam Kiely")
    print("")
    print("")
    time.sleep(3)
    print("And viewers like you")
    print("")
    print("Thank you")
    time.sleep(3)
    if replit == "no":
        stopsound()
    manyspace()
    intro()
def exit():
    playsound("Sound002.wav")
    print("Come back anytime!")
    time.sleep(4)
    os._exit(0)
def program():
    a = float(input("Enter any number that is not 0 for a. "))
    while a == 0:
        print("It has to be a number that isn't 0!")
        a = float(input("PLEASE Enter any number that is not 0 for a. "))
    b = float(input("Enter a real number for B "))
    c = float(input("Enter a real number for C "))
    discriminate = (b ** 2) - (4 * a * c)
    print("The descriminate of this equation is",discriminate)
    if discriminate < 0:
        print("This has complex roots")
        rootofdiscriminate = cmath.sqrt(discriminate)
        firstanswer = (-1 * b) + rootofdiscriminate
        secondanswer = (-1 * b) - rootofdiscriminate
        firstanswer /= (2 * a)
        secondanswer /= (2 * a)
        a = str(a)
        b = str(b)
        c = str(c)
        firstanswer = str("{0:.6f}".format(firstanswer))
        secondanswer = str("{0:.6f}".format(secondanswer))
        firstanswer = firstanswer.replace("j","i")
        secondanswer = secondanswer.replace("j","i")
        print("The roots of",a +"x² +",b +"x +",c,"are",firstanswer,"and",secondanswer)
    elif discriminate == 0:
        print("There is only one repeated root")
    else:
        rootofdiscriminate = math.sqrt(discriminate)
        firstanswer = (-1 * b) + rootofdiscriminate
        secondanswer = (-1 * b) - rootofdiscriminate
        firstanswer /= (2 * a)
        secondanswer /= (2 * a)
        a = str(a)
        b = str(b)
        c = str(c)
        firstanswer = str(float("{0:.6f}".format(firstanswer)))
        secondanswer = str(float("{0:.6f}".format(secondanswer)))
        print("This has two real roots")
        print("The roots of",a +"x² +",b +"x +",c,"are",firstanswer,"and",secondanswer)
    wait = input("Press enter when you have finished reviewing the answer")
    restartmaybe()
if replit == "no":
    playsound("soundthatneedstoplayatthebeginningforaveryspecificreasonthatidontknow-49490711.wav")
manyspace()
intro()
