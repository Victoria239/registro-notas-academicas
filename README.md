# Registro de Notas Académicas

## Descripción del proyecto

Este proyecto implementa un módulo de registro de notas académicas para la Universidad Regional del Sur.

El sistema permite:

- Registrar notas de estudiantes por materia y semestre.
- Validar que la nota esté entre 0.0 y 5.0.
- Determinar si un estudiante aprueba o reprueba una materia.
- Calcular el promedio de notas registradas.
- Evitar que se registre dos veces una nota para la misma materia en el mismo semestre.

## Tecnología seleccionada

Para este proyecto se seleccionó Python con las siguientes herramientas:

- `uv`: para la gestión del entorno y dependencias.
- `pytest`: para la ejecución de pruebas unitarias.
- `pytest-bdd`: para implementar pruebas BDD con escenarios Gherkin.
- `pytest-cov`: para medir la cobertura de pruebas.
- GitHub Actions: para ejecutar automáticamente las pruebas en cada push.

Se eligió Python porque permite implementar de forma clara y sencilla pruebas automatizadas, aplicar TDD y conectar escenarios BDD con código funcional.

---

# Parte 1 — Análisis inicial

## 1.1 Particiones de equivalencia

Requerimiento analizado:

> La nota debe estar entre 0.0 y 5.0.

| Partición | Rango que cubre | Valor representativo | Resultado esperado |
|---|---:|---:|---|
| Nota menor al mínimo | x < 0.0 | -0.1 | Rechazar nota |
| Límite inferior válido | x = 0.0 | 0.0 | Aceptar nota |
| Nota válida baja | 0.0 < x < 3.0 | 2.5 | Aceptar nota |
| Nota válida aprobatoria | 3.0 ≤ x ≤ 5.0 | 4.0 | Aceptar nota |
| Límite superior válido | x = 5.0 | 5.0 | Aceptar nota |
| Nota mayor al máximo | x > 5.0 | 5.1 | Rechazar nota |

## 1.2 Análisis de valores límite

Para los valores límite se evalúa el valor justo antes del límite, el límite exacto y el valor justo después.

| Límite evaluado | Valor | ¿Está dentro del rango? | Resultado esperado |
|---|---:|---|---|
| Antes del mínimo | -0.1 | No | Rechazar nota |
| Mínimo exacto | 0.0 | Sí | Aceptar nota |
| Después del mínimo | 0.1 | Sí | Aceptar nota |
| Antes del máximo | 4.9 | Sí | Aceptar nota |
| Máximo exacto | 5.0 | Sí | Aceptar nota |
| Después del máximo | 5.1 | No | Rechazar nota |

## 1.3 Preguntas al Product Owner

| Pregunta | Justificación |
|---|---|
| ¿La validación de duplicidad se debe hacer por nombre exacto de la materia o por un código único de materia? | Esta respuesta impacta el diseño de las pruebas porque no es lo mismo comparar textos como “Matemáticas” y “matematicas” que comparar códigos únicos de materia. |
| ¿Un estudiante puede registrar la misma materia en semestres diferentes? | Esta respuesta permite definir si el sistema debe permitir repetir una materia en otro semestre o si debe bloquearla siempre. |
| ¿Cuál debe ser el mensaje exacto cuando se intenta registrar una nota duplicada? | El requerimiento indica que debe lanzarse un error claro, pero para probarlo correctamente se necesita conocer el mensaje esperado o el tipo de error. |

---

# Parte 2 — Diseño formal de casos de prueba

| ID | Requerimiento | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo |
|---|---|---|---|---|---|---|---|
| CP001 | Req. 1 | Registrar una nota válida dentro del rango permitido | El estudiante no tiene nota previa en la materia | Estudiante: Ana, Materia: Matemáticas, Semestre: 2026-1, Nota: 4.0 | Registrar la nota | La nota queda registrada correctamente | Positivo |
| CP002 | Req. 1 | Registrar una nota menor al mínimo permitido | Existe un estudiante en el sistema | Nota: -0.1 | Intentar registrar la nota | El sistema rechaza la nota con un error claro | Negativo |
| CP003 | Req. 1 | Registrar una nota mayor al máximo permitido | Existe un estudiante en el sistema | Nota: 5.1 | Intentar registrar la nota | El sistema rechaza la nota con un error claro | Negativo |
| CP004 | Req. 1 | Registrar una nota en el límite inferior permitido | Existe un estudiante en el sistema | Nota: 0.0 | Registrar la nota | La nota queda registrada correctamente | Borde |
| CP005 | Req. 1 | Registrar una nota en el límite superior permitido | Existe un estudiante en el sistema | Nota: 5.0 | Registrar la nota | La nota queda registrada correctamente | Borde |
| CP006 | Req. 2 | Determinar aprobación con nota igual a 3.0 | El estudiante tiene una nota registrada | Nota: 3.0 | Consultar estado académico | El sistema indica “Aprobado” | Borde |
| CP007 | Req. 2 | Determinar reprobación con nota menor a 3.0 | El estudiante tiene una nota registrada | Nota: 2.9 | Consultar estado académico | El sistema indica “Reprobado” | Borde |
| CP008 | Req. 2 | Determinar aprobación con nota mayor a 3.0 | El estudiante tiene una nota registrada | Nota: 4.2 | Consultar estado académico | El sistema indica “Aprobado” | Positivo |
| CP009 | Req. 3 | Calcular promedio con varias notas registradas | El estudiante tiene tres notas registradas | Notas: 4.0, 3.0, 5.0 | Solicitar el promedio del estudiante | El promedio calculado es 4.0 | Positivo |
| CP010 | Req. 3 | Calcular promedio con una sola nota registrada | El estudiante tiene una nota registrada | Nota: 3.5 | Solicitar el promedio del estudiante | El promedio calculado es 3.5 | Positivo |
| CP011 | Req. 3 | Calcular promedio de un estudiante sin notas | El estudiante no tiene notas registradas | Sin notas | Solicitar el promedio del estudiante | El sistema retorna 0.0 | Negativo |
| CP012 | Req. 4 | Registrar dos notas para la misma materia en el mismo semestre | Ya existe una nota de Matemáticas para Ana en 2026-1 | Nueva nota: Matemáticas, 2026-1, 4.5 | Intentar registrar la segunda nota | El sistema lanza error por nota duplicada | Negativo |
| CP013 | Req. 4 | Registrar la misma materia en semestre diferente | Ya existe Matemáticas para Ana en 2026-1 | Nueva nota: Matemáticas, 2026-2, 4.5 | Registrar la nota | El sistema permite el registro | Positivo |
| CP014 | Req. 4 | Registrar materias diferentes en el mismo semestre | Ya existe Matemáticas para Ana en 2026-1 | Nueva nota: Física, 2026-1, 4.5 | Registrar la nota | El sistema permite el registro | Positivo |

---

# Parte 3 — Evidencia de TDD

El desarrollo se realizará aplicando el ciclo TDD:

1. RED: escribir primero pruebas que fallen.
2. GREEN: implementar el código mínimo para que las pruebas pasen.
3. REFACTOR: mejorar el código sin romper las pruebas.

Cada requerimiento tendrá commits separados para evidenciar el proceso.

---

# Parte 4 — BDD

Los escenarios BDD se encuentran en:

```text
tests/bdd/features/registro_notas.feature