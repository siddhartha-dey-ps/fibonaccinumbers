from array import *

# Generating first 34 Fibonacci numbers
maxcount = 34
fibnumarray = array('l', [1,1])
count = 3
while(count <= maxcount):
    fibnum = fibnumarray[count - 2] +  fibnumarray[count - 3]
    fibnumarray.append(fibnum)
    count = count + 1

print(fibnumarray)