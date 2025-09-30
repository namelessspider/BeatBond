#!/people/home/rvardiashv/public_html/.env/bin/python3
import cgi
import cgitb
import traceback
import sys
import tabulate
import os

print('Content-Type: text/html')
print('')

sys.path.append("..")
sys.path.append("../system/")
import db

form = cgi.FieldStorage()
table = form.getvalue("table")
conditions = form.getvalue("cond")
if(table == None):
	table = ""
if(conditions == None):
	conditions = ""
data = db.getData(table, conditions)
output = tabulate.tabulate(data, headers="keys", tablefmt="html")
print("<html>")
print("<head>")
print("<link rel='stylesheet' href='db_viewer.css'>")
print("</head>")
print("<body>")
print("<form method='get'>")
print("<label for='table'>Table:</label>")
print("<input type='text' name='table' value = '{}'>".format(table))
print("<label for='cond'>conditions:</label>")
print("<input type='text' name='cond' value = '{}'>".format(conditions))
print("<input type='submit' value='Create Table'>")
print("</form>")
print(output)
print("</body>")
print("</html>")
