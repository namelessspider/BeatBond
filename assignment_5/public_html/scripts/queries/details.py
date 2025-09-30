#!/people/home/rvardiashv/public_html/.env/bin/python3
import cgi
import cgitb
import traceback
import sys
import tabulate
import os


print('Content-Type: text/html')
print('')

print("<link rel='stylesheet' href='db_viewer.css'>")

sys.path.append("..")
sys.path.append("../system/")
import db
from user import User
from config import LOGDIR
form = cgi.FieldStorage()
type = form.getvalue('type')
vars = form.getvalue('vars')

def main():
	if(type == 'swipe'):
		swipe(vars[0], vars[1])
	elif(type == 'matches'):
		matches(vars[0], vars[1])
	elif(type == 'matchingMusic'):
		matchingMusic(vars[0], vars[1])
	elif(type=='message'):
		messagesWith(vars[0], vars[1], vars[2])
def swipe(swiper, swiped):
	data = User.swipeData(swiper, swiped)	
	output = tabulate.tabulate(data, headers="keys", tablefmt="unsafehtml")
	print(output)

def matches(uid, mid):
	data=db.getData(
	'Matches m, Matched_Users_With mu, Users u1, Users u2, BaseUser bu1, BaseUser bu2 ',
	'm.uid={} AND m.matchId = mu.matchId AND mu.uid={} AND mu.uid = u1.uid AND m.uid = u2.uid AND bu1.baseId = u1.baseId AND bu2.baseId = u2.baseId'.format(mid, uid )
	)
	output = tabulate.tabulate(data, headers="keys", tablefmt="unsafehtml")
	print(output)

def matchingMusic(mpid1,mpid2):
	user1 = db.getData(
	'MusicalProfile mp, Likes_Music lm, Users u, BaseUser bu',
	'mp.mpid = {} AND mp.mpid = lm.mpid AND lm.uid = u.uid AND bu.baseId = u.baseId'.format(mpid1),
	'bu.baseId, u.uid, bu.name, bu.lastname, bu.nationality, bu.dob, bu.gender, bu.email'
	)
	mp1 = db.getData(
        'MusicalProfile mp, Likes_Music lm',
        'mp.mpid = {} AND mp.mpid = lm.mpid'.format(mpid1) 
        )

	user2 = db.getData(
	'MusicalProfile mp, Likes_Music lm, Users u, BaseUser bu', 
	'mp.mpid = {} AND mp.mpid = lm.mpid AND lm.uid = u.uid AND bu.baseId = u.baseId'.format(mpid2),
	'bu.baseId, u.uid, bu.name, bu.lastname, bu.nationality, bu.dob, bu.gender, bu.email'
        )
	mp2 = db.getData(
        'MusicalProfile mp, Likes_Music lm',
        'mp.mpid = {} AND mp.mpid = lm.mpid'.format(mpid2) 
        )

	table1 = tabulate.tabulate(user1, headers="keys", tablefmt="unsafehtml")
	table2 = tabulate.tabulate(mp1, headers="keys", tablefmt="unsafehtml")
	table3 = tabulate.tabulate(user2, headers="keys", tablefmt="unsafehtml")
	table4 = tabulate.tabulate(mp2, headers="keys", tablefmt="unsafehtml")
	print('<p>User 1</p>')
	print(table1)
	print('<br>')
	print('<p>User 1 musical profile</p>')
	print(table2)
	print('<br>')
	print('<p>User 2</p>')
	print(table3)
	print('<br>')
	print('<p>User 2 musical profile</p>')
	print(table4)


def messagesWith(uid1, uid2, chatId):
	user1 = []
	user1_ = db.getData(
	'BaseUser bu, Users u, Massaged_to mt, Messeges m',
	'm.chatId = {} AND mt.chatId = m.chatId AND mt.senderUid={} AND u.uid = mt.senderUid AND u.baseId = bu.baseId'.format(chatId, uid1),
	'bu.baseId, u.uid, bu.name, bu.lastname, bu.nationality, bu.dob, bu.gender, bu.email'
	)[0]
	user1.append(user1_)
	user2 = db.getData(
        'BaseUser bu, Users u, Massaged_to mt, Messeges m',
        'm.chatId = {} AND mt.chatId = m.chatId AND mt.recieverUid={} AND u.uid = mt.senderUid AND u.baseId = bu.baseId'.format(chatId, uid2),
        'bu.baseId, u.uid, bu.name, bu.lastname, bu.nationality, bu.dob, bu.gender, bu.email' 
        )

	messaged = db.getData(
	'Messeges m',
	'chatId={}'.format(chatId)
	)

	table1 = tabulate.tabulate(user1, headers="keys", tablefmt="unsafehtml")
	table2 = tabulate.tabulate(messaged, headers="keys", tablefmt="unsafehtml")
	table3 = tabulate.tabulate(user2, headers="keys", tablefmt="unsafehtml")

	print('<p>User 1</p>')
	print(table1)
	print('<br>')
	print('<p>User 2</p>')
	print(table3)
	print('<br>')
	print('<p>message</p>')
	print(table2)


if __name__ == "__main__":
	try:
		main()
	except:
		with open(LOGDIR+"/exceptions.log", "a") as logfile:
			traceback.print_exc(file=logfile)
	raise


