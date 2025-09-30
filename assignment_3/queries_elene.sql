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
    

--returns list of people who listen Artists from the same Nationalities
SELECT  
    bu.name AS "name",
    bu.lastname AS "last name",
    bu.baseId AS "base ID"  
FROM 
    BaseUser bu,
    BaseUser abu, 
    Users u, 
    Likes_Music lm, 
    MusicalProfile mp,
    ArtistUsers a
WHERE 
    abu.nationality = "German" AND
    mp.mpid = lm.mpid AND 
    lm.uid = u.uid AND 
    u.baseId = bu.baseId AND
    a.baseId = bu.baseId AND
    mp.Artist = abu.name;
