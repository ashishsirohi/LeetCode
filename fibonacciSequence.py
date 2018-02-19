class Fibonacci(object):
	def __init__(self):
		self.memo = {0:0, 1:1}
	def fibonacciSequence(self, n):
		if n < 2:
			return [i for i in range(n)]
		result = [0, 1]
		for i in range(2, n):
			result.append(result[i-1]+result[i-2])

		return result

	def fibonacciSum(self, n):
		if n < 2:
			return n
		dp = [0, 1]
		res = 1
		for i in range(2,n):
			dp.append(dp[i-1] + dp[i-2])
			res += dp[i]

		return res

	def nthFibonaaciNumber(self, n):
		try:
			return self.memo[n]
		except:
			self.memo[n] = self.nthFibonaaciNumber(n-1) + self.nthFibonaaciNumber(n-2)

		return self.memo[n]


if __name__=="__main__":
	print "Enter the length of Sequence"
	inp = int(raw_input())
	obj = Fibonacci()
	print obj.fibonacciSequence(inp)
	print "Enter length for fibinacci sum"
	inp = int(raw_input())
	print obj.fibonacciSum(inp)
	print "Nth Fibonacci input"
	inp = int(raw_input())
	print obj.nthFibonaaciNumber(inp-1)


# Function for nth Fibonacci number


