SELECT FirstName, State FROM Employee 
WHERE State = 'MI' OR State IS NULL 
ORDER BY FirstName;