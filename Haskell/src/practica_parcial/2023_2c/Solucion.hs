module Solucion where

-- Ejercicio 1
-- t: 18'
porcentajeDeVotosAfirmativos :: [(String, String)] -> [Int] -> Int -> Float
porcentajeDeVotosAfirmativos [] [] _ = 0
porcentajeDeVotosAfirmativos (f:fs) (v:vs) c = division (100  * v) c + porcentajeDeVotosAfirmativos fs vs c

division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)

-- Ejercicio 2
-- t: 25'
formulasInvalidas :: [(String, String)] -> Bool
formulasInvalidas [] = False
formulasInvalidas [(p, v)] = (p == v)
formulasInvalidas ((p1, v1):(p2, v2):fs)
    | (p1 == v1 || p2 == v2 || p1 == p2 || v1 == v2 || p1 == v2 || p2 == v1) = True
    | otherwise = (formulasInvalidas ((p1,v1):fs)) || (formulasInvalidas ((p2,v2):fs))

-- Ejercicio 3
-- t: 22'
porcentajeDeVotos :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeVotos _ [] [] = 0.0
porcentajeDeVotos q fs cs = porcentajeDeVotosDesde q fs cs (votosAfirmativos cs)

porcentajeDeVotosDesde :: String -> [(String, String)] -> [Int] -> Int -> Float
porcentajeDeVotosDesde _ [] [] _ = 0.0
porcentajeDeVotosDesde q ((_,v):fs) (c:cs) m
    | (q == v) = division (100 * c) m
    | otherwise = porcentajeDeVotosDesde q fs cs m

votosAfirmativos :: [Int] -> Int
votosAfirmativos [] = 0
votosAfirmativos (v:vs) = v + votosAfirmativos vs

-- Ejercicio 4
-- t: 6'
menosVotado :: [(String, String)] -> [Int] -> String
menosVotado [] _ = ""
menosVotado [(p,_)] _ = p
menosVotado (f1:f2:fs) (v1:v2:vs)
    | (v1 < v2) = menosVotado (f1:fs) (v1:vs)
    | otherwise = menosVotado (f2:fs) (v2:vs)

-- tiempoTotal: 18' + 25' + 22' + 6' = 1h 11'
