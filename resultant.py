#!/usr/bin/env python3
# calculate resultant

# Todo:
# remove multiple values
#   - create function
#   - user enters indices separeted by space
#   - split list, check if .isdigit()
#   - remove indices

import sys
import os
import re
import math
import matplotlib.pyplot as plt

COLOROPTIONS = ['b-', 'g-', 'c-', 'm-', 'y-', 'k-', 'w-']

# All values are stored as a list of lists (valuesList).
# Everything related to Fr goes to its own list (resultantList).
# The valuesList has the format: F, degrees, radians, Fx, Fy
# The resultantList has the format: Fr, Frx, Fry, netRadians, netDegrees

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
    resultantList = []
    isCalculated = False
    return valuesList, resultantList, isCalculated



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
                userInput.append(math.radians(userInput[degrees]))

                values.append(userInput)
                break

            print("You're doing it wrong!")
            continue
    return values


def resolveForce(Force, radians):
    values = [float(Force) * math.cos(radians), (float(Force) * math.sin(radians))]

    return values


def getResultant():
    resultant = [0, 0, 0, 0, 0]
    for i in range(len(valuesList)):

        # sum
        resultant[Frx] += valuesList[i][Fx]
        resultant[Fry] += valuesList[i][Fy]

    resultant[Fr] = math.sqrt(resultant[Frx] ** 2 + resultant[Fry] ** 2)
    resultant[netRadians] = math.atan2(resultant[Fry], resultant[Frx])
    resultant[netDegrees] = math.degrees(resultant[netRadians])

    return resultant


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

    if isCalculated:
            print('\n')
            print('resultant:\t\t%8.3f' % resultantList[Fr])
            print('radians:\t\t%8.3f' % resultantList[netRadians])
            print('degrees:\t\t%8.3f' % resultantList[netDegrees])

    else:
        print("\nYou need to run 'calc' to see the resultant and all Fx and Fy!")

    if halt:
        input('\nPress Enter to continue...')

def plot():
    if not isCalculated:
        print("\nYou need to run 'calc' first!")
        return
    for i in range(len(valuesList)):
        plt.plot([0, round(valuesList[i][Fx], 3)],\
                [0, round(valuesList[i][Fy], 3)],\
                COLOROPTIONS[i], label='F[%s]' % str(i+1))

    plt.plot([0, round(resultantList[Frx], 3)],\
            [0, round(resultantList[Fry], 3)],\
            'r-', label='Fr')
    plt.axis('equal')
    plt.grid()
    plt.legend()
    plt.show()



print('Calculate the resultant')

# Populate all Variables
valuesList, resultantList, isCalculated = resetAllValues()

# For testing only, don't ship
valuesList = [[15.8, 82, math.radians(82)], [23.4, 175, math.radians(175)], [12.5, 270, math.radians(270)], [28.75, 340, math.radians(340)]]
# For testing only, don't ship

while True:
    # refactor: Why variable menutext?
    menutext = ("\nEnter one of the following:\n"
                "(Letters in parentheses are shortcuts to commands)\n"
                "\n"
                "A number     to add that many forces\n"
                "'(c)alc'     to calculate the resultant\n"
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
        isCalculated = False
    elif choice == 'calc' or choice.lower() == 'c':
        for i in range(len(valuesList)):
            if len(valuesList[i]) == 3:
                valuesList[i].extend(resolveForce(valuesList[i][F],\
                        valuesList[i][radians]))
        resultantList = getResultant()
        isCalculated = True
        outputResults()
    elif choice == 'print' or choice.lower() == 'p':
        outputResults()
    elif choice == 'plot' or choice.lower() == 'o':
        plot()
    elif choice == 'remove' or choice.lower() == 'r':
        outputResults(halt = False)
        removal = int(input('\nWhich index to remove: '))
        del valuesList[removal]
        isCalculated = False
        outputResults()
    elif choice == 'clear' or choice.lower() == 'a':
        valuesList, resultantList, isCalculated = resetAllValues()
