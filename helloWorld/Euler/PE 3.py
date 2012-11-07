# number = raw_input('Enter number:')
# print "number is", number

def is_prim(n):
	for x in range (2,n):
		if n % x == 0:
			return False
	return True


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
#max(nump(n))<number
n=2

while n<number:
	n+=1
	if isprime(n):
		if number%n==0:
			print n

print "end"
