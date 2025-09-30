#!/people/home/rvardiashv/public_html/.env/bin/python3.8

import cgi
import cgitb
import sys
import traceback
import http.cookies as Cookies
import auth
import os

cgitb.enable()

print('Content-Type: text/html')
print('')

cookie = Cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))
session_key = cookie.get('session_key')

sys.stdout.flush()
sys.path.append("..")
sys.path.append("../system")
from config import LOGDIR
from user import User
form = cgi.FieldStorage()
print('<a href = "../../HTML/maintain.html">Maintanance Page</a>')
def block():
	blocker = form.getvalue('blocker')
	blocked = form.getvalue('blocked')

	user = User.getUser(blocker)
	
	if(user == -1):
		result = "no user found with uid " + str(blocker) + "  | can't block user with uid " + blocked
	else:
		result = user.blockUser(uid = blocked)
	if(str(result) == ''):
		print('<p>success<p>')	
	else:
		print('<p>something went wrong. output: ' +str(result) +'<p>')


if __name__ == "__main__":
	try:
		if(session_key):
			user = User.authKey(session_key.value)
			if(user and user.admin):
				block()
			else:
				auth.notAuth()
		else:
			auth.notAuth()			
	except:
		with open(LOGDIR+"/exceptions.log", "a") as logfile:
			traceback.print_exc(file=logfile)
		raise
