pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs)
  | (e == x) = True
  | (e /= x) = pertenece e xs
