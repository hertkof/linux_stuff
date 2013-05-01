#!/usr/bin/python

import os, sys

<<<<<<< HEAD
def umount(path):
	y = raw_input()
	if y == 'y' or y == 'Y' or y == 'yes' or y == 'YES':
		command = 'sudo umount ' + path + '; sudo rm -r ' + path
		os.system(command)
	elif y == 'n' or y == 'N' or y == 'no' or y == 'NO':
		print 'OK, goodluck!'
def mount(x):
	path = '/mnt/' + x
	if os.path.exists(path):
		command = 'sudo mount /dev/disk/by-label/' + x + ' ' + path
	else:
		command = 'sudo mkdir ' + path + '; sudo mount /dev/disk/by-label/' + x + ' ' + path
	os.system(command)

if len(sys.argv) > 1:
	print 'Hi! Do you wanna unmount?[y/n]'
	p = sys.argv[1]
	path = '/dev/disk/by-label/' + p
	umount(path)
=======
if len(sys.argv) > 1:
	print 'Hi! Do you wanna unmount?[y/n]'
	y = raw_input()
	p = sys.argv[1]
	path = '/dev/disk/by-label/' + p
	if y == 'y' or y == 'Y' or y == 'yes' or y == 'Yes':
		command = 'sudo umount ' + path
		os.system(command)
	elif y == 'n' or y == 'N' or y == 'No' or y == 'no':
		print 'Ok, goodluck!'
>>>>>>> 38943ca84177c14f541d256c306e8b0a83fdd643
else:
	dir = '/dev/disk/by-label'
	list = os.listdir(dir)
	print '============'
	for i,x in enumerate(list):
		print str(i) + ". " + x
	print 'Which to mount?[num]'
	x = input()
	path = '/mnt/' + list[x]
	if os.path.ismount(path):
		print "It's already mounted! Do you want unmount it?[y/n]"
<<<<<<< HEAD
		umount(path)
	else:
		mount(list[x])
=======
		y = raw_input()
		if y == 'y' or y == 'Y' or y == 'yes' or y == 'Yes':
			command = 'sudo umount ' + path
			os.system(command)
		elif y == 'n' or y == 'N' or y == 'No' or y == 'no':
			print 'ok, goodluck!'
	else:
		if os.path.exists(path):
			command = 'sudo mount /dev/disk/by-label/' + list[x] + ' /mnt/' + list[x]
		else:
			command = 'sudo mkdir /mnt/' + list[x] + ' && sudo mount /dev/disk/by-label/' + list[x] + ' /mnt/' + list[x]
		os.system(command)
	
>>>>>>> 38943ca84177c14f541d256c306e8b0a83fdd643
