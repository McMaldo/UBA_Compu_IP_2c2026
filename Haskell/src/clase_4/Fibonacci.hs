module Fibonacci where

import Types (Z)

fibonacci :: Z -> Z
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n - 1) + fibonacci (n - 2)
