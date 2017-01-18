def data_type(n):
	if type(n) == type([]):
		try:
			x = n[2]
			return x
		except:
			return None
			