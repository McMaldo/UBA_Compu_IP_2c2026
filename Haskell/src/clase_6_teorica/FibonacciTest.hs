module FibonacciTest where

import Test.HUnit
import Fibonacci (fibonacci)
import Types (Z)

-- test Input
testCasoBase0 :: Test
testCasoBase0 = "Fibonacci de 0 es 0" ~: 0 ~=? fibonacci 0

testCasoBase1 :: Test
testCasoBase1 = "Fibonacci de 1 es 1" ~: 1 ~=? fibonacci 1

-- test Case
testCasosRecursivos :: Test
testCasosRecursivos = TestList [
    "Fibonacci de 2 es 1"  ~: 1  ~=? fibonacci 2,
    "Fibonacci de 3 es 2"  ~: 2  ~=? fibonacci 3,
    "Fibonacci de 5 es 5"  ~: 5  ~=? fibonacci 5,
    "Fibonacci de 10 es 55" ~: 55 ~=? fibonacci 10
    ]

-- test Suite
testsFibonacci :: Test
testsFibonacci = TestList [
    testCasoBase0,
    testCasoBase1,
    testCasosRecursivos
    ]

-- ejecutar los tests
fibonacciTest :: IO Counts
fibonacciTest = runTestTT testsFibonacci
