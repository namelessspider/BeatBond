#!/people/home/rvardiashv/public_html/.env/bin/python3
import cgi
import cgitb
import traceback
import sys
import tabulate
import os
from auto_complete import js
print('Content-Type: text/html')
print('')

sys.path.append("..")
sys.path.append("../system/")
import db

form = cgi.FieldStorage()
uid = form.getvalue("uid")
if(uid == None):
	uid = ""
if(uid != ''):
	data = db.execute(
		'''SELECT 
    		CONCAT(bu.name, " ", bu.lastname) AS "FUll Name", 
    		u.uid AS "User ID"

		FROM 
    		Users su,
	    	Swiped_On so,
    		Swipes s,
    		Users u,
    		BaseUser bu
		WHERE 
    		su.uid = {} AND
    		so.swiperUid = su.uid AND
    		so.swipeId = s.swipeId AND
    		s.liked = TRUE AND
    		s.uid = u.uid AND
    		bu.baseId = u.baseId;'''.format(uid)
	).split('\n')


	keys = data[0].split('\t')
	result = []
	if(len(data)>1):
		for i in range(1, len(data)-1):
			variables = data[i].split('\t')
			dict = {}
			for j in range(0, len(keys)):
				dict[keys[j]] = variables[j]
			dict['More'] = '<a href="details.py?type=swipe&vars={}&vars={}">details</a>'.format(uid, dict['User ID'])
			result.append(dict)
		output = tabulate.tabulate(result, headers="keys", tablefmt="unsafehtml")
	else:
		output = "user with given uid has not swiped on anybody"
print("<html>")
print("<head>")
print("<link rel='stylesheet' href='db_viewer.css'>")
print(js('GetData/uid.py'))
print("</head>")
print("<body>")
print("<p>input User Id (uid) of an user to see if they have liked any other users")
print("<form method='get'>")
print("<label for='uid'>Uid:</label>")
print("<input type='text' class = 'autocomplete' name='uid' value = '{}'>".format(uid))
print("<input type='submit' value='Create Table'>")
print("</form>")
print(output)
print("</body>")
print("</html>")
