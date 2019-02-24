def func(k):
	
	if k==0:
		return 1
	return k*func(k-1)

print("factorial:",func(5))    