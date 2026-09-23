module Solucion where

-- Ejercicio 1
-- t: 14' 16"
aproboMasDeNMaterias :: [(String, [Int])] -> String -> Int -> Bool
aproboMasDeNMaterias [] _ _ = False
aproboMasDeNMaterias ((name, notes):reg) alumno n
    | (name == alumno) = (cantidadMateriasAprobadas notes) > n
    | otherwise = aproboMasDeNMaterias reg alumno n

cantidadMateriasAprobadas :: [Int] -> Int
cantidadMateriasAprobadas [] = 0
cantidadMateriasAprobadas (n:ns)
    | (n >= 4) = 1 + cantidadMateriasAprobadas ns
    | otherwise = cantidadMateriasAprobadas ns

-- Ejercicio 2
-- t: 19' 19"
buenosAlumnos:: [(String, [Int])] -> [String]
buenosAlumnos [] = []
buenosAlumnos ((name, notes):reg)
    | (promedio notes) >= 8 && not (tieneAplazos notes) = name : buenosAlumnos reg
    | otherwise = buenosAlumnos reg

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (n:ns) = n + sumatoria ns

largo :: [Int] -> Int
largo [] = 0
largo (n:ns) = 1 + largo ns

promedio :: [Int] -> Float
promedio [] = 0
promedio ns = fromIntegral (sumatoria ns) / fromIntegral (largo ns)

tieneAplazos :: [Int] -> Bool
tieneAplazos [] = False
tieneAplazos (n:ns)
    | n < 4 = True
    | otherwise = tieneAplazos ns

-- Ejercicio 3
-- t: 10' 24"
mejorPromedio:: [(String, [Int])] -> String
mejorPromedio [] = ""
mejorPromedio [(name,_)] = name
mejorPromedio ((name1,notes1):(name2,notes2):reg)
    | (promedio notes1) >= (promedio notes2) = mejorPromedio ((name1,notes1):reg)
    | otherwise = mejorPromedio ((name2,notes2):reg)

-- Ejercicio 4
-- t: 10' 30"
seGraduoConHonores :: [(String, [Int])] -> Int -> String -> Bool
seGraduoConHonores [] _ _ = True
seGraduoConHonores ((name, notes):reg) materias alumno
    | name == alumno = (aproboMasDeNMaterias [(name, notes)] alumno (materias-1)) && ((buenosAlumnos [(name, notes)]) == [alumno])
    | otherwise = seGraduoConHonores reg materias alumno

-- tiempoTotal: 14'16" + 19'19" + 10'24" + 10'30" = 54 min 29 seg
