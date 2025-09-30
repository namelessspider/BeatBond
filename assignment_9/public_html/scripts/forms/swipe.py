#!/people/home/rvardiashv/public_html/.env/bin/python3.8
import cgi
import cgitb
import sys
import os
import traceback
import http.cookies as Cookies
import auth

cgitb.enable()
print('Content-Type: text/html')
print('')

cookie = Cookies.SimpleCookie(os.environ.get('HTTP_COOKIE'))
session_key =  cookie.get('session_key')

sys.path.append("../system/")
sys.path.append("..")

from config import LOGDIR
from user import User

form = cgi.FieldStorage()
print('<a href = "../../HTML/maintain.html">Maintanance Page</a>')
def swipe():
	swiper = form.getvalue("swiper")
	swiped = form.getvalue("swiped")
	dir  = form.getvalue("dir")
	print(swiper)
	print(swiped)
	swiperUser = User.getUser(swiper)
	swipedUser = User.getUser(swiped)
	if(swiperUser == -1):
		print('can not swipe no user with uid: ' + str(swiper))
		return
	if(swipedUser == -1):
		print('can not swipe no user with uid: ' + swiped)
		return

	output = swiperUser.swipe(uid = swiped, liked = dir == 'liked')
	if(output == ''):
		print('<p>success</p>')
	else:
		print('<p>something went wrong. output: {}'.format(output))    


if __name__ == "__main__":
    try:
        if session_key:
            user = User.authKey(session_key.value)
            if user and user.admin:                  
                swipe()
            else:
                auth.notAuth()
        else:
            auth.notAuth()
    except:
        with open(LOGDIR+"/exceptions.log", "a") as logfile:
            traceback.print_exc(file=logfile)
        raise
