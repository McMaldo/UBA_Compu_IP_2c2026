# Programación Funcional

### Etapa de 1er Parcial

- Desde: 24/08/2026
- Hasta: 23/09/2026

### Instalación de Cabal

- Descargar e instalar la versión recomendada de Cabal

```shell
  ghcup install cabal
```

- Utilizar la versión de Cabal recién instalar

```shell
  ghcup set cabal
```

### Ejecución de Proyecto con Cabal

- Verificar Librerías

```shell
  cabal update
```

- Cargar entorno interactivo con Cabal

```shell
  cabal repl
```

- Verificar Compilación

```shell
  cabal build
```

### Opciones Vanilla

- Ejecución sin Test.HUnit (utiliza los módulos declarados en ./hie.yaml)

```shell
  ghci -ilib clase_n/función.hs
```
