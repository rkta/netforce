#!/usr/bin/env python3
# calculate resultant

# Todo:
# enumerate instead of for i in ?

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
# The valuesList has the format: F, degrees, x, y, radians, Fx, Fy
# The resultantList has the format: Fr, Frx, Fry, resRadians, resDegrees

# Assign names to list indices
# valuesList
F = 0
degrees = 1
x = 2
y = 3
radians = 4
Fx = 5
Fy = 6

# resultantList
Fr = 0
resDegrees = 1
#x = 2          same values as for valuesList
#y = 3          same values as for valuesList
resRadians = 4
Frx = 5
Fry = 6

def resetAllValues():
    global valuesList
    global resultantList
    global isCalculated

    valuesList = []
    resultantList = []
    isCalculated = False


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
    If the force system is non-concurrent and non-parallel enter the x and y
    coordinates after the angle.

    Example:
    500 90
    Example with coordinates:
    500 90 10 -15
    """)

    values = []
    for i in range(int(count)):
        while True:
            userInput = input('%d: ' % i)
            # ^(?=.) matches a ^ that is followed by a .
            # without making the . part of the match.
            # It is needed to not match an empty string.
            if re.match(r'^(?=.)([+-])?\d*(\.\d+)? (?=.)([+-])?\d*(\.\d+)?( (?=.)([+-])?\d*(\.\d+)? (?=.)([+-])?\d*(\.\d+)?)?$', userInput) is not None:
                userInput = userInput.split(' ')
                if len(userInput) == 2:
                    userInput.extend([0,0])
                userInput = [float(element) for element in userInput]

                # convert degrees to radians
                userInput.append(math.radians(userInput[degrees]))

                values.append(userInput)
                break

            print("You're doing it wrong!")
            continue
    return values


def resolveForce(Force, radians):
    values = [Force * math.cos(radians), (Force * math.sin(radians))]

    return values


def getResultant():
    resultant = [0] * 7
    for values in valuesList:
        resultant[Frx] += values[Fx]
        resultant[Fry] += values[Fy]

    resultant[Fr] = math.sqrt(resultant[Frx] ** 2 + resultant[Fry] ** 2)
    resultant[resRadians] = math.atan2(resultant[Fry], resultant[Frx])
    resultant[resDegrees] = math.degrees(resultant[resRadians])

    resultant[x], resultant[y] = \
            getCoordinatesOfResultant(resultant[Fr], resultant[resRadians])

    return resultant

def getCoordinatesOfResultant(resultant, angelOfResultant):
    Mx = 0
    My = 0
    for values in valuesList:
        Mx += values[Fx] * values[x]
        My += values[Fy] * values[y]

    # r is the distance from the origin of ordinates to the point of origin of
    # the resultant
    r = (Mx - My) / resultant

    slopeResultant = math.tan(angelOfResultant)

    slope_r = -(1/slopeResultant)

    x_of_resultant = math.sqrt(r ** 2 / ( 1 + slope_r ** 2))
    y_of_resultant = math.sqrt(r ** 2 - x_of_resultant ** 2)

    return x_of_resultant, y_of_resultant


def outputResults(halt = True):
    if halt:
        os.system("clear")

    if len(valuesList) == 0:
        print('\nYou need to enter something!')
        input('\nPress Enter to continue...')
        return None

    print('\ni\t   F\t        Angle\t   Fx\t\t   Fy\t\t x\t\t y')
    print('-' * 70)
    for i in range(len(valuesList)):
        if len(valuesList[i]) == 7:
            print(('%d\t%8.3f\t%3.2f\t%8.3f\t%8.3f\t%8.2f\t%8.2f'
                    % (i,
                       float(valuesList[i][F]),
                       float(valuesList[i][degrees]),
                       round(valuesList[i][Fx], 3),
                       round(valuesList[i][Fy], 3),
                       valuesList[i][x],
                       valuesList[i][y]))
                 )

        else:
            print(('%d\t%8.3f\t%3.2f\t%s\t%s\t%8.2f\t%8.2f'
                    % (i,
                        float(valuesList[i][F]),
                        float(valuesList[i][degrees]),
                        ' - ',
                        ' - ',
                        valuesList[i][x],
                        valuesList[i][y]))
                 )

    if halt:
        if isCalculated:
                print('\n')
                print('resultant:\t\t%8.3f' % resultantList[Fr])
                print('radians:\t\t%8.3f' % resultantList[resRadians])
                print('degrees:\t\t%8.3f' % resultantList[resDegrees])
                print('x coordinates:\t\t%8.3f' % resultantList[x])
                print('y coordinates:\t\t%8.3f' % resultantList[y])

        else:
            print("\nYou need to run 'calc' to see the resultant and all Fx and Fy!")

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

        plt.plot([valuesList[i][x], round(valuesList[i][Fx], 3) + valuesList[i][x]],\
                [valuesList[i][y], round(valuesList[i][Fy], 3) + valuesList[i][y]],\
                COLOROPTIONS[color], label='F[%s]' % str(i+1))

    plt.plot([0, round(resultantList[Frx], 3)],\
            [0, round(resultantList[Fry], 3)],\
            'r-', label='Fr')
    plt.axis('equal')
    plt.grid()
    plt.legend()
    plt.show()


def removeValues():
    global valuesList
    outputResults(halt = False)
    print("""\n
    Input indices separated by a space.
    Press enter to do nothing.
    """)
    while True:

        removal = input('\nWhich indices to remove: ')
        if not removal:
            return
        elif re.match(r'^\d+( \d+)*$', removal) is not None:
            print(removal)
            removal = removal.split(' ')
            removal = [int(element) for element in removal]

            for index in removal:
                if index <= len(valuesList) - 1:
                    del valuesList[index]
                else:
                    print('List index out of range: %s' % index)
                    input('Press enter to continue')
            isCalculated = False
            outputResults()
            break

        print("You're doing it wrong!")
        continue


print('Calculate the resultant')

# Populate all Variables
resetAllValues()

# For testing only, don't ship
#valuesList = [[15.8, 82, 0, 0, math.radians(82)], [23.4, 175, 0, 0, math.radians(175)], [12.5, 270, 0, 0, math.radians(270)], [28.75, 340, 0, 0, math.radians(340)]]
#valuesList = [[810, 220, 3.5, 4, math.radians(220)], [1050, 265, 7.2, 5.5, math.radians(265)], [560, 282, 8, 2.5, math.radians(282)], [700, 345, 10.5, 3, math.radians(345)]]
valuesList = []
#for i in range(len(COLOROPTIONS)):
#for i in range(21):
    #valuesList.append([10, 10 * i, 0, 0, math.radians(10 * i)])
# For testing only, don't ship

while True:
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
        if not valuesList:
            print('\nYou need to enter something!')
            input('\nPress Enter to continue...')
        else:
            for values in valuesList:
                if len(values) == 5:
                    values.extend(resolveForce(values[F], values[radians]))
            resultantList = getResultant()
            isCalculated = True
            outputResults()
    elif choice == 'print' or choice.lower() == 'p':
        outputResults()
    elif choice == 'plot' or choice.lower() == 'o':
        plot()
    elif choice == 'remove' or choice.lower() == 'r':
        removeValues()
    elif choice == 'clear' or choice.lower() == 'a':
        resetAllValues()
