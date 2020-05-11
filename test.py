#D. Da Silva  05/08/2020
#For my "Hello World!" Docker Project

a = 5
b= 10
exit=0
print('This program is a simple program to test building and running a docker container. The program will deter if the number inopt is within range of 5<x<10.')
while exit== 0:
        c=int(input('Enter number: '))
        if (c>a and c<b):
                print('In range')
        else:
                print('Out of range')
        bye= input('Continue? Y/N: ')
        bye= bye.capitalize()
        if bye== 'N':
            exit= 1

