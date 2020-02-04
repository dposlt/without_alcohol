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

    countArgs = len(sys.argv)

    if countArgs < 2:
        print('You must get argumnent y or n')
        sys.exit()

    YesOrNo = sys.argv[1]

    if len(YesOrNo) != 1:
        print('Incorrect count of arguments')
        sys.exit()

    if YesOrNo.lower() == 'y':
        return y
    elif YesOrNo.lower() == 'n':
        return n
    else:
        print('Argument must be "y" or "n" ')
        sys.exit()


# get today date
def getDate():
    today = date.today()

    return today


def writeToDb(result, today):
    # needed small database for previous days
    with open('data.txt','a+') as database:
        database.writelines(f'\n{today} > {Fore.RED}{result}{Style.RESET_ALL}')


# main
def main():
    with open('data.txt','r') as database:
        f = database.readlines()
        return f

writeToDb(getResult(), getDate())

f = main()
for i in f:
    print(i)






