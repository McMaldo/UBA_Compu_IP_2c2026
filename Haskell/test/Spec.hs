module Main where

import Test.HUnit
import ContarPalabrasTest (contarPalabrasTest)
import FibonacciTest (fibonacciTest)

main :: IO Counts
main = do
    putStrLn "\n--- Ejecutando tests de ContarPalabras ---"
    _ <- contarPalabrasTest
    putStrLn "\n--- Ejecutando tests de Fibonacci ---"
    fibonacciTest
