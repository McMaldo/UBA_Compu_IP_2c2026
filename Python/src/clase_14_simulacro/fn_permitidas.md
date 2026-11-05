# Lista de funciones permitidas:

+ conversión de tipos: (int, list, float, str, tuple, bool)
+ estructuras: (if-else-elif, while, for) // Pueden usar for in range(..) o for in secuencia
+ Rango: range(i,f,p) // Pueden usar los 3 parámetros, 2 o 1.
+ ariméticas (+, -, *, /, //, sqrt, round, floor, ceil, %)
+ lógicas (and, or, not, ==, !=, >, <, >=, <=)
+ estructuras: (if-else-elif, while, for)

### Sobre secuencias:
+ pertenece: in
+ concatenacion: +
+ repeticion: *
+ longitud: len()
+ acceso a elementos: s[elem] // No está permitido s[i:f], s[-i] o similar!
+ Listas: append(e), insert(p, e), remove(e), index(e), count(e), clear(), pop(), pop(n), copy()
+ Diccionarios: items(), keys(), values(), pop(clave), clear()
+ TAD Pilas: from queue import LifoQueue
+ pila = LifoQueue(); put(e); get(); empty()
+ TAD Colas: from queue import Queue
+ cola = Queue(); put(e); get(); empty()
+ Archivos: open, read, readline, readlines, write, writelines, close, os.path.join(), os.path.exists()

Recordar que todas las variables deben ir anotadas con su tipo correspondiente.
