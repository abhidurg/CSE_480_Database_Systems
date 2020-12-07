SELECT Artist.Name,SUM(Milliseconds)*0.001 AS TotalTime FROM Track
INNER JOIN Album ON Track.AlbumId = Album.AlbumId
INNER Join Artist ON Album.ArtistId = Artist.ArtistID
WHERE Artist.Name LIKE 'B%'
AND
MIlliseconds > 120000
GROUP BY Artist.Name
ORDER BY TotalTime;