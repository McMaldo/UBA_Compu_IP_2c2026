module ContarPalabrasTest where

import Test.HUnit
import ContarPalabras (contarPalabras)
import Types (Z)

-- ejecutar los tests
runContarPalabrasTest = runTestTT testSuite

-- test Input
testCasoBase0 :: Test
testCasoBase0 = "ContarPalabras de [] es 0" ~: 0 ~=? contarPalabras []
testCasoBase1 :: Test
testCasoBase1 = "ContarPalabras de [' '] es 0" ~: 0 ~=? contarPalabras [' ']
testCasoBase2 :: Test
testCasoBase2 = "ContarPalabras de [c] es 1" ~: 1 ~=? contarPalabras ['a']

-- test Case
testCasosRecursivos :: Test
testCasosRecursivos = TestList [
    "ContarPalabras de ['s','o','y','r','1','0'] es 1"  ~: 1  ~=? contarPalabras ['s','o','y','r','1','0'],
    "ContarPalabras de ['s','o','y',' ','r','1','0'] es 2"  ~: 2  ~=? contarPalabras ['s','o','y',' ','r','1','0'],
    "ContarPalabras de ['s','o','y',' ','r','1','0',' '] es 2"  ~: 2  ~=? contarPalabras ['s','o','y',' ','r','1','0',' '],
    "ContarPalabras de [' ','s','o','y',' ','r','1','0',' '] es 2"  ~: 2  ~=? contarPalabras [' ','s','o','y',' ','r','1','0',' ']
    ]

-- test Suite
testSuite :: Test
testSuite = TestList [
    testCasoBase0,
    testCasoBase1,
    testCasoBase2,
    testCasosRecursivos
    ]
