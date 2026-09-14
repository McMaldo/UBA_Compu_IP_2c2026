-- Ejercicio 8
import Types (Z)

multiplicarFilas :: [[Z]] -> [Z]
multiplicarFilas [[]] = [0]
multiplicarFilas [f] = [multiplicarLista f]
multiplicarFilas (f:fs) = (multiplicarLista f):(multiplicarFilas fs)

multiplicarLista :: [Z] -> Z
multiplicarLista [] = 0
multiplicarLista [n] = n
multiplicarLista (n:ns) = n * multiplicarLista ns