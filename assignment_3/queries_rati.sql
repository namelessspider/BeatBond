--return names and base id of all users with same genre profile--
SELECT 
    bu.name AS "name", 
    bu.lastname AS "last name", 
    bu.baseId AS "base ID"  
FROM 
    BaseUser bu, 
    Users u, 
    Likes_Music lm, 
    MusicalProfile mp 
WHERE 
    mp.genre = "Pop" AND 
    mp.mpid = lm.mpid AND 
    lm.uid = u.uid AND 
    u.baseId = bu.baseId;

--returns chat messeges send by one user to another--
SELECT
    CONCAT(sbu.name, " ", sbu.lastname) AS "Sender FUll Name",
    CONCAT(rbu.name, " ", rbu.lastname) AS "Reciever FUll Name",    
    msg.messageText,
    msg.messageImange,
    msg.MessageVideo
FROM
    Users su,
    Users ru,
    Massaged_to mt,
    Messeges msg,
    BaseUser sbu,
    BaseUser rbu
WHERE
    su.uid = 101 AND ru.uid = 102 AND
    mt.senderUid = su.uid AND
    msg.chatId = mt.chatId AND
    su.baseId = sbu.baseId AND
    ru.baseId = rbu.baseId;

--returns recommended song by genre--
SELECT
    CONCAT(bu.name, " ", bu.lastname) AS "FUll Name",
    rmp.song AS "Recommended song by Genre",
    rmp.mpid 

FROM
    Users u,
    BaseUser bu,
    MusicalProfile mp,
    Likes_Music lm,
    MusicalProfile rmp

WHERE
    u.uid = 101 AND
    bu.baseId = u.baseId AND
    lm.uid = u.uid AND
    mp.mpid = lm.mpid AND
    rmp.genre = mp.genre AND
    rmp.mpid != mp.mpid
ORDER BY RAND()
LIMIT 1;
<<<<<<< HEAD
<<<<<<< HEAD:assignment_3/queries_rati.sql
=======

--returns recommended song by vibe--
SELECT
    CONCAT(bu.name, " ", bu.lastname) AS "FUll Name",
    rmp.song AS "Recommended song by Vibe",
    rmp.mpid 

FROM
    Users u,
    BaseUser bu,
    MusicalProfile mp,
    Likes_Music lm,
    MusicalProfile rmp

WHERE
    u.uid = 101 AND
    bu.baseId = u.baseId AND
    lm.uid = u.uid AND
    mp.mpid = lm.mpid AND
    rmp.vibe = mp.vibe AND
    rmp.mpid != mp.mpid
ORDER BY RAND()
LIMIT 1;

--returns list of people users swiped right on--
SELECT 
    CONCAT(bu.name, " ", bu.lastname) AS "FUll Name", 
    u.uid AS "User ID"

FROM 
    Users su,
    Swiped_On so,
    Swipes s,
    Users u,
    BaseUser bu
WHERE 
    su.uid = 101 AND
    so.swiperUid = su.uid AND
    so.swipeId = s.swipeId AND
    s.liked = TRUE AND
    s.uid = u.uid AND
    bu.baseId = u.baseId;
--returns list of people blocked by user--
SELECT 
    CONCAT(bu.name, " ", bu.lastname) AS "Full Name", 
    u.uid AS "User ID"

FROM 
    Users su,
    Blocked_Users blu,
    BlockedUsers bus,
    Users u,
    BaseUser bu
WHERE 
    su.uid = 101 AND
    su.uid = blu.uid AND
    bus.blockId = blu.blockId AND
    bus.uid = u.uid AND
    bu.baseId = u.baseId; 

--returns list of people person has matched with--

SELECT 
    CONCAT(bu.name, " ", bu.lastname) AS "Full Name", 
    mu.uid AS "User ID"

FROM 
    Users u,
    Matched_Users_With blu,
    Matches m,
    Users mu,
    BaseUser bu
WHERE 
    u.uid = 101 AND
    blu.uid = u.uid AND
    blu.matchId = m.matchId AND
    m.uid = mu.uid AND
    mu.baseId = bu.baseId; 

--returns list of people person could see on their feed--
SELECT 
    CONCAT(bu.name, " ", bu.lastname) AS "Full Name", 
    mu.uid AS "User ID"

FROM 
    Users u,
    has_possible_matches hpm,
    PossibleMatches pm,
    Users mu,
    BaseUser bu
WHERE 
    u.uid = 101 AND
    hpm.uid = u.uid AND
    hpm.mid = pm.mid AND
    pm.uid = mu.uid AND
    bu.baseId = mu.baseId; 
    
>>>>>>> 2600ce1515024ab65f3892c236566432a5cea927:assignment_3/queries.sql
=======
>>>>>>> 9b015422f4115a6dc66192002e255e292a7ac0ec
