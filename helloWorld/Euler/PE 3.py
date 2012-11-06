def nump(n):
	for x in range (2,n):
		if n%x==0:
			return False
	return True
number = raw_input ('Enter number:')
if number%nump(n)==0:
	print nump(n)