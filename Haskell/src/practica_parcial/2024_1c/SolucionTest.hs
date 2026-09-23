import Test.HUnit
import Solucion

runTest = runTestTT tests

tests = test [
-- Ejercicio 1
    "Ej 1 - caso 0" ~: aproboMasDeNMaterias [("Pablo", [4,6,7,10])] "Pablo" 3 ~?= True,
    "Ej 1 - caso 1" ~: aproboMasDeNMaterias [("Jorge", [4,4]),("Pablo", [4,6,7,10])] "Pablo" 3 ~?= True,

-- Ejercicio 2
    "Ej 2 - caso 0" ~: buenosAlumnos [("Jorge", [8,8]),("Pablo", [8,8,8])] ~?= ["Jorge","Pablo"],
    "Ej 2 - caso 1" ~: buenosAlumnos [("Jorge", [4,4]),("Pablo", [8,8,8])]~?= ["Pablo"],
    "Ej 2 - caso 2" ~: buenosAlumnos [("Jorge", [8,8]),("Pablo", [4,4,8])] ~?= ["Jorge"],
    "Ej 2 - caso 3" ~: buenosAlumnos [("Jorge", [8,8]),("Pablo", [10,10,10,10,10,10,3])] ~?= ["Jorge"],

-- Ejercicio 3
    "Ej 3 - caso 0" ~: mejorPromedio [("Jorge", [8,8])] ~?= "Jorge",
    "Ej 3 - caso 1" ~: mejorPromedio [("Jorge", [8,8]),("Pablo", [7,7])] ~?= "Jorge",
    "Ej 3 - caso 2" ~: mejorPromedio [("Jorge", [8,8]),("Pablo", [7,7]),("Juani", [8,8])] ~?= "Jorge",
    "Ej 3 - caso 3" ~: mejorPromedio [("Jorge", [7,7]),("Pablo", [8,8]),("Juani", [8,8])] ~?= "Pablo",

-- Ejercicio 4
    "Ej 4 - caso 0" ~: seGraduoConHonores [("Pablo", [8,8,8])] 3 "Pablo" ~?= True,
    "Ej 4 - caso 1" ~: seGraduoConHonores [("Pablo", [6,6,6])] 3 "Pablo" ~?= False,
    "Ej 4 - caso 2" ~: seGraduoConHonores [("Jorge", [7,7,7]),("Pablo", [8,8,8]),("Juani", [8,8,8])] 3 "Pablo" ~?= True,
    "Ej 4 - caso 3" ~: seGraduoConHonores [("Pablo", [10,10,10,10,3])] 5 "Pablo" ~?= False
    ]
