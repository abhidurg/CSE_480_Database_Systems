SELECT supers.name AS Super, powers.name AS Power
FROM supers LEFT OUTER JOIN powers 
ON supers.id = powers.super_id
ORDER BY supers.name, powers.name;