import Types (Z)

longitudDeLista :: [t] -> Z
longitudDeLista [] = 0
longitudDeLista (_:xs) = 1 + longitudDeLista xs