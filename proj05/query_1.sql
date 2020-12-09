SELECT UPPER(Artist.Name) AS UPPER_NAME, 
MAX(Track.Bytes) AS MEMORY_SIZE
FROM Artist
INNER JOIN Album ON Artist.ArtistId = Album.ArtistId
INNER JOIN Track ON Track.AlbumId = Album.AlbumId
GROUP BY Artist.Name
ORDER BY Track.Bytes DESC LIMIT 10;