#!/people/home/rvardiashv/public_html/.env/bin/python3.8

import tempfile
import cgi
import cgitb
import random
import traceback
import os
import sys
import bcrypt
import http.cookies as Cookies
import auth

cgitb.enable()
print('Content-Type: text/html')
print('')

cookie = Cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))
session_key = cookie.get('session_key')

sys.stdout.flush()
sys.path.append("../system/")
sys.path.append("..")
from config import TMPDIR
from config import USERIMAGES
from config import LOGDIR
from db import getData
from user import User
os.environ['TMPDIR'] = TMPDIR
form = cgi.FieldStorage()
print('<a href = "../../HTML/maintain.html">Maintanance Page</a>')

def addUser():
	name = form.getvalue('name')
	lastname = form.getvalue('lastname')
	gender = form.getvalue('gender')
	dob = form.getvalue('dob')
	email = form.getvalue('email')
	password = form.getvalue('password')
	nation = form.getvalue('nationality')
	artistName = form.getvalue('artist')
	artistType = form.getvalue('type')

	users = User.getAllUsers()
	
	bid = len(users[1])
	uid = int('20'+str(bid))
	password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

	
	newuser = User(bid=bid, uid=uid, name=name, lastname=lastname, email=email, gender=gender, nationality=nation, dob=dob, password=password, artist=artistName, artistType = artistType)
	output = newuser.create("artist")
	if(output == ''):
		print('<p>success</p>')
	else:
		print('<p>something went wrong. output: {}'.format(output))	

if __name__ == "__main__":
    try:
        if session_key:
            user = User.authKey(session_key.value)
            if user and user.admin:
                addUser()
            else:
                auth.notAuth()
        else:
            auth.notAuth()
    except Exception as e:
        with open(LOGDIR + "/exceptions.log", "a") as logfile:
            traceback.print_exc(file=logfile)
        raise 
