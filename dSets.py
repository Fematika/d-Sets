import math
	
class Q:
	def __init__(self, end):
		self.end = end
		self.prime = []
		self.dsets = []
		self.primesCalculated = [2, 3, 5]
		self.sums = []
	
	def searchPrimes(self, min, max):
		primes = self.primesCalculated
		
		if max > primes[len(primes) - 1]:
			for n in range(primes[len(primes) - 1] + 1, max + 1):
				if n % 2 != 0:
					i = 0
			
					while i in range(0, len(primes)):
						a = primes[i]
						i += 1
					
						if n % a == 0:
							break
				
					if i == len(primes):
						primes.append(n)
		return primes
		self.primesCalculated = primes
		
	def primeDivisors(self, x, n):
		divisors = []
			
		if x in self.primesCalculated:
			if x == n:
				divisors.append(x)
		else:
			r = x
			
			for i in self.searchPrimes(2, math.ceil(x / 2)):
				if r == 1:
					break
				else:
					if r % i == 0:
						a = math.log(r, i)
						
						if a % 1 == 0:
							r = 1
							a = int(a)
							
							for j in range(0, a):
									divisors.append(i)
						elif (r / i) % i == 0:
							for j in range(0, math.ceil(a) - 1):
								if r % i == 0:
									divisors.append(i)
									r /= i
								else:
									break
						else:
							r /= i
							divisors.append(i)
		
		return divisors
		
	def dSet(self, n):
		primes = self.searchPrimes(2, n)
		dset = []
		
		if n in self.primesCalculated:
			dset.append({n : n})
		
		for i in range(math.ceil(n / 2), len(self.sums)):
			if self.sums[i][2] == n:
				dset.append({self.sums[i][0] : self.sums[i][1]})
		
		for x in range((n - 1) ** 2, n ** 2):
			s = 0
			divisors = self.primeDivisors(x, n)
		
			for i in divisors:
				s += i
			
			self.sums.append([x, divisors, s])
			
			if s == n:
				dset.append({x : divisors})
		
		return [n, dset]
			
	def iterate(self):
		for i in range(2, self.end + 1):
			a = self.dSet(i)
			print(a[0], ": ")
			
			for i in a[1]:
				print(i)
				
example = Q(100)
example.iterate()