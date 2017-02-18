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

COLOROPTIONS = [
'#0000FF',	# 'blue':
'#008000',	# 'green':
'#00FFFF',	# 'cyan':
'#FF00FF',	# 'magenta':
'#FFFF00',	# 'yellow':
'#000000',	# 'black':
'#A52A2A',	# 'brown':
'#FF1493',	# 'deeppink':
'#8A2BE2',	# 'blueviolet':
'#DEB887',	# 'burlywood':
'#5F9EA0',	# 'cadetblue':
'#7FFF00',	# 'chartreuse':
'#D2691E',	# 'chocolate':
'#FF7F50',	# 'coral':
'#6495ED',	# 'cornflowerblue':
'#00BFFF',	# 'deepskyblue':
'#696969',	# 'dimgray':
'#1E90FF',	# 'dodgerblue':
'#B22222',	# 'firebrick':
'#228B22',	# 'forestgreen':
'#FF00FF',	# 'fuchsia':
'#DCDCDC',	# 'gainsboro':
'#FFD700',	# 'gold':
'#DAA520',	# 'goldenrod':
'#808080',	# 'gray':
'#ADFF2F',	# 'greenyellow':
'#F0FFF0',	# 'honeydew':
'#FF69B4',	# 'hotpink':
'#CD5C5C',	# 'indianred':
'#4B0082',	# 'indigo':
'#FFFFF0',	# 'ivory':
'#F0E68C',	# 'khaki':
'#E6E6FA',	# 'lavender':
'#FFF0F5',	# 'lavenderblush':
'#7CFC00',	# 'lawngreen':
'#FFFACD',	# 'lemonchiffon':
'#ADD8E6',	# 'lightblue':
'#F08080',	# 'lightcoral':
'#E0FFFF',	# 'lightcyan':
'#FAFAD2',	# 'lightgoldenrodyellow':
'#90EE90',	# 'lightgreen':
'#D3D3D3',	# 'lightgray':
'#FFB6C1',	# 'lightpink':
'#FFA07A',	# 'lightsalmon':
'#20B2AA',	# 'lightseagreen':
'#87CEFA',	# 'lightskyblue':
'#778899',	# 'lightslategray':
'#B0C4DE',	# 'lightsteelblue':
'#FFFFE0',	# 'lightyellow':
'#00FF00',	# 'lime':
'#32CD32',	# 'limegreen':
'#FAF0E6',	# 'linen':
'#800000',	# 'maroon':
'#66CDAA',	# 'mediumaquamarine':
'#0000CD',	# 'mediumblue':
'#BA55D3',	# 'mediumorchid':
'#9370DB',	# 'mediumpurple':
'#3CB371',	# 'mediumseagreen':
'#7B68EE',	# 'mediumslateblue':
'#00FA9A',	# 'mediumspringgreen':
'#48D1CC',	# 'mediumturquoise':
'#C71585',	# 'mediumvioletred':
'#191970',	# 'midnightblue':
'#F5FFFA',	# 'mintcream':
'#FFE4E1',	# 'mistyrose':
'#FFE4B5',	# 'moccasin':
'#000080',	# 'navy':
'#FDF5E6',	# 'oldlace':
'#808000',	# 'olive':
'#6B8E23',	# 'olivedrab':
'#FFA500',	# 'orange':
'#FF4500',	# 'orangered':
'#DA70D6',	# 'orchid':
'#EEE8AA',	# 'palegoldenrod':
'#98FB98',	# 'palegreen':
'#AFEEEE',	# 'paleturquoise':
'#DB7093',	# 'palevioletred':
'#FFEFD5',	# 'papayawhip':
'#FFDAB9',	# 'peachpuff':
'#CD853F',	# 'peru':
'#FFC0CB',	# 'pink':
'#DDA0DD',	# 'plum':
'#B0E0E6',	# 'powderblue':
'#800080',	# 'purple':
'#FF0000',	# 'red':
'#BC8F8F',	# 'rosybrown':
'#4169E1',	# 'royalblue':
'#8B4513',	# 'saddlebrown':
'#FA8072',	# 'salmon':
'#FAA460',	# 'sandybrown':
'#2E8B57',	# 'seagreen':
'#FFF5EE',	# 'seashell':
'#A0522D',	# 'sienna':
'#C0C0C0',	# 'silver':
'#87CEEB',	# 'skyblue':
'#6A5ACD',	# 'slateblue':
'#708090',	# 'slategray':
'#FFFAFA',	# 'snow':
'#00FF7F',	# 'springgreen':
'#4682B4',	# 'steelblue':
'#D2B48C',	# 'tan':
'#008080',	# 'teal':
'#D8BFD8',	# 'thistle':
'#FF6347',	# 'tomato':
'#40E0D0',	# 'turquoise':
'#EE82EE',	# 'violet':
'#F5DEB3',	# 'wheat':
'#9ACD32',	# 'yellowgreen':
'#00008B',	# 'darkblue':
'#008B8B',	# 'darkcyan':
'#B8860B',	# 'darkgoldenrod':
'#A9A9A9',	# 'darkgray':
'#006400',	# 'darkgreen':
'#BDB76B',	# 'darkkhaki':
'#8B008B',	# 'darkmagenta':
'#556B2F',	# 'darkolivegreen':
'#FF8C00',	# 'darkorange':
'#9932CC',	# 'darkorchid':
'#8B0000',	# 'darkred':
'#E9967A',	# 'darksalmon':
'#8FBC8F',	# 'darkseagreen':
'#483D8B',	# 'darkslateblue':
'#2F4F4F',	# 'darkslategray':
'#00CED1',	# 'darkturquoise':
'#9400D3']	# 'darkviolet':

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

    if len(valuesList) == 0:
        print('\nYou need to enter something!')
        input('\nPress Enter to continue...')
        return None

    print('\ni\t   F\t        Angle\t   Fx\t\t   Fy')
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
        if i < len(COLOROPTIONS):
            color = i
        else:
            color = i - len(COLOROPTIONS)

        plt.plot([0, round(valuesList[i][Fx], 3)],\
                [0, round(valuesList[i][Fy], 3)],\
                COLOROPTIONS[color], label='F[%s]' % str(i+1))

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
#valuesList = [[15.8, 82, math.radians(82)], [23.4, 175, math.radians(175)], [12.5, 270, math.radians(270)], [28.75, 340, math.radians(340)]]
valuesList = []
#for i in range(len(COLOROPTIONS)):
for i in range(21):
    valuesList.append([10, 10 * i, math.radians(10 * i)])
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
