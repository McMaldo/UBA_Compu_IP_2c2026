import CalcBox (esDiv)
import Types (Z, ZxZ)

-- | Devuelve el menor divisor de @n@ mayor que 1 (su menor factor primo).
--   Casos especiales: @menorDivisorDe 0 = 0@, @menorDivisorDe 1 = 1@.
--
-- >>> menorDivisorDe 15
-- 3
menorDivisorDe :: Z -> Z
menorDivisorDe 0 = 0
menorDivisorDe 1 = 1
menorDivisorDe n = menorDivisorDesde (n, 2)
  where
    menorDivisorDesde :: ZxZ -> Z
    menorDivisorDesde (n, d)
      | esDiv n d = d
      | otherwise = menorDivisorDesde (n, (d + 1))
