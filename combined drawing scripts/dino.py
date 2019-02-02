#!/usr/bin/env python3
import dectohex
import random # importing the random module
import turtle #importing the turtle module
import time
wn = turtle.Screen()              # Set up the window and its attributes
wn.bgcolor("black")          # makes the background black
alex = turtle.Turtle() #creating a turtle
alex.hideturtle()
f = open("mystery.txt","r") # opening the doc for reading

message = '#{0}{1}{2}'

def colorpicker():


    random1 = dectohex.dectohex(random.randrange(0,256))
    random2 = dectohex.dectohex(random.randrange(0,256))
    random3 = dectohex.dectohex(random.randrange(0,256))

    if len(random1)<2:
        random1= "0" + random1

    if len(random2)<2:
        random2 = '0' + random2

    if len(random3)<2:
        random3 = '0' + random3

    finalcolor = message.format(random1,random2,random3)
    #print(random1+random2+random3)
    #print(finalcolor)
    alex.color(finalcolor)
test = input("press enter to continue.")
for aline in f: #repeats for each line in the doc
    items = aline.split() # splits the line on each space and stores it in a list
    if items[0] == "UP": # if the value at index 0 of the list is "UP" alex is picked up
        alex.up()

    else:
        if items[0] == "DOWN": # if the value at index 0 of the list is "DOWN" alex is put down
            alex.down()

        else:
            #alex goes to coordes and draws a pic as he goes
            colorpicker()
            alex.goto(int(items[0]),int(items[1])) # uses the values at index 0 and index 1 to tell alex where to go







f.close() # closes the txt doc
wn.exitonclick() # exits when user clicks screen
