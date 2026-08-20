# 🧮 Calculadora en Python

## 📋 Descripción

Este proyecto consiste en una **calculadora básica desarrollada en Python**, creada como ejercicio práctico para reforzar el uso de:

- Estructuras de control.
- Condicionales.
- Bucles.
- Funciones.
- Entrada y salida de datos.
- Manejo de excepciones.
- Control de errores.
- Git y GitHub.

La calculadora permite realizar operaciones matemáticas básicas y gestionar diferentes acciones desde un menú interactivo.

---

## ⚙️ Funcionalidades

La calculadora permite realizar las siguientes operaciones:

| Opción | Operación |
|---|---|
| `1` | Sumar |
| `2` | Restar |
| `3` | Multiplicar |
| `4` | Dividir |
| `5` | Salir del programa |

### Operaciones disponibles

- **Suma:** suma dos números.
- **Resta:** resta el segundo número del primero.
- **Multiplicación:** multiplica dos números.
- **División:** divide el primer número por el segundo.
- **Salir:** finaliza la ejecución del programa.

---

## 🛡️ Manejo de errores

El programa incluye manejo de excepciones para evitar que la calculadora se cierre ante errores de entrada.

### Entrada inválida

Si el usuario introduce texto en lugar de un número, se muestra un mensaje de error:

```text
Error: debe ingresar números válidos.
```

### División por cero

La función de división controla el intento de dividir por cero:

```text
Error: No se puede dividir por cero.
```

---

## 🗂️ Estructura del proyecto

```text
calculadora_y_test/
│
├── calculadora.py
└── README.md
```

### `calculadora.py`

Contiene toda la lógica de la calculadora, incluyendo las funciones:

```python
sumar()
restar()
multiplicar()
dividir()
```

### `README.md`

Contiene la documentación y descripción del proyecto.

---

## 🚀 Requisitos

Para ejecutar este proyecto es necesario tener instalado:

- Python 3.x
- Git (para gestionar el repositorio)

No se utilizan librerías externas.

---

## ▶️ Ejecución

Desde la carpeta del proyecto ejecutar:

```bash
python calculadora.py
```

En algunos sistemas puede ser necesario utilizar:

```bash
python3 calculadora.py
```

---

## 💻 Ejemplo de uso

Al iniciar el programa se muestra:

```text
===== CALCULADORA =====
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
```

Por ejemplo, para realizar una suma:

```text
Seleccione una operación: 1

Ingrese el primer número: 20
Ingrese el segundo número: 10

Resultado: 30.0
```

Después del resultado se puede elegir:

```text
Seleccione una operación:
1..
2..
3..
4..
5. Salir
```

---

## 🔀 Git

El proyecto utiliza Git para el control de versiones.

Para inicializar el repositorio:

```bash
git init
```

Agregar los archivos:

```bash
git add .
```

Crear un commit:

```bash
git commit -m "feat: crear calculadora con operaciones basicas y sus respectivos test"
```

---

## ☁️ GitHub

El proyecto puede vincularse con un repositorio remoto de GitHub.

Agregar el repositorio remoto:

```bash
git remote add origin https://github.com/TU_USUARIO/calculadora_y_test.git
```

Establecer la rama principal:

```bash
git branch -M main
```

Subir el proyecto:

```bash
git push -u origin main
```

---

## 🎯 Objetivo del ejercicio

El objetivo principal es practicar la creación de programas estructurados en Python utilizando **funciones, condicionales, bucles y manejo de excepciones**, además de familiarizarse con el flujo básico de trabajo utilizando **Git y GitHub**.

---

## 👩‍💻 Autor

**Mónica Carena**

Proyecto realizado como ejercicio práctico de aprendizaje de Python, Git y GitHub.