"""
    This script calculates the sum of the digits in the 100!
"""
import math

resultInt = 0
# obtaining a factorial of 100 and convert it to string
resultStr = str(math.factorial(100))
# cycle for each char in string
for char in resultStr:
    resultInt += int(char)
print(resultInt)
