
def fibonacci (n):
	if n == 1 or n == 2:
		return 1
	return fibonacci(n-1)+fibonacci(n-2)

suma = 0
n = 0 
while True:
	n = n+1
	x= fibonacci(n)
	if x<4000000:
		if x%2==0:
			suma= x + suma
			print suma
	else:
		break
print "end"
