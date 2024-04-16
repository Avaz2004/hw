select name,duration from Track 
where duration = (select MAX(duration) from Track);

select name,duration from Track
where duration >= 00:03:30;

select name from Collection
where date between 2018 and 2020;

select name from Executor 
where name not like '% %';

select name from Track 
where name like 'my' or name like 'мой';


SELECT genre_ID, COUNT(executor_ID) as number_of_artists
FROM executorgenre 
GROUP BY genre_ID;

select COUNT(Track)
from Track
where (select name from Collection 
where date between 2019 and 2020);

SELECT name AS album_name, AVG(duration) AS avg_dur
FROM Track
JOIN Album ON Track.album_id = Album.id
GROUP BY name;

SELECT name
FROM Executor
WHERE name NOT IN (
SELECT DISTINCT name
FROM Album
WHERE date = 2020;

SELECT name FROM Collection
JOIN Track ON ID = Track.Collection_id,
JOIN Executor ON Track.executor_id = Executor.id,
WHERE name = 'Deep purple';