#!/usr/bin/env python

__author__ = 'David Poslt'

'''
    Program is for overview days without alcohol :)
    
'''
import sys
from datetime import date
from colorama import init, Fore, Style
init()

# db method it's not possible using with statement becouse with automatic close file
def getDB(wr):
    db = 'testdata.txt'
    if wr == True:
        database = open(db,'a+')
        return database
    else:
        database = open(db, 'r')
        return database



# get restult
def getResult():
    y = f'{Fore.GREEN} OK'
    n = f'{Fore.RED} KO'
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


def writeToDb(result, today):
    database = getDB(True)
    database.writelines(f'\n{today} > {result}{Style.RESET_ALL}')
    database.close()

#count
def count():
    countOK = 0
    countKO = 0
    database = getDB(False)
    for db in database.readlines():

        if 'OK' in db:
            countOK +=1
        elif 'KO' in db:
            countKO +=1

    database.close()
    return countOK, countKO



# main
def main():
    writeToDb(getResult(), getDate())
    database = getDB(False)
    f = database.readlines()
    for i in f:
        print(i)

    database.close()
    ok, ko = count()
    print(f'Total days without_alkohol is {Fore.CYAN} {ok} {Style.RESET_ALL}and total days with alcohol is {Fore.RED}{ko}')



main()






