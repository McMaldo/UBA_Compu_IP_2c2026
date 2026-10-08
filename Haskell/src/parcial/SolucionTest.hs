import Test.HUnit
import SolucionT2

runTest = runTestTT tests

tests = test [
    -- Ejercicio 1
    "Ej 1 - caso 0" ~: ejercicio1 [1,2,3,4,5,6,7,8] 2 ~?= [3,4,5,6,7,8],
    "Ej 1 - caso 1" ~: ejercicio1 [1,2,3,4,5,6,7,8] 6 ~?= [1,4,5,6,7,8],
    "Ej 1 - caso 2" ~: ejercicio1 [1,2,3,4,5,6,7,8] 12 ~?= [1,2,5,6,7,8],

    -- Ejercicio 3
    "Ej 1 - caso 3" ~: ejercicio1 [1,-3,0,2,-6] 0 ~?= [1,2,-6],

    -- Ejercicio 4
    "Ej 4 - caso 0" ~: cantidadSinDigitosRepetidos 95 105 ~?= 8,
    "Ej 4 - caso 0" ~: cantidadSinDigitosRepetidos 95 95 ~?= 1,

    -- Ejercicio 5
    "Ej 5 - caso 0" ~: distanciaEntreExtremosDelMaximo [3,7,7,2,7,1] ~?= 3,
    "Ej 5 - caso 1" ~: distanciaEntreExtremosDelMaximo [7,7,7,2,7,1] ~?= 4,
    "Ej 5 - caso 2" ~: distanciaEntreExtremosDelMaximo [1,1,1,1,1,1] ~?= 5,
    "Ej 5 - caso 3" ~: distanciaEntreExtremosDelMaximo [1] ~?= 0,
    "Ej 5 - caso 4" ~: distanciaEntreExtremosDelMaximo [1,1] ~?= 1,

    "Ej 5 - aux 0" ~: primerMaximoPosicion [3,7,7,2,7,1] 7 ~?= 1,
    "Ej 5 - aux 1" ~: ultimoMaximoPosicion [3,7,7,2,7,1] 7 ~?= 4,

    -- Ejercicio 6
    "Ej 6 - caso 0" ~: ejercicio6 [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]] ~?= [[1,2,3,4],[1,0,3,4],[1,2,1,4],[1,2,3,0]],
    "Ej 6 - caso 1" ~: ejercicio6 [[1,1,1],[1,1,1],[1,1,1]] ~?= [[1,1,1],[1,1,1],[1,1,1]],
    "Ej 6 - caso 2" ~: ejercicio6 [[0,0,0],[0,0,0],[0,0,0]] ~?= [[0,0,0],[0,0,0],[0,0,0]]
    ]
