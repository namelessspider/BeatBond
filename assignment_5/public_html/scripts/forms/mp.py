#!/people/home/rvardiashv/public_html/.env/bin/python3.8
import tempfile
import cgi
import cgitb
import random
import traceback
import os
import sys
import http.cookies as Cookies
import auth


cgitb.enable()
print('Content-Type: text/html')
print('')
sys.path.append("../system/")
sys.path.append("..")
from config import TMPDIR
from config import USERIMAGES
from config import LOGDIR
from db import insert
from user import User
os.environ['TMPDIR'] = TMPDIR
form = cgi.FieldStorage()
cookie = Cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))
session_key = cookie.get('session_key')


print('<a href = "../../HTML/maintain.html">Maintanance Page</a>')

def main():
	addMp()

def addMp():
	genre = form.getvalue("genre")
	artist = form.getvalue("artist")
	uid = form.getvalue("uid")
	album = form.getvalue("album")
	song = form.getvalue("song")
	vibe = form.getvalue("vibe")
	year = form.getvalue("year")
	time = form.getvalue("time")
	user = User.getUser(uid)
	result = user.addMP(
		genre = genre, artist = artist, album = album, song = song, vibe = vibe, release_year = year, listening_time = time             
	)
	if(result == ''):
		print('<p>success</p>')
	else:
		print('<p>something went wrong. output: ' + result + '</p>')

if __name__ == "__main__":
	try:
		if(session_key):
			user = User.authKey(session_key.value)
			if(user and user.admin):
				main()
			else:
				auth.notAuth()
		else:
			auth.notAuth()
	except:
		with open(LOGDIR+"/exceptions.log", "a") as logfile:
			traceback.print_exc(file=logfile)
		raise
