{-
  Implementar quitar :: (Eq t) => t -> [t] -> [t], que dados
  un elemento e y una lista s, elimina la primera aparici´on de e en la lista s
  (de haberla).
-}

-- quitarDeLista
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar e (x:xs) 
  | (e == x) = xs
  | (e /= x) = x:(quitar e xs)

-- quitarTodosDeLista
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos e (x:xs) 
  | (e == x) = (quitarTodos e xs)
  | (e /= x) = x:(quitarTodos e xs)
