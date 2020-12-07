SELECT Title, Name FROM Album INNER JOIN Artist 
ON Album.ArtistId = Artist.ArtistId
WHERE substr(Title,1,1) = 'B'
ORDER BY Title;