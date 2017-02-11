#!/usr/bin/env python3
# calculate net force
# Resultierende berechnen

# TODO
# Change data structure
#   put all var in one dict/list?

import sys
import os
import re
import math
import matplotlib.pyplot as plt

COLOROPTIONS = ['b-', 'g-', 'c-', 'm-', 'y-', 'k-', 'w-']

# All values are stored as a list of lists (valuesList).
# Everything related to Fr goes to its own list (netforceList).
# The valuesList has the format: F, degrees, radians, Fx, Fy
# The netforceList has the format: Fr, Frx, Fry, netRadians, netDegrees

# Asign names to list indices
F = 0
degrees = 1
radians = 2
Fx = 3
Fy = 4

Fr = 0
Frx = 1
Fry = 2
netRadians = 3
netDegrees = 4

def resetAllValues():
    valuesList = []
    netforceList = []
    calc = False
    return valuesList, netforceList, calc



def waitingfornothing():
    """
    Just wait for user to press 'Enter'
    For debugging only!
    """
    waitingfornothing = input('...')


def getInput(count):
    print("""
    Input force and angle separated by a space.
    Forces must have all the same unit.
    Angle has to be degrees.

    Example:
    500 90
    """)

    values = []
    for i in range(0, int(count)):
        while True:
            userInput = input('%d: ' % i)
            # ^(?=.) matches a ^ that is followed by a .
            # without making the . part of the match.
            # It is needed to not match an empty string.
            if re.match(r'^(?=.)([+-])?\d*(\.\d+)? (?=.)([+-])?\d*(\.\d+)?$',\
                    userInput) is not None:
                userInput = userInput.split(' ')
                userInput = [float(element) for element in userInput]

                # convert degrees to radians
                userInput.append(math.radians(float(userInput[degrees])))

                print(userInput) # debug
                values.append(userInput)
                break

            print("You're doing it wrong!")
            continue
    print(values) # debug
    return values


def calculate(Force, radians):
    print('Inside calculate')
    print(Force)

    values = [float(Force) * math.cos(radians), (float(Force) * math.sin(radians))]

    print(values)
    return values

def getNetForce():
    netforce = [0, 0, 0, 0, 0]
    for i in range(len(valuesList)):

        # sum
        print(valuesList[i])
        netforce[Frx] += valuesList[i][Fx]
        netforce[Fry] += valuesList[i][Fy]

    netforce[Fr] = math.sqrt(netforce[Frx] ** 2 + netforce[Fry] ** 2)
    netforce[netRadians] = math.atan(netforce[Fry] / netforce[Frx])
    netforce[netDegrees] = math.degrees(netforce[netRadians])
    
    return netforce


def outputResults(halt = True):
    if halt:
        os.system("clear")

    head = '\ni\t   F\t        Angle\t   Fx\t\t   Fy'
    if len(valuesList) == 0:
        print('\nYou need to enter something!')
        input('\nPress Enter to continue...')
        return None

    print(head)
    print('-' * 70)
    for i in range(len(valuesList)):
        if len(valuesList[i]) == 5:
            print(('%d\t%8.3f\t%3.2f\t%8.3f\t%8.3f'
                    % (i,
                       float(valuesList[i][F]),
                       float(valuesList[i][degrees]),
                       round(valuesList[i][Fx], 3),
                       round(valuesList[i][Fy], 3)))
                 )

        else:
            print(('%d\t%8.3f\t%3.2f'
                    % (i,
                        float(valuesList[i][F]),
                        float(valuesList[i][degrees])))
                 )

    if calc:
            print('\n')
            print('net force:\t\t%8.3f' % netforceList[Fr])
            print('radians:\t\t%8.3f' % netforceList[netRadians])
            print('degrees:\t\t%8.3f' % netforceList[netDegrees])

    else:
        print("\nYou need to run 'calc' to see the net force and all Fx and Fy!")

    if halt:
        input('\nPress Enter to continue...')

def plot():
    for i in range(len(valuesList)):
        plt.plot([0, round(valuesList[i][Fx], 3)],\
                [0, round(valuesList[i][Fy], 3)],\
                COLOROPTIONS[i], label='F[%s]' % str(i+1))

    plt.plot([0, round(netforceList[Frx], 3)],\
            [0, round(netforceList[Fry], 3)],\
            'r-', label='Fr')
    plt.axis('equal')
    plt.grid()
    plt.legend()
    plt.show()

def removeValues():
    pass


print('Calculate the net force')

# Populate all Variables
valuesList, netforceList, calc = resetAllValues()

# For testing only, don't ship
valuesList = [[15.8, 82, math.radians(82)], [23.4, 175, math.radians(175)], [12.5, 270, math.radians(270)], [28.75, 340, math.radians(340)]]
# For testing only, don't ship

while True:
    menutext = ("\nEnter one of the following:\n"
                "(Letters in parentheses are shortcuts to commands)\n"
                "\n"
                "A number     to add that many forces\n"
                "'(c)alc'     to calculate the net force\n"
                "'(p)rint'    to print\n"
                "'pl(o)t'     to plot all forces\n"
                "'(r)emove'   to remove one pair of values\n"
                "'cle(a)r'    to clear all values\n"
                "'(q)uit'     to quit\n")
    print(menutext)
    while True:
        choice = input('> ')
        if choice.lower() == 'quit' or choice.lower() == 'q':
            sys.exit()

        elif (choice.isdigit()
                or choice.lower() in ['c', 'p', 'o', 'r', 'a']
                or choice.lower() == 'calc'
                or choice.lower() == 'print'
                or choice.lower() == 'plot'
                or choice.lower() == 'remove'
                or choice.lower() == 'clear'):
            break

        print('You entered: %s\n Try again!' % choice)

    if choice.isdigit():
        valuesList.extend(getInput(choice))
        calc = False
    elif choice == 'calc' or choice.lower() == 'c':
        for i in range(len(valuesList)):
            if len(valuesList[i]) == 3:
                valuesList[i].extend(calculate(valuesList[i][F],\
                        valuesList[i][radians]))
        netforceList = getNetForce()
        calc = True
        outputResults()
    elif choice == 'print' or choice.lower() == 'p':
        outputResults()
    elif choice == 'plot' or choice.lower() == 'o':
        plot()
    elif choice == 'remove' or choice.lower() == 'r':
        outputResults(halt = False)
        removal = int(input('Which index to remove: '))
        del valuesList[removal]
        calc = False
        outputResults()
    elif choice == 'clear' or choice.lower() == 'a':
        valuesList, netforceList, calc = resetAllValues()
