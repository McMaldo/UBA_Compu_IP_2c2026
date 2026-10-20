```C++
problema generar nros al azar (in cantidad : Z, in desde : Z, in hasta : Z) : Pila[Z] {
    requiere: {cantidad ≥0}
    requiere: {desde ≤hasta}
    asegura: {El tamaño de resultado es igual a cantidad}
    asegura: {Todos los elementos de res son valores entre desde y hasta (ambos inclusive), seleccionados aleatoriamente con probabilidad uniforme.}
}
```
Para obtener numeros al azar pueden usar la funcion
`random.randint(<desde>, <hasta>)`{:.python} importando previamente el modulo random
Guía 8 - Ejercicio 1.1
Elaboremos casos de test para la solucion. ¿Que debe cumplir la pila generada? ¿Que casos de test podemos pensar?

| Caso              | Entradas    | Esperado   |
| ----------------  | ----------- | ---------- | 
| La cantidad es 0  | cantidad=0<br>desde=0<br>hasta=10  | Pila vacıa |
| La cantidad es 10 | cantidad=10<br>desde=0<br>hasta=10 | Pila con 10 elementos |
| El rango es desde 10 hasta 20 | <br>cantidad=10<br>desde=10<br>hasta=20 | Pila con elementos entre 10 y 20 |
