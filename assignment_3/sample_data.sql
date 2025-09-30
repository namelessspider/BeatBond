-- Sample data for BaseUser table
INSERT INTO BaseUser (baseId, name, lastname, gender, dob, email, password)
VALUES
    (1, 'John', 'Doe', 'Male', '1990-01-15', 'john.doe@example.com', 'password123'),
    (2, 'Jane', 'Smith', 'Female', '1995-03-20', 'jane.smith@example.com', 'securepwd456'),
    (3, 'Alice', 'Johnson', 'Female', '1988-07-10', 'alice.johnson@example.com', 'mypassword789');

-- Sample data for Users table
INSERT INTO Users (baseId, uid, profile_picture)
VALUES
    (1, 101, 'base64encodedimage1'),
    (2, 102, 'base64encodedimage2'),
    (3, 103, 'base64encodedimage3');

-- Sample data for AdminUsers table
INSERT INTO AdminUsers (baseId, aid)
VALUES
    (1, 201),
    (2, 202);

-- Sample data for ArtistUsers table
INSERT INTO ArtistUsers (baseId, ArtistId)
VALUES
    (2, 301),
    (3, 302);

-- Sample data for PossibleMatches table
INSERT INTO PossibleMatches (mid, uid)
VALUES
    (1, 101),
    (2, 102),
    (3, 103);

-- Sample data for Preferences table
INSERT INTO Preferences (uid, relationshipType, gender, minAge, maxAge, muscial_genre)
VALUES
    (101, 'Dating', 'F', 25, 35, 'Pop'),
    (102, 'Friendship', 'M', 20, 30, 'Rock'),
    (103, 'Dating', 'M', 30, 40, 'Jazz');

-- Sample data for MusicalProfile table
INSERT INTO MusicalProfile (mpid, genre, artist, abloum, song, vibe)
VALUES
    (1, 'Pop', 'Artist 1', 'Album 1', 'Song 1', 'Happy'),
    (2, 'Rock', 'Artist 2', 'Album 2', 'Song 2', 'Energetic'),
    (3, 'Jazz', 'Artist 3', 'Album 3', 'Song 3', 'Relaxing');

-- Sample data for Swipes table
INSERT INTO Swipes (SwipeId, uid, liked)
VALUES
    (1, 101, TRUE),
    (2, 102, FALSE),
    (3, 103, TRUE);

-- Sample data for Messeges table
INSERT INTO Messeges (chatId, messageText, messageImange, messageVideo, date)
VALUES
    (1, 'Hello!', NULL, NULL, '2023-01-01'),
    (2, 'Hi there!', NULL, NULL, '2023-01-02'),
    (3, NULL, 'base64encodedimage', NULL, '2023-01-03');

-- Sample data for Matches table
INSERT INTO Matches (uid, matchId)
VALUES
    (101, 1),
    (103, 1);

-- Sample data for BlockedUsers table
INSERT INTO BlockedUsers (uid, blockId)
VALUES
    (101, 201),
    (102, 202);

-- Sample data for Pictures table
INSERT INTO Pictures (uid, pictureId, picture)
VALUES
    (101, 1, 'base64encodedimage1'),
    (102, 2, 'base64encodedimage2');

-- Sample data for Massaged_to table
INSERT INTO Massaged_to (senderUid, recieverUid, chatId)
VALUES
    (101, 102, 1),
    (102, 101, 1);

-- Sample data for Blocked_Users table
INSERT INTO Blocked_Users (uid, blockId)
VALUES
    (101, 202),
    (103, 201);

-- Sample data for Matched_Users_With table
INSERT INTO Matched_Users_With (uid, matchId)
VALUES
    (101, 1),
    (103, 2);

-- Sample data for Swiped_On table
INSERT INTO Swiped_On (swiperUid, swipeId)
VALUES
    (101, 1),
    (102, 2);

-- Sample data for Likes_Music table
INSERT INTO Likes_Music (uid, mpid)
VALUES
    (101, 1),
    (102, 2);

-- Sample data for has_possible_matches table
INSERT INTO has_possible_matches (uid, mid)
VALUES
    (101, 1),
    (102, 2);
