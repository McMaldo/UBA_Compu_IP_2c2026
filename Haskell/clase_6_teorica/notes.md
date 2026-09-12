Date: 10 / 09 /2026

# Testing en Haskell

- librería utilizada: HUnit
- ejemplo de uso:

```shell
  cabal repl
  ghci> :l clase_6_teorica/FibonacciTest.hs
  ghci> fibonacciTest
  Cases: 6  Tried: 6  Errors: 0  Failures: 0
```

```shell
  cabal repl
  ghci> :l clase_6_teorica/ContarPalabrasTest.hs
  ghci> contarPalabrasTest
  Cases: 7  Tried: 7  Errors: 0  Failures: 0
```

- Carga todos los Tests registrados

```shell
  cabal repl test:unit-tests
  ghci> contarPalabrasTest
  Cases: 7  Tried: 7  Errors: 0  Failures: 0
```

- Ejecuta todos los Tests en Spec.hs

```shell
  cabal test
```
