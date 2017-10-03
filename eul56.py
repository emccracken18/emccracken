# n = 99 squared (biggest possible square under 100)
n = 99**99
# creating variable for the separation of numbers in variable n
digits = ([int(x) for x in str(n)])
# printing the sum of the individual digits of variable n
print sum(digits)
