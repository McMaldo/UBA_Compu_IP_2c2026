module SolucionT2 where

-- Ejercicio 1
-- t = (18:15 - 18:24)

ejercicio1 :: [Integer] -> Integer -> [Integer]
ejercicio1 [] _ = []
ejercicio1 [x] _ = [x]
ejercicio1 (x:y:ys) n
    | (x * y == n) = ys
    | otherwise = x : ejercicio1 (y:ys) n

-- Ejercicio 4
-- t = (18:35 - 18:40) + (19:53 - 20:35)

cantidadSinDigitosRepetidos :: Integer -> Integer -> Integer
cantidadSinDigitosRepetidos d h
    | d == h && tieneDigitosRepetidos (intToIntList h) = 0
    | d == h = 1
    | tieneDigitosRepetidos (intToIntList d) = cantidadSinDigitosRepetidos (d+1) h
    | otherwise = 1 + cantidadSinDigitosRepetidos (d+1) h

-- Funcion para Testing
sinDigitosRepetidos :: Integer -> Integer -> [Integer]
sinDigitosRepetidos d h
    | d == h && tieneDigitosRepetidos (intToIntList h) = []
    | d == h = [d]
    | tieneDigitosRepetidos (intToIntList d) = sinDigitosRepetidos (d+1) h
    | otherwise = d : sinDigitosRepetidos (d+1) h
-- Funcion para Testing

tieneDigitosRepetidos :: [Integer] -> Bool
tieneDigitosRepetidos [] = False
tieneDigitosRepetidos [n] = False
tieneDigitosRepetidos (n:ns)
    | pertenece n ns = True
    | otherwise = tieneDigitosRepetidos ns

intToIntList :: Integer -> [Integer]
intToIntList 0  = []
intToIntList n = (mod n 10) : intToIntList (div n 10)

-- Ejercicio 5
-- t = (18:43 - 19:16)

distanciaEntreExtremosDelMaximo :: [Integer] -> Integer
distanciaEntreExtremosDelMaximo [] = 0
distanciaEntreExtremosDelMaximo ns = (ultimoMaximoPosicion ns (maximoDeLista ns)) - (primerMaximoPosicion ns (maximoDeLista ns))

maximoDeLista :: [Integer] -> Integer
maximoDeLista [x] = x
maximoDeLista (x:y:ys)
    | x > y = maximoDeLista (x:ys)
    | otherwise = maximoDeLista (y:ys)

primerMaximoPosicion :: [Integer] -> Integer -> Integer
primerMaximoPosicion [n] _ = 0
primerMaximoPosicion (n:ns) maximo
    | n == maximo = 0
    | otherwise = 1 + primerMaximoPosicion (ns) maximo

ultimoMaximoPosicion :: [Integer] -> Integer -> Integer
ultimoMaximoPosicion [n] _ = 0
ultimoMaximoPosicion (n:ns) maximo
    | n == maximo && esUltimoMaximo (n:ns) = 0
    | otherwise = 1 + ultimoMaximoPosicion (ns) maximo

esUltimoMaximo :: [Integer] -> Bool
esUltimoMaximo (n:ns) = not (pertenece n ns)

pertenece :: Integer -> [Integer] -> Bool
pertenece _ [] = False
pertenece n (x:xs)
    | n == x = True
    | otherwise = pertenece n xs


-- Ejercicio 6
-- t = (19:16 - 19:46)

ejercicio6 :: [[Integer]] -> [[Integer]]
ejercicio6 [] = []
ejercicio6 matriz = paresDeMatriz matriz 0

paresDeMatriz :: [[Integer]] -> Integer -> [[Integer]]
paresDeMatriz [] _ = []
paresDeMatriz (fila:matriz) j = (paresDeFila fila 0 j) : (paresDeMatriz matriz (j+1))

paresDeFila :: [Integer] -> Integer -> Integer -> [Integer]
paresDeFila [] _ _ = []
paresDeFila (n:fila) i j
    | (i == j) = (mod n 2) : paresDeFila fila (i+1) j
    | otherwise = n : paresDeFila fila (i+1) j
