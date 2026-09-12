import Types (Z)

incrementarListaEn :: Z -> [Z] -> [Z]
incrementarListaEn _ [] = []
incrementarListaEn n (x:xs) = (x+n) : (incrementarListaEn n xs)
