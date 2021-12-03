def mean(numbers):
	N = 0
	sum = 0
	for i in numbers:
		N += 1
		sum += i
	return sum/N

def std(numbers):
	sum = 0
	M = -1
	mean = mean(numbers)
	for i in numbers:
		sum += (i-mean)**2
		M += 1
	return sum**(1/2)/M

def skew(numbers):
	sum = 0
	mean = mean(numbers)
	std = std(numbers)
	for num in numbers:
		sum += (num-mean)**3
	return sum/((N-1)*std**3)
