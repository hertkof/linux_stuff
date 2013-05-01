# --------------------------------------------------------------------#

		# realy ugly script i know
		# but it works like a cake!

		# all links are from http://mp3skull.com/
		# this is illegal website so maybe it's blocked in your country
		# you can always use proxies.
		# maybe you need to change proxy setting of
		# console, for this should edit ~/.bashrc and add
		# 	http_proxy="http://adress:port"
		# 	export http_proxy	
		# to end of it then
		# 	$ source .bashrc
		# good luck

# --------------------------------------------------------------------#

from BeautifulSoup import BeautifulSoup 
import urllib2
import os

# --------------------------------------------------------------------#

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

def check(soup):
	try:
		div = soup.body.find('div', attrs={'style' : 'float:left;'})
		content = div.find('div', attrs={'id' : 'content'})
		return True
	except (NameError, AttributeError):
		return False

# --------------------------------------------------------------------#

os.system('clear')

try:
	search = raw_input('search: ').replace(' ', '_')
	search = 'http://mp3skull.com/mp3/'+search+'.html'

	page = urllib2.urlopen(search)
	soup = BeautifulSoup(page)

	# ----------------------------------------------------------------#

	if check(soup):
		searchforlink(soup)
	else:
		print 'Not Found'

	# ----------------------------------------------------------------#

except Exception, e:
	print str(e)

# --------------------------------------------------------------------#