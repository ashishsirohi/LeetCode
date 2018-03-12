def sticksOp(sticks):
	
	while len(sticks) > 0:
		minV = min(sticks)

		i = 0
		while i < len(sticks):
			if sticks[i] == minV:
				sticks.remove(sticks[i])
			else:
				sticks[i] -= minV
				i += 1

		print sticks

sticksOp([6,4,2,2,8])