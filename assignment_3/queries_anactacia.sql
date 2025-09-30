--identify music by same music decades
SELECT 
    mp.song AS "Song",
    mp.genre AS "Genre",
    mp.artist AS "Artist",
    mp.abloum AS "Album",
    mp.vibe AS "Vibe",
    SUBSTRING(mp.song_release_year, 1, 3) AS "Decade"
FROM 
    MusicalProfile mp
WHERE 
    SUBSTRING(mp.song_release_year, 1, 3) = '200' 
ORDER BY 
    mp.song_release_year;


-- List of matched songs for two specific users (e.g., users with UID 101 and 102) without using JOIN --
SELECT
    CONCAT(bu1.name, ' ', bu1.lastname) AS "User 1 Name",
    mp1.genre AS "User 1 Genre",
    mp1.artist AS "User 1 Artist",
    mp1.abloum AS "User 1 Album",
    mp1.song AS "User 1 Song",
    mp1.vibe AS "User 1 Vibe",
    CONCAT(bu2.name, ' ', bu2.lastname) AS "User 2 Name",
    mp2.genre AS "User 2 Genre",
    mp2.artist AS "User 2 Artist",
    mp2.abloum AS "User 2 Album",
    mp2.song AS "User 2 Song",
    mp2.vibe AS "User 2 Vibe"
FROM
    Users u1, Likes_Music lm1, MusicalProfile mp1, BaseUser bu1,
    Users u2, Likes_Music lm2, MusicalProfile mp2, BaseUser bu2
WHERE
    u1.uid = 101
    AND u2.uid = 102
    AND u1.uid = lm1.uid
    AND lm1.mpid = mp1.mpid
    AND u2.uid = lm2.uid
    AND lm2.mpid = mp2.mpid
    AND u1.baseId = bu1.baseId
    AND u2.baseId = bu2.baseId
    AND mp2.song = mp1.song;

-- Calculate the average listening time for a specific song
SELECT 
    mp.song AS "Song",
    AVG(mp.listening_time) AS "Average Listening Time (seconds)"
FROM 
    MusicalProfile mp
GROUP BY
    mp.song;
