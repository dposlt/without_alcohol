#!/usr/bin/env python

__author__ = 'David Poslt'

'''
    Program is for overview days without alcohol :)
    
'''
import sys
from datetime import date
from colorama import init, Fore, Style
init()


# get restult
def getResult():
    y = 'OK'
    n = 'KO'
    help = 'add argument "-y" for day without alcoho \n add argument "-n" for day with alcohol'

    countArgs = len(sys.argv)

    if countArgs < 2:
        print('You must get argumnent y or n')
        sys.exit()

    YesOrNo = sys.argv[1]

    if len(YesOrNo) != 2:
        print('Incorrect count of arguments')
        sys.exit()
        
    if YesOrNo.lower() == '-h':
        return help
        sys.exit()

    if YesOrNo.lower() == '-y':
        return y
    elif YesOrNo.lower() == '-n':
        return n
    else:
        print('Argument must be "y" or "n" ')
        sys.exit()


# get today date
def getDate():
    today = date.today()

    return today

db = 'testdata.txt'
def writeToDb(result, today):
    # needed small database for previous days
    with open(db,'a+') as database:
        database.writelines(f'\n{today} > {Fore.RED}{result}{Style.RESET_ALL}')


# main
def main():
    with open(db,'r') as database:
        f = database.readlines()
        return f

writeToDb(getResult(), getDate())

f = main()
for i in f:
    print(i)






