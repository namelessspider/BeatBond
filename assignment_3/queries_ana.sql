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
