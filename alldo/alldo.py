#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os

if sys.argv[1] == '-f':
	lines = open(sys.argv[3], 'r').read().split('\n')
	for x in lines:
		command = sys.argv[2] + " " + x
		os.system(command)
else:
	for x in sys.argv[2:]:
		command = sys.argv[1] + " " + x
		os.system(command)
