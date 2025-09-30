#!/people/home/rvardiashv/public_html/.env/bin/python3
import os
import subprocess
import random
import sys
sys.path.append("..")
from config import TMPDIR
from config import LOGDIR
from config import DATABASE_USER
from config import DATABASE_PASS

def insert(table, variables, values):
        sql_command = "INSERT INTO {} {} VALUES {};".format(table, variables, values)

        try:
                out = execute(sql_command)
        except subprocess.CalledProcessError as grepexc:   
                out = "error " + str(grepexc.returncode) + str(grepexc.output) + str(grepexc)
                with open(LOGDIR+"db_errors", 'w') as file:
                        file.write(out)

        return out

def execute(sql):
       filename = TMPDIR+"/temp{}.sql".format(random.randint(1, 9999))
       fp = open(filename, 'w')
       fp.write(sql)       
       fp.close()
       result = ""
       result_str = ""
       errors = ""
       try:
              result = subprocess.run("mariadb -u{} -p{} Group-16 < {}".format(DATABASE_USER, DATABASE_PASS, filename), shell = True, stdout=subprocess.PIPE, stderr = subprocess.PIPE)
              result_str = str(result.stdout.decode('utf-8'))
              errors = result.stderr.decode('utf-8')	      
       except Exception as e:
              with open(LOGDIR+"db_error_log", "a") as file:
                     file.write("output: " + result_str + "\n")
                     file.close()
       with open(LOGDIR+"db_log", "a") as file:
              file.write("output: " + result_str + "\n")
              file.close()
       if(result_str == ""):
              result_str = errors

       return result_str

def getData(table, conditions = "", select = '*'):
	if(conditions != ""):
		conditions = "WHERE " + conditions
	out = execute("SELECT {} FROM {} {};".format(select, table, conditions))
	out = out.split('\n')
	keys = out[0].split('\t')
	result = []
	for i in range(1, len(out)-1):
		variables = out[i].split('\t')
		data = {}
		for j in range(0, len(keys)):
			data[keys[j]] = variables[j]
		result.append(data)
	return result





