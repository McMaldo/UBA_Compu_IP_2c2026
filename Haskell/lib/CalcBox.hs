module CalcBox where

import Types (B, Z)

esPar :: Z -> B
esPar n = mod n 2 == 0

esDiv :: Z -> Z -> B
esDiv n d = mod n d == 0
