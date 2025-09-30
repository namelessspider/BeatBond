#!/people/home/rvardiashv/public_html/.env/bin/python3
import cgi
import cgitb
import traceback
import sys
import tabulate
import os
import json

print('Content-Type: application/json')
print('')

sys.path.append("../../")
sys.path.append("../../system/")
import db
data = db.getData('Users', '', 'uid')
data_array = list()
for i in data:
	data_array.append(i['uid'])


data_json = json.dumps(data_array)
print(data_json)
