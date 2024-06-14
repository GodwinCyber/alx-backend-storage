-- lists all bands with Glam rock as their main style, ranked by their longevity
-- If the band is not split, use 2022 as the current year
SELECT band_name, IFNULL(split, '2022') - IFNULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;