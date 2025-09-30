#!/people/home/rvardiashv/public_html/.env/bin/python3.8
import cgi
import cgitb
import random
import traceback
import os
import sys
import http.cookies as Cookies


cgitb.enable()
sys.path.append("../system/")
sys.path.append("..")
from config import LOGDIR
from db import insert
from user import User

print('Content-type: text/html')
form = cgi.FieldStorage()

def login():
	key = User.authenticate(form.getvalue('email'), form.getvalue('password'))
	if(key == -1 or key == -2):
		print('')
		print('cannot authenticate with given credentials')
		print(str(key))
		return
	cookie = Cookies.SimpleCookie()
	cookie['session_key'] = key
	cookie['session_key']['httponly'] = True
	print(cookie.output())
	print('')
	print('<p>successfully logged in</p>')

if __name__ == "__main__":
	try:
		login()
	except:
		with open(LOGDIR+"/exceptions.log", "a") as logfile:
			traceback.print_exc(file=logfile)
		raise
