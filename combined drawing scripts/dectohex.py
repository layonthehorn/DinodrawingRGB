#!/usr/bin/env python3
#-------------------------------------------------------------------------------
# Name:        dectohex
# Purpose:
#
# Author:      LayontheHorn
#
# Created:     
# Copyright:  
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def dectobin(num):
    """This program converts from decimal to binary"""
    finalprint = ""
    num = int(num)
    list =[]
    if num == 0:
        pass
    else:
        while num > 0:

            remander = num%2
            list.append(remander)
            #print(remander)
            num = num //2
        list.reverse()
    while len(list) % 4 != 0 or list == []:

        list.insert(0,0)

    for i in list:
        finalprint = finalprint + str(i)
    return finalprint


def dectohex(num):
    """This program will convert decimal to hexidecimal"""
    hex =""
    start = 0
    count = 0
    end = 4
    list = []
    bin = dectobin(num)

    for i in bin:
        list.append(i)

    while len(list) > count:
        stringer=""
        chunk=list[start:end]


        for i in chunk:
            stringer= stringer + str(i)

        if stringer == "0000":
            hex = hex + "0"
        elif stringer == "0001":
            hex = hex + "1"
        elif stringer =="0010":
            hex = hex + "2"
        elif stringer == "0011":
            hex = hex + "3"
        elif stringer == "0100":
            hex = hex + "4"
        elif stringer == "0101":
            hex = hex + "5"
        elif stringer == "0110":
            hex = hex +"6"
        elif stringer == "0111":
            hex = hex + "7"
        elif stringer == "1000":
            hex = hex + "8"
        elif stringer =="1001":
            hex = hex + "9"
        elif stringer == "1010":
            hex = hex + "A"
        elif stringer == "1011":
            hex = hex + "B"
        elif stringer == "1100":
            hex = hex + "C"
        elif stringer == "1101":
            hex = hex + "D"
        elif stringer == "1110":
            hex = hex +"E"
        elif stringer == "1111":
            hex = hex + "F"

        start = start + 4
        end = end + 4
        count = count + 4

    return hex
