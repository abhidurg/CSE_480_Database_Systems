SELECT Genre.Name AS Genre_Name, 
SUM(InvoiceLine.Quantity) AS Number_Purchased
FROM
Track INNER JOIN InvoiceLine
ON Track.TrackId = InvoiceLine.TrackId
INNER JOIN Genre
ON Track.GenreId = Genre.GenreId
WHERE Track.UnitPrice < 1
GROUP BY Genre.Name
HAVING Number_Purchased >= 10;
