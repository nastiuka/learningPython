# number = raw_input('Enter number:')
# print "number is", number
from math import sqrt
# def is_prime(n):
# 	for x in range (2, int(n**0.5)+1, 2):
# 		if n % x == 0:
# 			return False
# 	return True

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

number = 600851475143
n=2
for n in range (2, int(sqrt(number))+1):
	n+=1
	if is_prime(n):
		if number%n==0:
			print n
print "end"
