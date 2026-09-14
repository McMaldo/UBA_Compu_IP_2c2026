# Reglas
Listado de funciones que pueden utilizar para el parcial de Haskell. Cualquier otra función debe ser implementada. Si utilizan una función no permitida, se anula el ejercicio.
```haskell
  mod :: Integral a => a -> a -> a
  div :: Integral a => a -> a -> a
  fst :: (a, b) -> a
  snd :: (a, b) -> b
  sqrt :: Floating a => a -> a
  (:) :: a -> [a] -> [a]
  (++) :: [a] -> [a] -> [a]
  head :: [a] -> a
  tail :: [a] -> [a]
  fromIntegral :: (Integral a, Num b) => a -> b
  fromInteger :: Num a => Integer -> a
  not :: Bool -> Bool
  -- ariméticas (+,-,*,/)
  -- potencia (**,^)
  -- lógicas (&&,||,==,/=,>,<,>=,<=)
```
### Aclaraciones
1) No está permitido el uso del condicional “if then else”.
2) El uso de where está permitido
