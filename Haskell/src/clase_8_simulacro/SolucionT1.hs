module SolucionT1 where

type Z = Integer
type B = Bool
type S = String

-- Ejercicio 1
{-
    Cronometro
    inicio: 19:24
    final: 20:03
    total: 39'
-}
f1 :: Z -> Z -> Z
f1 0 0 = 0
f1 d h
    | (d == h) && (esAbundate h) = 1
    | (d == h) && not (esAbundate h) = 0
    | (esAbundate d) = 1 + f1 (d+1) h
    | otherwise = f1 (d+1) h

esAbundate :: Z -> B
esAbundate n = (sumaDivisores n) > n

sumaDivisores :: Z -> Z
sumaDivisores n = sumaDivisoresDesde n 1

sumaDivisoresDesde :: Z -> Z -> Z
sumaDivisoresDesde n i
    | n == i = 0
    | esDiv n i = i + sumaDivisoresDesde n (i+1)
    | otherwise = sumaDivisoresDesde n (i+1)

esDiv :: Z -> Z -> B
esDiv n d = (mod n d == 0)

-- Ejercicio 2
{-
    Cronometro
    inicio: 20:06
    final: 20:50
    total: 44'

    input [{
        nombre_materia: S;
        año_aprobación: Z;
        cuatri_aprobación: 0 | 1 | 2;
    }]
    output [nombre_materia]
-}
f2 :: [(S, Z, Z)] -> [S]
f2 [] = []
f2 ((n,a,c):list)
    | (estaVencida a c) && not (pertenece n list) =  n : f2 list
    | otherwise = f2 list

pertenece :: S -> [(S, Z, Z)] -> Bool
pertenece _ [] = False
pertenece m ((m2,_,_):ys)
    | (m == m2) = True
    | otherwise = pertenece m ys

estaVencida :: Z -> Z -> B
estaVencida a c = (a < 2021) || (a == 2021) && (c < 2)

-- Ejercicio 3
{-
    Cronometro
    inicio: 20:55
    final: 21:12
    total: 17'
-}
f3 :: [Z] -> Z -> [Z]
f3 [] _ = []
f3 (n:ns) u
    | (esPositivo n) && (n > u) = u : (f3 ns u)
    | (esPositivo n) = n : (f3 ns u)
    | otherwise = []

esPositivo :: Z -> B
esPositivo n = (n >= 0)

-- Ejercicio 4
{-
    Cronometro
    inicio: 21:21
    final: fuera de horario
    total: 45'
-}
f4 :: [[Z]] -> Z -> Z
f4 [] _ = 0
f4 matriz col = paresDeColumna matriz 1 col

paresDeColumna :: [[Z]] -> Z -> Z -> Z
paresDeColumna [] _ _ = 0
paresDeColumna ((n:row):matriz) colAct col
    | (colAct == col) && (esPar n) = 1 + paresDeColumna matriz 1 col
    | (colAct == col) = paresDeColumna matriz 1 col
    | otherwise = paresDeColumna (row:matriz) (colAct+1) col

esPar :: Z -> B
esPar n = mod n 2 == 0

-- tiempoTotal: 39'+44'+17'+45' = 2h 25'
