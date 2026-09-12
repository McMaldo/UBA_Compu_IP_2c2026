import Types (Z)

-- pertenece
f1 :: (Eq t) => t -> [t] -> Bool
f1 _ [] = False
f1 e (x:xs)
  | (e == x) = True
  | (e /= x) = f1 e xs

-- incrementarListaEn
f2 :: Z -> [Z] -> [Z]
f2 _ [] = []
f2 n (x:xs) = [(x+n)] ++ (f2 n xs)
-- f2 n (x:xs) = (x+n) : (f2 n xs)
