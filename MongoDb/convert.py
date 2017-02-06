while(1):
	try:
		inp = raw_input()
		if(inp == '-1'):break
		print float(inp)
	except:
		print 'Not a integer'
