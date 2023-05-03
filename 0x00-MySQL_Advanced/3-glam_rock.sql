-- lists all bands with Glam rock as their main style
-- displays columns band_name and lifespan
SELECT DISTINCT `band_name`, `split` - `formed` AS `lifespan`
FROM `metal_bands`
WHERE style LIKE "%Glam rock%" ORDER BY `lifespan` DESC;