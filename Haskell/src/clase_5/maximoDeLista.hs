import Types (Z)

{-
  problema máximo (s: seq⟨Z⟩) : Z {
    requiere: { |s| > 0 }
    asegura: { resultado ∈ s ∧ todo elemento de s es menor o igual a
    resultado}
  }
-}

-- V1
maximo :: [Z] -> Z
maximo [x] = x
maximo (x:y:ys)
 | x > y = maximo (x:ys)
 | x <= y = maximo (y:ys)

-- V2
maximoV2 :: [Z] -> Z
maximoV2 [x] = x
maximoV2 (x:xs)
 | x > maximoV2 xs = x
 | x <= maximoV2 xs = maximoV2 xs

-- V3 no aplicable para la materia
maximoV3 :: [Z] -> Z
maximoV3 [x] = x
maximoV3 (x:xs) = if x > maximoV3 xs then x else maximoV3 xs
