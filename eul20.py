# importing math
import math
# making variable for the factorial of 100
n = math.factorial(100)
# making another variable for list of digits in 100!
digits = ([int(x) for x in str(n)])
# printing the sum of the digits in 100!
print sum(digits)
