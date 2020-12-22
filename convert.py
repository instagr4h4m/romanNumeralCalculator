"""
Roman Numeral Calculator

Author: Graham Harris

When this program is run, it will prompt the user to input an integer.
The program will then convert the given number (base 10) into
a Roman numeral. This program will work in any environment that a 
Python program can be compiled in.
"""

import math

# A method that performs validation on the input number
def validate(number):
  # try to cast number to int
  flag = True
  while flag:
    try:
     number = int(number)
     return number
    except:
      print("Invalid symbols. Please enter an integer number.")
      number = input()
  return number

# A method that converts numbers under 10 to Roman numerals
#   "num" is the number under 10 to convert
#   "buildstring" is a string that will have numerals appended to it
def ones(num, buildstring):
  numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
  buildstring += numerals[num - 1]
  return buildstring

# A method that recursively solves the Roman numerals to print
#   "num" is number base 10 to recursively solve for
#   "buildstring" is the string that each recursive call builds upon
#   "divisors" are the base 10 numbers that represent each letter, in an array
#   "divisorPos" is the position in the divisor list that we are indexing
#   "romanLetters" are the representation of the base 10 numbers
#   "romanLetterPos" is the position in the Roman number list that we are indexing
def convertToRoman(num, buildstring, divisors, divisorPos, 
                    romanLetters, romanLetterPos):
  # If the number is 0, stop recursion and return the string.
  if num == 0:
    pass

  # If the number is lower than 10, go to the ones place,
  # since the ones place has different numerals, then return the string.
  elif num < 10:
    buildstring = ones(num, buildstring)
  
  # If the number >= 10
  else:
    numInThisPlace = math.floor( num/divisors[divisorPos] ) # Number of times letter repeats
    letters = numInThisPlace * romanLetters[romanLetterPos] # String of letter repeats
    buildstring += letters # Adds letter repeats to return string

    # Find the remainder, pass it to the function that the next lowest numbers
    remainder = num % divisors[divisorPos]
    buildstring = convertToRoman(remainder, buildstring, divisors, divisorPos-1, romanLetters, romanLetterPos-1) 

  return buildstring

# --------------- Begin main program --------------- 
flag = True # Loop until user quits
divisors = [10, 50, 100, 500, 1000]
numerals = ["X", "L", "C", "D", "M"]

print("Welcome to the Roman Numeral Calculator!")
print("This program will calculate whatever number you'd like into Roman Numerals.")
print()

while flag:
  print("Enter '0' to exit the program. Fun fact, there is no '0' in Roman numerals!")
  print("Please enter a number: ")
  number = input()
  number = validate(number)

  # If the user entered 0, quit
  if number == 0:
    flag = False
    print("Thank you! Exiting program.")

  else:
    returnString = convertToRoman(number, "", divisors, 4, numerals, 4)
    print(returnString + "\n")