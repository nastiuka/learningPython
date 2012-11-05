
def fibonacci (n):
	if n == 1 or n == 2:
		return 1
	return fibonacci(n-1)+fibonacci(n-2)
suma = 0
for fibonacci in range (0, 4000000):
	if fibonacci%2==0:
		suma= fibonacci + suma

print suma