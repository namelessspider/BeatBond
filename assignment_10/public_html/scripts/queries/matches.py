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
output = ""
form = cgi.FieldStorage()
uid = form.getvalue("uid")
if(uid == None):
	uid = ""
if(uid!=''):
	data = db.execute(
	'''	SELECT 
        	CONCAT(bu.name, " ", bu.lastname) AS "Full Name", 
        	mu.uid AS "User ID"

       		FROM 
        	Users u,
	        Matched_Users_With blu,
        	Matches m,
        	Users mu,
        	BaseUser bu
	        WHERE 
        	u.uid = {} AND
        	blu.uid = u.uid AND
        	blu.matchId = m.matchId AND
       		m.uid = mu.uid AND
        	mu.baseId = bu.baseId; 
    	'''.format(uid)
	).split('\n')


	keys = data[0].split('\t')
	result = []
	if(len(data) > 1):
		for i in range(1, len(data)-1):
			variables = data[i].split('\t')
			dict = {}
			for j in range(0, len(keys)):
				dict[keys[j]] = variables[j]
			dict['More'] = '<a href="details.py?type=matches&vars={}&vars={}">details</a>'.format(uid, dict['User ID'])
			result.append(dict)
		output = tabulate.tabulate(result, headers="keys", tablefmt="unsafehtml")
	else: 
		output = "No matches found for user with given uid\n query."

print("<html>")
print("<head>")
print(js("GetData/uid.py"))
print("<link rel='stylesheet' href='db_viewer.css'>")
print("</head>")
print("<body>")
print("<p>input User Id(uid) to get all matches of an user</p>")
print("<form method='get'>")
print("<label for='uid'>Uid:</label>")
print("<input type='text' class='autocomplete' name='uid' value = '{}'>".format(uid))
print("<input type='submit' value='Create Table'>")
print("</form>")
print(output)
print("</body>")
print("</html>")
