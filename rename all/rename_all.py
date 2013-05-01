#!/usr/bin/python

import os
print "Pattern:"
first = raw_input()
print "Change to:"
second = raw_input()
print "Are you sure?[y/n]"
sure = raw_input()
#if not second :
#	second == ''
if sure == 'y' or sure == 'Y' or sure == 'Yes' or sure == 'yes' or sure == 'YES':
	for x in os.listdir('.'):
		y = x.replace(first, second)
		os.rename(x, y)
else:
	print "Ok! goodluck"

