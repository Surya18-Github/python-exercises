#! /usr/bin/python

# variable to store the fractional part of the number
x=' '

""" for loop,
To set the upper limit of the loop:
We have 9 - 1 digit numbers, 90 - 2 digit numbers, 900 - 3 digit numbers, 9000 - 4 digit numbers, 90000 - 5 digit numbers, 900000 - 6 digit numbers.
Which will be total of 5888885 digits.But we need only 1000000 digits.
so, 9*1 + 90*2 + 900*3 + 90000*4 + 900000*5 + n*6 = 1000000. 
i.e value of n is approximately 185186."""

for i in xrange(1,185186):
    x=x+str(i)
    
# finding d1,d10,d100,d1000,d10000,d100000,d1000000
d1=int(x[0])
d10=int(x[9])
d100=int(x[99])
d1000=int(x[999])
d10000=int(x[9999])
d100000=int(x[99999])
d1000000=int(x[999999])

# print the result
print d1*d10*d100*d1000*d10000*d100000*d1000000
