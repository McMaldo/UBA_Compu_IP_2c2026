# Introducción a Programación

## 1er Parcial - Tema 2 - Turno Noche

Resolver los siguientes ejercicios cuyas especificaciones en lenguaje semiformal figuran a continuación. Deben ser implementadas en Haskell utilizando los tipos requeridos y solamente las funciones que se ven en la materia Introducción a la Programación / Algoritmos y Estructuras de Datos I (FCEyN-UBA).

### Ejercicio 1 [2 puntos]

```Haskell
problema ejercicio1 (s: seq⟨Z⟩, n: Z) : seq⟨Z⟩ {
  requiere: {existe un índice i tal que 0 ≤ i < |s|-1 y s[i]*s[i+1] = n}
  asegura: {|res| = |s| - 2}
  asegura: {res es igual a s sin s[j] ni s[j+1], donde j es una posición válida de s tal que s[j] * s[j+1] = n}
}
```

### Ejercicio 2 [0,5 puntos]

Conteste marcando la opción correcta.

¿Qué nombre le pondrías a la función del ejercicio anterior?

- [ ] SacarTodosLosParesConsecutivosCuyoProductoEsN
- [ ] SacarAlgunParConsecutivoCuyoProductoEsN
- [ ] SacarPrimerParConsecutivoCuyoProductoEsN
- [ ] Ninguna de las opciones anteriores describe adecuadamente el problema

### Ejercicio 3 [0,5 puntos]

Conteste marcando la opción correcta, teniendo el cuenta el problema ejercicio1

Si s = [1, -3, 0, 2, -6] y n = 0 , entonces:

- [ ] res1 = [1, 2, -6] es una salida válida
- [ ] res2 = [1,-6] es una salida válida
- [ ] No es posible ejecutar la función con n = 0
- [ ] No hay problema con n = 0, pero res1 y res2 no son soluciones válidas de acuerdo a la especificación

### Ejercicio 4 [2 puntos]

Decimos que un número entero positivo no tiene dígitos repetidos si todos sus dígitos son distintos entre sí. Por ejemplo, 1234 y 5 no tienen dígitos repetidos, mientras que 1123 y 99 sí tienen dígitos repetidos.

```Haskell
problema cantidadSinDigitosRepetidos (d: Z, h: Z) : Z {
  requiere: {0 < d ≤ h}
  asegura: {res es la cantidad de números sin dígitos repetidos en el rango [d..h]}
}
```

Ejemplo:

```Shell
cantidadSinDigitosRepetidos 95 105 debe devolver 8
# (porque 99, 100 y 101 tienen dígitos repetidos; los demás no)
```

### Ejercicio 5 [2 puntos]

```Haskell
problema distanciaEntreExtremosDelMaximo (lista: seq⟨Z⟩) : Z {
  requiere: {|lista| > 0}
  asegura: {res es la distancia (en cantidad de posiciones) entre la primera y la última aparición del valor máximo de lista}
}
```

Ejemplo:

```Shell
distanciaEntreExtremosDelMaximo [3,7,7,2,7,1] debe devolver 3
# (el máximo es 7, su primera aparición es la posición 1 y su última aparición es la posición 4)
```

### Ejercicio 6 [2 puntos]

En Haskell, una matriz se puede representar utilizando una secuencia de secuencias, donde cada secuencia interna representa una fila de la matriz. Todas las filas deben tener igual longitud.

```Haskell
problema ejercicio6 (matriz: seq⟨seq⟨Z⟩⟩) : seq⟨seq⟨Z⟩⟩ {
  requiere: {|matriz| > 0}
  requiere: {para toda fila perteneciente a matriz, |fila| = |matriz|}
  asegura: {|res| = |matriz|}
  asegura: {para todo i tal que 0 ≤ i < |matriz|, |res[i]| = |matriz[i]|}
  asegura: {para todo i, j tales que 0 ≤ i < |matriz| y 0 ≤ j < |matriz|, i ≠ j: res[i][j] = matriz[i][j]}
  asegura: {para todo i tal que 0 ≤ i < |matriz|: si matriz[i][i] es par entonces res[i][i] = 0, si no res[i][i] = 1}
}
```

```Haskell
input = [
  [1,2,3,4],
  [1,2,3,4],
  [1,2,3,4],
  [1,2,3,4]
]

res = [
  [1,2,3,4],
  [1,0,3,4],
  [1,2,1,4],
  [1,2,3,0]
]
```

### Ejercicio 7 [0,5 puntos]

Conteste marcando la opción correcta.

¿Qué nombre le pondrías a la función del ejercicio anterior?

- [ ] ReemplazarDiagonalSegúnParidad
- [ ] ReemplazarDiagonalPorCeros
- [ ] ObtenerDiagonal
- [ ] Ninguna de las opciones anteriores es un buen nombre para la función

### Ejercicio 8 [0,5 puntos]

¿Cuál de las siguientes afirmaciones describe mejor el testing de caja negra?

- [ ] Consiste en diseñar pruebas a partir de la especificación del programa y observar sus resultados.
- [ ] Consiste en demostrar que el programa no tiene errores.
- [ ] Consiste en ejecutar todas las funciones (principales y auxiliares) al menos una vez.
