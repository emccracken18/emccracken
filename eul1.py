# using the multiples of only 3 and 5
def multiples_of_3_or_5():
# using 1000 as range
    for number in xrange(1000):
         # using only the numbers 3 and 5
        if not number % 3 or not number % 5:
            # finding the answer using the variable
            yield number
# printing only the answer to the sum of the multiples of 3 and 5
print sum(multiples_of_3_or_5())
