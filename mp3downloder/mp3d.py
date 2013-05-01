# --------------------------------------------------------------------#

		# realy ugly script i know
		# but works like a cake!

		# all links are from http://mp3skull.com/
		# this is illegal website so maybe it's blocked in your country
		# you can always use proxies.
		# maybe you need to change proxy setting of
		# console, for this should edit ~/.bashrc and add
		# 	http_proxy="http://adress:port"
		# 	export http_proxy	
		# to end of it then
		# 	$ source .bashrc
		
		# Usage:
		#		$ python mp3d.py <<<<< input method
		#		$ python mp3d.py 'led zeppelin' 'inflames' 'floods pantera'
		#

# --------------------------------------------------------------------#

from BeautifulSoup import BeautifulSoup 
import urllib2
import os
import sys

# --------------------------------------------------------------------#

def searchlink(a):
	return 'http://mp3skull.com/mp3/'+a+'.html' # create the search link

def searchforlink(soup):
	div = soup.body.find('div', attrs={'style' : 'float:left;'})
	content = div.find('div', attrs={'id' : 'content'})
	songs = content.find('div')
	song_html = songs.findAll('div', attrs={'id' : 'song_html'})
	for x in song_html:
		right_song = x.find('div', attrs={'id' : 'right_song'})
		left = right_song.find('div', attrs={'style' : 'float:left;'})
		left = left.find('div')
		download_div = left.find('div')
		download = download_div.find('a')
		print download.get('href')

def check(soup): # check if whatever you search for is exist
	try:
		div = soup.body.find('div', attrs={'style' : 'float:left;'})
		content = div.find('div', attrs={'id' : 'content'})
		return True
	except (NameError, AttributeError):
		return False

def search(a):
	try:
		page = urllib2.urlopen(a) # open html
		soup = BeautifulSoup(page) # BeautifulSoup type

		# ----------------------------------------------------------------#

		if check(soup): # is there what i want?
			searchforlink(soup)
		else:
			print 'Not Found'

		# ----------------------------------------------------------------#

	except Exception, e: # if an error happend
		print str(e)	# print it and die

# --------------------------------------------------------------------#

os.system('clear')
if len(sys.argv) > 1: # how you want to search?
	for i, x in enumerate(sys.argv):
		if i != 0:
			print '\n'+ x + ' results: \n'
			srch = x.replace(' ', '_')
			search(searchlink(srch))
else:
	srch = raw_input('search: ').replace(' ', '_')
	search(searchlink(srch))

# --------------------------------------------------------------------#
