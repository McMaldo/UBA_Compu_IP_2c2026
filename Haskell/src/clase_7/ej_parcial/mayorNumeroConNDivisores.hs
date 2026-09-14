import Types (Z, B)

-- mayorNumeroConNDivisores :: Z -> Z -> Z -> Z
-- mayorNumeroConNDivisores d h n
--     | cantDivs d == n 

cantDivs :: Z -> Z
cantDivs m = cantDivsDesde m 1

cantDivsDesde :: Z -> Z -> Z
cantDivsDesde m d
    | m == d = 1
    | esDiv m d = 1 + cantDivsDesde m (d+1)
    | otherwise = cantDivsDesde m (d+1)

esDiv :: Z -> Z -> B
esDiv m d = div m d == 0