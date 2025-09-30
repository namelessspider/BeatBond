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

from datetime import datetime
from user import User
from config import LOGDIR
from config import USERIMAGES
from config import TMPDIR

os.environ['TMPDIR'] = TMPDIR

form = cgi.FieldStorage()

print('<a href = "../../HTML/maintain.html">Maintanance Page</a>')
def pic():
	uid = form.getvalue('uid')
	picture = form['img']
	print('a')	
	picturePath = USERIMAGES + '/uploads/' + str(uid) + str(datetime.now().strftime('%Y%m%d%H%M%S%f'))[:-5] + '.' + picture.filename.split('.')[-1]
	user = User.getUser(uid)
	
	if(user == -1):
		print('no user found with uid: ' + str(uid))
		return
	open(picturePath, 'wb').write(picture.file.read())
	out = str(user.addPicture(path = picturePath))
	
	if(out == ''):
		print('<p>success</p>')
	else:
		print('<p>something went wrong. output: ' + out + '</p>')

if __name__ == "__main__":
	try:
		if(session_key):
			user = User.authKey(session_key.value)
			if(user and user.admin):
				pic()
			else:
				auth.notAuth()
		else:
			auth.notAuth()
	except:
		with open(LOGDIR+"/exceptions.log", "a") as logfile:
			traceback.print_exc(file=logfile)
		raise
