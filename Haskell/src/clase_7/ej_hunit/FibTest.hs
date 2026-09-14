module FibTest where

import Test.HUnit
import Fib (fib)

runFibTest = runTestTT testsFib

testsFib = test [
    " Casobase 1 : fib 0" ~: (fib 0) ~?= 0 ,
    " Casobase 2 : fib 1" ~: (fib 1) ~?= 1 ,
    " Casorecursivo 1 : fib 2 " ~: (fib 2) ~?= 1
    ]

