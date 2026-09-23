# Introducción a la Programación

## Primer Parcial - Turno Mañana - Tema 2

Fuente: https://github.com/larriera/uba-intprogramacion/blob/main/1er-parcial/1parcial-2c2024.hs

---

1. mediaMovilN [2 puntos]

```Haskell
problema mediaMovilN (lista: seq⟨Z⟩, n: Z) : Float {
  requiere: {|lista| > 0}
  requiere: {n > 0 ∧ n ≤ |lista|}
  asegura: {res es el promedio de los últimos n elementos de lista}
}
```

2. esAtractivo [2 puntos]

```Haskell
problema esAtractivo (n: Z) : Bool {
  requiere: {n > 0}
  asegura: {res = true <=> la cantidad de factores primos de n (distintos o no) es también un número primo.}
}
-- Aclaración: los factores primos de 30 son [5,3,2]. Los factores primos de 9 son [3,3].
```

3. palabraOrdenada [2 puntos]

```Haskell
problema palabraOrdenada (palabra: seq⟨Char⟩) : Bool {
  requiere: {True}
  asegura: {res = true <=> cada uno de los elementos no blancos de palabra es mayor o igual al anterior caracter no blanco, si existe alguno.}
}
-- Aclaración: 'a' < 'b' es True.
```

4. similAnagrama [3 puntos]

```Haskell
roblema similAnagrama (palabra1: seq⟨Char⟩, palabra2: seq⟨Char⟩) : Bool⟩{
  requiere: {True}
  asegura: {res = true <=> (para todo caracter no blanco, la cantidad de apariciones de ese caracter en palabra1 es igual a la cantidad de apariciones en palabra2, y además existe al menos un caracter en palabra1 que tiene una posición distinta en palabra2)}
}
```

5. Multiple Choice [1 punto]

¿Cuándo se dice que una especificación está sub-especificada?:

- [ ] Cuando se da una precondición más restrictiva de lo realmente necesario, o bien una postcondición más débil de la que se necesita.
- [ ] Cuando se da una precondición más débil de lo realmente necesario, o bien una postcondición más restrictiva de la que se necesita.
- [ ] Cuando no hay precondiciones (o la precondición es True)
