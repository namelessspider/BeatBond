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
uid1 = form.getvalue("uid1")
uid2 = form.getvalue("uid2")
output = ''

if(uid1 == None):
	uid1 = ""
if(uid2 == None):
	uid2 = ""
if(uid1 != '' and uid2 != ''):
	data = db.execute(
	'''SELECT
    	mp1.artist AS "Artist",
    	mp1.song AS "Song",
    	CONCAT(bu1.name, ' ', bu1.lastname) AS "User 1 Name",
	mp1.mpid as "mpid 1",
    	mp1.listening_time AS "User 1 time listened",
    	CONCAT(bu2.name, ' ', bu2.lastname) AS "User 2 Name",
    	mp2.mpid as "mpid 2",
	mp2.listening_time AS "User 2 time listened"
	FROM
    	Users u1, Likes_Music lm1, MusicalProfile mp1, BaseUser bu1,
    	Users u2, Likes_Music lm2, MusicalProfile mp2, BaseUser bu2
	WHERE
    	u1.uid = {}
    	AND u2.uid = {}
    	AND u1.uid = lm1.uid
    	AND lm1.mpid = mp1.mpid
    	AND u2.uid = lm2.uid
    	AND lm2.mpid = mp2.mpid
    	AND u1.baseId = bu1.baseId
    	AND u2.baseId = bu2.baseId
    	AND mp2.song = mp1.song
    	AND mp2.artist = mp2.artist;
   	'''.format(uid1, uid2)
	).split('\n')

	keys = data[0].split('\t')
	result = []
	if(len(data)>1):
		for i in range(1, len(data)-1):
			variables = data[i].split('\t')
			dict = {}
			for j in range(0, len(keys)):
				dict[keys[j]] = variables[j]
			dict['More'] = '<a href="details.py?type=matchingMusic&vars={}&vars={}">details</a>'.format(dict['mpid 1'], dict['mpid 2'])
			result.append(dict)
		output = tabulate.tabulate(result, headers="keys", tablefmt="unsafehtml")
	else:
		output = "no matching songs found with given users"

print("<html>")
print("<head>")
print("<link rel='stylesheet' href='db_viewer.css'>")
print(js('GetData/uid.py'))
print("</head>")
print("<body>")
print("<p>Input User Id(uid) of a users you want to check matching songs for</p>")
print("<form method='get'>")
print("<label for='uid'>Uid1:</label>")
print("<input type='text' class = 'autocomplete' name='uid1' value = '{}'>".format(uid1))
print("<label for='uid'>Uid2:</label>")
print("<input type='text' class = 'autocomplete' name='uid2' value = '{}'>".format(uid2))
print("<input type='submit' value='Create Table'>")
print("</form>")
print(output)
print("</body>")
print("</html>")
