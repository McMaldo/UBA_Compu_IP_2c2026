import Test.HUnit
import Solucion

runTest = runTestTT tests

tests = test [
    -- Ejercicio 1
    "Ej 1 - caso 0" ~: porcentajeDeVotosAfirmativos [("Juan Pérez","Susana García"), ("María Montero","Pablo Moreno")] [34, 56] 90 ~?= 100,
    "Ej 1 - caso 1" ~: porcentajeDeVotosAfirmativos [("Juan Pérez","Susana García"), ("María Montero","Pablo Moreno")] [34, 56] 180 ~?= 50,

    -- Ejercicio 2
    "Ej 2 - caso 0" ~: formulasInvalidas [("JP","SG"), ("MM","PM")] ~?= False,
    "Ej 2 - caso 1" ~: formulasInvalidas [("JP","SG"), ("MM","MM")] ~?= True,
    "Ej 2 - caso 2" ~: formulasInvalidas [("MM","SG"), ("PM","AR"), ("SG","JP")] ~?= True,
    "Ej 2 - caso 3" ~: formulasInvalidas [("SG","MM"), ("PM","AR"), ("SG","JP")] ~?= True,
    "Ej 2 - caso 4" ~: formulasInvalidas [("SG","MM"), ("PM","AR"), ("JP","JP")] ~?= True,

    -- Ejercicio 3
    "Ej 3 - caso 0" ~: porcentajeDeVotos "SG" [("MM","SG"), ("PM","AR"), ("AA","JP")] [3,2,1] ~?= 50,

    -- Ejercicio 4
    "Ej 4 - caso 0" ~: menosVotado [("MM","SG"), ("PM","AR"), ("SG","JP")] [1,2,3] ~?= "MM"
    ]
