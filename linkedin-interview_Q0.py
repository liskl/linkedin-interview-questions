#!/usr/bin/env python3

for i in range(100):
	if (i % 4 == 0 ) and (i % 6 == 0 ):
		print("{}, LinkedIn".format(i))
	elif (i % 4 == 0 ):
		print("{}, Linked".format(i))
	elif (i % 6 == 0 ):
		print("{}, in".format(i))
	else:
		pass
