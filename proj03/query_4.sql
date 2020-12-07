SELECT Artist.Name, Track.Name FROM 
Track INNER JOIN Album
ON Track.AlbumId = Album.AlbumId
INNER JOIN Artist
ON Album.ArtistId = Artist.ArtistId
WHERE Album.Title = Artist.Name
ORDER BY Track.Name;