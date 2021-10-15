
SELECT
   	a.id,
	a.name,
	a.address,
	a.location_id,
    l.name location_name,
    l.address location_address
FROM Employee a
JOIN Location l
    ON l.id = a.location_id
