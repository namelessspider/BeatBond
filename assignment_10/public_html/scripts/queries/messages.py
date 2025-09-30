#!/people/home/rvardiashv/public_html/.env/bin/python3
import cgi
import cgitb
import traceback
import sys
import os
import tabulate
from auto_complete import js
sys.path.append("..")
sys.path.append("../system/")

import db

print('Content-Type: text/html')
print('')

output = ""
form = cgi.FieldStorage()
uid1 = form.getvalue('uid1')
uid2 = form.getvalue('uid2')
if(uid1 == None):
        uid1 = ""

if(uid2 == None):
        uid2 = ""

if(uid1 != '' and uid2 != ''):
	data = db.execute(
        '''
	SELECT
	CONCAT(sbu.name, " ", sbu.lastname) AS "Sender FUll Name",
	CONCAT(rbu.name, " ", rbu.lastname) AS "Reciever FUll Name",    
	msg.messageText,
	msg.media,
	msg.chatId as "cid"
	FROM
	Users su,
	Users ru,
	Massaged_to mt,
	Messeges msg,
	BaseUser sbu,
	BaseUser rbu
	WHERE
	su.uid = {} AND ru.uid = {} AND
	mt.senderUid = su.uid AND
	mt.recieverUid = ru.uid AND	
	msg.chatId = mt.chatId AND
	su.baseId = sbu.baseId AND
	ru.baseId = rbu.baseId; '''.format(uid1, uid2)
        ).split('\n')
	keys = data[0].split('\t')
	result = []
	if(len(data)>1):
		for i in range(1, len(data)-1):
			variables = data[i].split('\t')
			dict = {}
			for j in range(0, len(keys)):
				dict[keys[j]] = variables[j]
			dict['More'] = '<a href="details.py?type=message&vars={}&vars={}&vars={}">details</a>'.format(uid1, uid2, dict['cid']) 
			result.append(dict)
		output = tabulate.tabulate(result, headers="keys", tablefmt="unsafehtml")
	else:
		output = "no chats found send by user 1 to user 2"
print("<html>")
print("<head>")
print("<link rel='stylesheet' href='db_viewer.css'>")
print(js('GetData/uid.py'))
print("</head>")
print("<body>")
print("<p>Input user id(uid) of users you want to see chat messeges between</p>")
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

