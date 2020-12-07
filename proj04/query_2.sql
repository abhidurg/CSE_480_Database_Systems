SELECT Name FROM Genre
WHERE GenreId IN (SELECT GenreId FROM Track)
ORDER BY Name;