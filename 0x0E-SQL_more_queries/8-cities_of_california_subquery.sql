-- list all the cities of Calfironia
SELECT id, name
FROM states
WHERE state_id = (
      SELECT id
      FROM states
      WHERE name = "California"
)
