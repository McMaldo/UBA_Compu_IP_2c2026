import Types (Z)

sumatoriaDeLista :: [Z] -> Z
sumatoriaDeLista [] = 0
sumatoriaDeLista (x:xs) = x + sumatoriaDeLista xs