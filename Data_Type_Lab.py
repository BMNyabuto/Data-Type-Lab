def data_type(n):
	if type(n) == type([]):
		try:
			x = n[2]
			return x
		except:
			return None
	elif n == None:
		return 'no value'
	elif n == True:
		return True
	elif n == False:
		return False