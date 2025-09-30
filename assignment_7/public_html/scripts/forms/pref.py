#!/people/home/rvardiashv/public_html/.env/bin/python3
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
from user import User
from config import LOGDIR
form = cgi.FieldStorage()
print('<a href = "../../HTML/maintain.html">Maintanance Page</a>')

def createPreferences():
	uid = form.getvalue("uid")
	genre = form.getvalue("genre")
	minAge = form.getvalue("minAge")
	maxAge = form.getvalue("maxAge")
	female = form.getvalue("female")
	male = form.getvalue("male")
	other_gen = form.getvalue("other_gen")
	friendship = form.getvalue("friend")
	dating = form.getvalue("date")
	ltr = form.getvalue("ltr")
	hookup = form.getvalue("hookup")
	other_rel = form.getvalue("other_rel")

	rel_type = str(friendship) + "|" +  str(dating) + "|" + str(ltr) + "|" + str(hookup) + "|" + str(other_rel)
	gender = str(female) + "|" + str(male) + "|" + str(other_gen)

	result = User.getUser(uid).createPreferences(rel_type, gender, minAge, maxAge, genre)
	if(result == ''):
		print('<p>success</p>')
	else:
		print('<p>something went wrong. output: '+result+'</p>')


if __name__ == "__main__":
    try:
        if session_key:
            user = User.User.authKey(session_key.value)
            if user and user.admin:
                addUser()
            else:
                auth.notAuth()
        else:
            auth.notAuth()
    except:
        with open(LOGDIR + "/exceptions.log", "a") as logfile:
            traceback.print_exc(file=logfile)
        raise 

