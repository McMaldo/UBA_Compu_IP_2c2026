import Types (Z)

{-
  problema ordenar (s: seq⟨Z⟩) : seq⟨Z⟩ {
    requiere: { True }
    asegura: { resultado contiene los elementos de s ordenados de
    forma creciente}
  }
-}

ordenar :: [Z] -> [Z]
ordenar [x] = [x]
ordenar (x:xs) = (ordenar (quitar x xs)) ++ [maximo xs]
-- in development ...

maximo :: [Z] -> Z
maximo [x] = x
maximo (x:y:ys)
 | x > y = maximo (x:ys)
 | x <= y = maximo (y:ys)

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar e (x:xs)
  | (e == x) = xs
  | (e /= x) = x:(quitar e xs)
