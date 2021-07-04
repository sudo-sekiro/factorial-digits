##### Factorial digits #####
# Program to take the factorial of an integer input and return the sum of the digits
# Date: 03/07/2021
# Written for python 3.9.0
# Created by Jon Friedman as part of the Corigine recruitment process

import numpy
import sys

def main():
    #Get parameter from terminal command (had to cast here)
    num = int(sys.argv[1])
    #Take the factorial of input using numpy
    factorial = numpy.math.factorial(num)
    #Loop through factorial of input summing together each digit
    #loop breaks when factorial = 0, no longer any digits to add
    output = 0
    while(factorial>0):
        output += factorial%10
        factorial = factorial//10
    #print output
    print(output)

if __name__ == '__main__':
    try:
        main()
    except IndexError as e:
        #Catch exception where no input is given
        print("No input found, please enter a number after command in the format: python factorial-digits.py <int>\nerror type: ",e)
    except (TypeError, ValueError) as e:
        #This is to catch incorrect inputs: strings, negative numbers, etc
        print("Input error please enter a positive integer\nerror type: ", e)
        #Handle all other exceptions
    except Exception as e:
        print("The following error has occurred: ", e)