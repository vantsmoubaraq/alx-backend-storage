-- lists all bands with Glam rock as their main style
-- displays columns band_name and lifespan
SELECT band_name, COALESCE(split, 2022) - formed as lifespan FROM metal_bands
WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;