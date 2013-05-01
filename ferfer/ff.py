






from ferfer import ferfer
from pprint import pprint

import json
import os
import os.path

os.system('clear')

# --------- register - check if register get key and if not do register ---------- #

feed = ferfer() # create ferfer object, register if didn't
feed.getKey() # get username and remotekey

# --------- timeline - get timeline ---------------------------------------------- #

feed.getTimeline()

# --------- post - sent request to server to post a feed ------------------------- #

p = raw_input('\n\nwrite: ').replace(' ','+')

image = raw_input('     image?[y]: ')
if image == 'y':
	i = raw_input('      url: ')

audio = raw_input('     audio?[y]: ')
if audio == 'y':
	a = raw_input('      url: ')

feed.post(p) # post 'p'

# getProfile() -- soon

# --------- end ----------------------------------------------------------------- #



