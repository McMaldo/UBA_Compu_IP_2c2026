module ContarPalabras where

import Types (Z)

-- | Devuelve la cantidad de palabras de @[Char]@ (una palabra se identifica por un caracter (no espacio en blanco) seguido de un espacio en blanco (" ") o ser el último caracter (no espacio en blanco) de la secuencia).
--   Casos especiales: @contarPalabras [] = 0.
--
-- >>> contarPalabras ['h','o','l','a',' ','s','o','y',' ','r','1','0']
-- 3
contarPalabras :: [Char] -> Z
contarPalabras [] = 0
contarPalabras [' '] = 0
contarPalabras [c] = 1
contarPalabras (x:y:ys)
    | x /= ' ' && y == ' ' = 1 + contarPalabras (y:ys)
    | otherwise = contarPalabras (y:ys)
