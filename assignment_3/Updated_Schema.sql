CREATE TABLE BaseUser(
    baseId INT NOT NULL UNIQUE,
    name CHAR(255) NOT NULL, 
    lastname CHAR(255) NOT NULL,
    gender CHAR(255) NOT NULL,
    dob DATE NOT NULL,
    email CHAR(255) NOT NULL UNIQUE,
    nationality CHAR(255) NOT NULL,
    password CHAR(255),
    PRIMARY KEY(baseId)
);

CREATE TABLE Users(
    baseId INT NOT NULL,
    uid INT NOT NULL UNIQUE,
    profile_picture LONGBLOB NOT NULL,
    PRIMARY KEY (uid),
    Foreign Key (baseId) REFERENCES BaseUser(baseId)
);
CREATE TABLE AdminUsers(
    baseId INT NOT NULL,
    aid INT NOT NULL UNIQUE,
    Foreign Key (baseId) REFERENCES BaseUser(baseId),
    PRIMARY KEY (aid)
);
CREATE TABLE ArtistUsers(
    baseId INT NOT NULL,
    ArtistId INT NOT NULL UNIQUE,
    Foreign Key (baseId) REFERENCES BaseUser(baseId),
    PRIMARY KEY(ArtistId)
);
CREATE TABLE PossibleMatches(
    mid INT NOT NULL UNIQUE,
    uid INT NOT NULL,
    PRIMARY KEY (mid),
    Foreign Key (uid) REFERENCES Users(uid)
);

CREATE TABLE Preferences(
    uid INT NOT NULL,
    relationshipType CHAR(255) NOT NULL,
    gender CHAR(1),
    minAge INT NOT NULL,
    maxAge INT NOT NULL,
    muscial_genre CHAR(255) NOT NULL,
    PRIMARY KEY(uid),
    FOREIGN KEY(uid)
    REFERENCES Users(uid)
);

CREATE TABLE MusicalProfile(
    mpid INT NOT NULL UNIQUE,
    genre CHAR(255) NOT NULL,
    artist CHAR(255) NOT NULL,
    abloum CHAR(255) NOT NULL,
    song CHAR(255) NOT NULL,
    vibe CHAR(255) NOT NULL,
    song_release_year INT NOT NULL,
    listening_time INT NOT NULL,
    PRIMARY KEY(mpid)
);

CREATE TABLE Swipes(
    SwipeId INT NOT NULL UNIQUE,
    uid INT NOT NULL,
    liked BOOL,
    PRIMARY KEY(SwipeId),
    FOREIGN KEY(uid)
    REFERENCES Users(uid)
);

CREATE TABLE Messeges(
    chatId INT NOT NULL,
    messageText TEXT,
    messageImange LONGBLOB,
    messageVideo TEXT,
    date DATE NOT NULL,
    PRIMARY KEY(ChatId)
);

CREATE TABLE Matches(
    uid INT NOT NULL,
    matchId INT NOT NULL UNIQUE,
    PRIMARY KEY(matchId),
    Foreign Key (uid)
    REFERENCES Users(uid)
);

CREATE TABLE BlockedUsers(
    uid INT NOT NULL,
    blockId INT NOT NULL UNIQUE,
    PRIMARY KEY(blockId),
    FOREIGN KEY(uid)
    REFERENCES Users(uid)
);

CREATE TABLE Pictures(
    uid INT NOT NULL,
    pictureId INT NOT NULL UNIQUE,
    picture LONGBLOB NOT NULL,
    PRIMARY KEY(pictureId),
    Foreign Key (uid)
    REFERENCES Users(uid)
);

CREATE TABLE Massaged_to(
    senderUid INT NOT NULL,
    recieverUid INT NOT NULL,
    chatId INT NOT NULL,
    PRIMARY KEY(senderUid, recieverUid, chatId),
    Foreign Key (senderUid) REFERENCES Users(uid),
    Foreign Key (recieverUid) REFERENCES Users(uid),
    Foreign Key (chatId) REFERENCES Messeges(chatId)
);

CREATE TABLE Blocked_Users (
    uid INT NOT NULL,
    blockId INT NOT NULL,
    PRIMARY KEY(uid, blockID),
    FOREIGN KEY (Uid) REFERENCES Users (uid),
    Foreign Key (blockId) REFERENCES BlockedUsers(blockId)
);

CREATE TABLE Matched_Users_With (
    uid INT NOT NULL,
    matchId INT,
    PRIMARY KEY(uid, matchId),
    FOREIGN KEY (uid) REFERENCES Users (uid),
    FOREIGN KEY (matchId) REFERENCES Matches(matchId)
);

CREATE TABLE Swiped_On (
    swiperUid INT NOT NULL,
    swipeId INT NOT NULL,
    PRIMARY KEY (SwiperUid, SwipeId),
    FOREIGN KEY (SwiperUid) REFERENCES Users (uid),
    FOREIGN KEY (SwipeId) REFERENCES Swipes (SwipeId)
);

CREATE TABLE Likes_Music (
    uid INT NOT NULL,
    mpid INT NOT NULL,
    PRIMARY KEY (uid, mpid),
    FOREIGN KEY (uid) REFERENCES Users (uid),
    FOREIGN KEY (mpid) REFERENCES MusicalProfile (mpid)
);

CREATE TABLE has_possible_matches(
    uid INT NOT NULL,
    mid INT NOT NULL,
    PRIMARY KEY(uid, mid),
    Foreign Key (uid) REFERENCES Users(uid),
    Foreign Key (mid) REFERENCES PossibleMatches(mid)
);
