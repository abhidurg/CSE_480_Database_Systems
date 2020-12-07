SELECT DISTINCT UnitPrice, count() FROM Track
GROUP BY UnitPrice;