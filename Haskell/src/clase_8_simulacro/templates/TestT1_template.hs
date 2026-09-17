import Test.HUnit
import SolucionT1

runTest = runTestTT tests

tests = test [
    -- Ejercicio 1
    "Rango que incluye varios abundantes" ~: f1 12 24 ~?= 4,
    "12 es abundante" ~: esAbundate 12 ~?= True,
    "sumaDivisores de 12 es 16" ~: sumaDivisores 12 ~?= 16,

    -- Ejercicio 2
    "Ej 2 - caso 0" ~: f2 [("AED I", 2020, 2), ("AED II", 2022, 1)] ~?= ["AED I"],
    "Ej 2 - caso 1" ~: f2 [("AED I", 2020, 2)] ~?= ["AED I"],
    "Ej 2 - caso 2" ~: f2 [("AED II", 2022, 1)] ~?= [],
    "Ej 2 - caso 3" ~: f2 [("IP", 2021, 1),("Alg", 2020, 1)] ~?= ["Alg"],

    -- Ejercicio 3
    "Ej 3 - caso 0" ~: f3 [3,8,5,0,7,-2,4] 5 ~?= [3,5,5,0,5],
    "Ej 3 - caso 1" ~: f3 [3,8,5,0,7,7,1,3,-2,4] 5 ~?= [3,5,5,0,5,5,1,3],

    -- Ejercicio 4
    "Ej 4 - caso 0" ~: f4 [[-9,8,2,3],[2,7,-5,3],[-1,0,5,6]] 2 ~?= 2
    ]