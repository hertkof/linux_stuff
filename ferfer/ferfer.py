
	
	#	
	#	
	#	
	#	
	#	



	class ferfer:

			homedir = os.path.expanduser('~')
			ferdir = homedir+'/.ferfer'
			keyfile = ferdir+'/.key'
			msg = ''
			username = ''
			remote = ''

			def __init__(self):
				if not os.path.isdir(self.ferdir) or not os.path.isfile(self.keyfile):
					self.register()

			def isError(self):
				if self.msg.find('errorCode') > 0:
					for x in u'{}"':
						self.msg = self.msg.replace(x, '')
					err = self.msg.split(':')
					if str(err[1]) == 'feed-not-found':
						print 'Unrecognized feed id/username'
					elif str(err[1]).find('-required') > 0 :
						print 'The HTTP argument ARG is required for this request'
					elif str(err[1]) == 'limit-exceeded':
						print 'Request limit exceeded'
					elif str(err[1]) == 'forbidden':
						print 'User does not have access to entry, group or other entity specified in the request'
					elif str(err[1]) == 'unauthorized':
						print 'The request requires authentication'
					else :
						print "Something wrong"	
				else :
					return False

			def register(self):
				username = raw_input('hey fella! give me your username: ')
				remote = raw_input('very good! now remote key(found it at https://friendfeed.com/account/api): ')
				key = username+':'+remote
				os.mkdir(self.ferdir)
				open(self.keyfile, 'w').write(key)

			def getKey(self):
				key = open(self.keyfile, 'r').read().split(':')
				self.username = key[0]
				self.remote = key[1]


			def getFeeds(self, j):
				data = json.load(j)
				for x in data['entries']:
					pprint(x['body'].encode("ascii","replace").encode('utf-8'))
					pprint(x["from"]["name"].encode("ascii","replace").encode('utf-8'))
					try:
						print 'comments:' + str(len(x["comments"])) + ' '
					except KeyError:
						pass
					try:
						print 'likes:' + str(len(x["likes"]))
					except KeyError:
						pass
					print '\n'

			def getTimeline(self):
				cmd = 'curl -u "'
				cmd += self.username+':'+self.remote
				cmd += '" http://friendfeed-api.com/v2/feed/'
				cmd += self.username
				cmd += '/friends'
				self.msg = os.popen(cmd)
				os.system('clear')
				self.getFeeds(self.msg)

			def post(self, p):
				cmd = 'curl -u "'
				cmd += self.username+':'+self.remote
				cmd += '" -d "body='
				cmd += p
				if 'i' in globals():
					cmd += '&image_url='+i
				if 'a' in globals():
					cmd += '&audio_url='+a
				cmd += '" http://friendfeed-api.com/v2/entry'
				self.msg = os.popen(cmd).read()
				os.system('clear')
				self.isError()
