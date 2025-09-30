#!/people/home/rvardiashv/public_html/.env/bin/python3

print('Content-Type: text/html')
print('') 

import cgi
import cgitb
import sys
import traceback
import os
import http.cookies as Cookies
import auth

cgitb.enable()

sys.path.append('..')
sys.path.append('../system')

from datetime import datetime
from user import User
from config import LOGDIR
from config import USERIMAGES
from config import TMPDIR
import db

cookie = Cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))
session_key = cookie.get('session_key')


os.environ['TMPDIR'] = TMPDIR

form = cgi.FieldStorage()
print('<a href = "../../HTML/maintain.html">Maintanance Page</a>')

def send():
	sender = form.getvalue('sender')	
	reciever = form.getvalue('receiver')
	media = form['media']
	msgtext = form.getvalue('messageText')
	
	senderUser = User.getUser(sender) 
	if(senderUser == -1):
		print('can not send | no user with uid: ' + str(sender))
		return
	
	recieverUser = User.getUser(reciever)
	if(recieverUser == -1):
		print('can not recieve | no user with uid: ' + str(reciever))
		return
	if(media.filename == ""):
		out = senderUser.sendMessege(uid = reciever, text = msgtext)
		if(out == ''):
			print('<p>success</p>')
		else:
			print('<p> something went wrong. output: ' + out + '</p>')
		return
	
	mediaPath = USERIMAGES + '/media/' + str(sender) + str(datetime.now().strftime('%Y%m%d%H%M%S%f'))[:-5] + '.' + media.filename.split('.')[-1]
	open(mediaPath, 'wb').write(media.file.read())	
	out = senderUser.sendMessege(uid = reciever, text = msgtext, media = mediaPath)
	if(out == ''):
		print('<p>success</p>')
	else:
		print('<p>something went wrong. output: ' +  out + '</p>')
		
if __name__ == "__main__":
	try:
		if(session_key):
			user = User.authKey(session_key.value)
			if(user and user.admin):
				send()
			else:
				auth.notAuth()
		else:
			auth.notAuth()
	except:
		with open(LOGDIR+"/exceptions.log", "a") as logfile:
			traceback.print_exc(file=logfile)
		raise
