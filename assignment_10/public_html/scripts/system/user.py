#!/people/home/rvardiashv/public_html/.env/bin/python3

import db
import traceback
import sys
import random
from datetime import datetime
sys.path.append("..")
from config import LOGDIR
import json
import random
import bcrypt
import string
class User():
    def __init__(self, bid, uid, name, lastname, email, gender, nationality, dob, password, profile_pic = None, artist = None, artistType = None, session_key = None, admin = False):
        self.bid = bid
        self.name = name
        self.lastname = lastname
        self.email = email
        self.profile_pic = profile_pic
        self.gender = gender
        self.nationality = nationality
        self.password = password
        self.dob = dob
        self.uid = uid
        self.artist = artist
        self.artistType = artistType
        self.session_key = session_key
        self.admin = admin
    def create(self, type):
        out1 = db.insert('BaseUser', '(name, lastname, gender, dob, email, password, baseId, nationality, session_key)', '("{}", "{}", "{}", "{}", "{}", "{}", {}, "{}", "{}")'
               	.format(self.name, self.lastname, self.gender, self.dob, self.email, self.password, self.bid, self.nationality, self.session_key))
        out2 = ""
       	if(type == "basic"):
               	out2 = db.insert('Users', '(uid, baseId, profile_picture)', '({}, {},"{}")'.format(self.uid, self.bid, self.profile_pic))
        if(type=="artist"):
                out2 = db.insert('ArtistUsers', '(artist, type, ArtistId, baseId)', '("{}", "{}", {}, {})'.format(self.artist, self.artistType, self.uid, self.bid))
        return out1+out2

    def addMP(self, genre, artist, album, song, vibe, listening_time, release_year):
        mpid = int('11' + str(self.uid)+str(len(db.getData('Likes_music', 'uid = '+ self.uid))))
        out1 = db.insert('MusicalProfile', '(mpid, genre, artist, album, song, vibe, listening_time, song_release_year)', '({}, "{}", "{}", "{}", "{}", "{}", {}, {})'.format(mpid, genre, artist, album, song, vibe, listening_time, release_year))
        out2 = db.insert('Likes_Music', '(uid, mpid)', '({}, {})'.format(self.uid, mpid))
        return out1 + out2

    def blockUser(self, uid):
        blockId = int('12' + str(self.uid))
        out1 = db.insert('BlockedUsers', '(blockId, uid)', '({}, {})'.format(blockId, uid)) 
        out2 = db.insert('Blocked_Users', '(uid, blockID)', '({}, {})'.format(self.uid, blockId))
        return out1 + out2

    
    def createPreferences(self, type, gender, minAge, maxAge, genre):
        result = db.insert('Preferences', '(uid, relationshipType, gender, minAge, maxAge, musical_genre)', '({}, "{}", "{}", {}, {}, "{}")'
                .format(self.uid, type, gender, minAge, maxAge, genre))
        return result
    
    @staticmethod
    def getUser(uid):
        try:
            uData = db.getData("Users", "uid = " + str(uid))[0]
            buData = db.getData("BaseUser", "baseId = " + uData["baseId"])[0]
        except IndexError:
            return -1 
        user = User(
                bid = buData["baseId"], uid = uData["uid"], name = buData["name"], lastname = buData["lastname"], email = buData["email"], profile_pic = uData["profile_picture"], gender = buData["gender"], nationality = buData["nationality"], dob = buData["dob"], password = buData["password"], session_key = buData["session_key"]
        )
        return user
    @staticmethod
    def getArtist(aid):
        try:
            uData = db.getData("ArtistUsers", "ArtistId = " + str(aid))[0]
            buData = db.getData("BaseUser", "baseId = " + uData["baseId"])[0]
        except IndexError:
            return -1
        user = User(	
                bid = buData["baseId"], uid = uData["ArtistId"], name = buData["name"], lastname = buData["lastname"], email = buData["email"], gender = buData["gender"], nationality = buData["nationality"], dob = buData["dob"], password = buData["password"], artistType = uData["type"], artist = uData["artist"], session_key = buData["session_key"]
        )
        return user
    @staticmethod
    def getAdmin(aid):
        try:
            uData = db.getData("AdminUsers", "aid = " + str(aid))[0]
            buData = db.getData("BaseUser", "baseId = " + uData["baseId"])[0]
        except IndexError:
            return
        user = User(    
                bid = buData["baseId"], uid = uData["aid"], name = buData["name"], lastname = buData["lastname"], email = buData["email"], gender = buData["gender"], nationality = buData["nationality"], dob = buData["dob"], password = buData["password"], session_key = buData["session_key"], admin = True
        )
        return user
    


    @staticmethod
    def getAllUsers():
        uData = db.getData("Users")
        buData = db.getData("BaseUser")
        result = [uData, buData]
        return result

    def addPicture(self, path):
        pid = int("13" + str(self.uid)+str(len(db.getData("Pictures", "uid = " + self.uid))))
        out = db.insert('Pictures', '(pictureId, uid, picture)', '({}, {}, "{}")'.format(pid, self.uid, path))
        return out

    def sendMessege(self, uid, text, media = None):
        chatId = len(db.getData('Messeges'))
        out1 = db.insert('Messeges', '(chatId, messageText, media, datetime)', '({}, "{}", "{}", "{}")'.format(chatId, text, media, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        out2 = db.insert('Massaged_to', '(senderUid, recieverUid, chatId)', '({}, {}, {})'.format(self.uid, uid, chatId))
        out = str(out1) + str(out2)
        return out

    def swipe(self, uid, liked):
        swipeId = len(db.getData('Swipes'))+1	
        out1 = db.insert('Swipes', '(swipeId, uid, liked)', '({}, {}, {})'.format(swipeId, uid, liked))
        out2 = db.insert('Swiped_On', '(swiperUid, swipeId)', '({}, {})'.format(self.uid, swipeId))
        out = str(out1) + str(out2)
        
        return out
    @staticmethod
    def swipeData(liker, liked):
        out1 = db.getData('Users u, BaseUser bu,Swiped_On so, Swipes sw', 'so.swiperUid = {} AND sw.Swipeid = so.swipeId AND sw.uid = {} AND u.uid = sw.uid AND bu.baseId = u.baseId'.format(liker, liked))
        return out1
    @staticmethod
    def getUserType(bid):
        if(len(db.getData('Users', 'baseId = ' + bid)) > 0):
            return 'basic'
        elif(len(db.getData('ArtistUsers', 'baseId = ' + bid)) > 0):
            return 'artist'
        if(len(db.getData('AdminUsers', 'baseId = ' + bid)) > 0):
            return 'admin'


    @staticmethod
    def authKey(key):
        baseUser = db.getData('BaseUser', 'session_key = "{}"'.format(key))
        user = None
        if(len(baseUser) > 0):
            userType = User.getUserType(baseUser[0]['baseId'])
            if(userType == 'basic'):
                id = db.getData('Users', "baseId = " + baseUser[0]['baseId'], "uid")
                user = User.getUser(id[0]["uid"])          
            elif(userType == 'artist'):
                id = db.getData('ArtistUsers', "baseId = " + baseUser[0]['baseId'], "ArtistId")
                user = User.getArtist(id[0]["ArtistId"])          
            elif(userType == 'admin'):
                id = db.getData('AdminUsers', "baseId = " + baseUser[0]['baseId'], "aid")
                user = User.getAdmin(id[0]["aid"])          

        return user
    
    @staticmethod
    def setKey(bid, key):
        return db.execute('UPDATE BaseUser SET session_key = "{}" WHERE baseId = {};'.format(key, bid))
    @staticmethod
    def authenticate(email, password):
        try:
            buData = db.getData("BaseUser", "email = '" + email + "'")[0]
        except IndexError:
            return -1
        if(bcrypt.checkpw(password.encode('utf-8'), buData['password'][2:-1].encode('utf-8'))):
            key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            User.setKey(buData["baseId"], key)
            return key
        else:
            return -2
