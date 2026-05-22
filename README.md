# Registro de Notas Académicas

## Descripción del proyecto

Este proyecto implementa un módulo de registro de notas académicas para la Universidad Regional del Sur.

El sistema permite:

- Registrar notas de estudiantes por materia y semestre.
- Validar que la nota esté entre 0.0 y 5.0.
- Determinar si un estudiante aprueba o reprueba una materia.
- Calcular el promedio de notas registradas.
- Evitar que se registre dos veces una nota para la misma materia en el mismo semestre.

---

## Tecnología seleccionada

Para este proyecto se seleccionó Python con las siguientes herramientas:

- `uv`: para la gestión del entorno y dependencias.
- `pytest`: para la ejecución de pruebas unitarias.
- `pytest-bdd`: para implementar pruebas BDD con escenarios Gherkin.
- `pytest-cov`: para medir la cobertura de pruebas.
- GitHub Actions: para ejecutar automáticamente las pruebas en cada push.

Se eligió Python porque permite implementar de forma clara y sencilla pruebas automatizadas, aplicar TDD y conectar escenarios BDD con código funcional.

---

## Estructura del proyecto

```text
registro-notas-academicas/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── registro_notas/
│       ├── __init__.py
│       └── sistema_notas.py
├── tests/
│   ├── bdd/
│   │   ├── features/
│   │   │   └── registro_notas.feature
│   │   └── steps/
│   │       └── test_registro_notas_steps.py
│   └── test_sistema_notas.py
├── README.md
├── pyproject.toml
├── uv.lock
└── .gitignore
```

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

---

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

---

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

El desarrollo se realizó aplicando el ciclo TDD:

1. **RED:** se escribieron primero las pruebas automatizadas, antes de implementar la lógica.
2. **GREEN:** se implementó el código mínimo necesario para que las pruebas pasaran.
3. **REFACTOR:** se mejoró la estructura del código sin alterar el comportamiento ni romper las pruebas.

El historial de commits del repositorio evidencia el proceso para cada requerimiento.

## Ciclo TDD aplicado

| Requerimiento | Fase RED | Fase GREEN | Fase REFACTOR |
|---|---|---|---|
| Req. 1 — Registrar nota entre 0.0 y 5.0 | Tests de validación de rango de nota | Implementación del registro de notas válidas | Extracción de validación de rango |
| Req. 2 — Aprobar o reprobar materia | Tests para notas 3.0, 2.9 y 4.2 | Implementación de estado académico | Extracción de constantes de reglas académicas |
| Req. 3 — Calcular promedio | Tests de promedio con varias notas, una nota y sin notas | Implementación de cálculo de promedio | Separación de búsqueda de notas por estudiante |
| Req. 4 — Evitar notas duplicadas | Tests de duplicidad por materia y semestre | Implementación de validación de duplicados | Mejora de validación usando método auxiliar |

---

# Parte 4 — BDD en Gherkin

Los escenarios BDD se encuentran en:

```text
tests/bdd/features/registro_notas.feature
```

Los step definitions se encuentran en:

```text
tests/bdd/steps/test_registro_notas_steps.py
```

El archivo `.feature` incluye:

- Contexto del usuario en lenguaje de negocio.
- Uso de `Background`.
- Escenarios para aprobación y reprobación.
- Escenarios para cálculo de promedio.
- Escenarios para validación de duplicados.
- Un `Scenario Outline` con tabla de ejemplos.
- Camino de error con mensaje esperado.
- Tags `@smoke`, `@critical` y `@regression`.

---

# Parte 5 — Pipeline CI/CD

El proyecto incluye un workflow de GitHub Actions ubicado en:

```text
.github/workflows/ci.yml
```

El pipeline se ejecuta automáticamente en cada push a la rama principal y realiza las siguientes acciones:

1. Descarga el repositorio.
2. Instala Python.
3. Instala `uv`.
4. Instala las dependencias del proyecto.
5. Ejecuta pruebas unitarias y pruebas BDD.
6. Genera reporte de cobertura.
7. Falla si alguna prueba no pasa o si la cobertura baja del 80%.

Comando usado por el pipeline:

```bash
uv run pytest --cov=src --cov-report=term-missing --cov-fail-under=80
```

---

# Parte 6 — Cobertura de pruebas

La cobertura se generó con el siguiente comando:

```bash
uv run pytest --cov=src --cov-report=term-missing --cov-fail-under=85
```

Resultado obtenido:

```text
Name                                  Stmts   Miss  Cover   Missing
-------------------------------------------------------------------
src\registro_notas\__init__.py            0      0   100%
src\registro_notas\sistema_notas.py      30      0   100%
-------------------------------------------------------------------
TOTAL                                    30      0   100%
Required test coverage of 85% reached. Total coverage: 100.00%

22 passed in 0.58s
```

La cobertura total obtenida fue del **100%**, superando el mínimo solicitado del 85%.

---

# Comandos de ejecución

## Ejecutar todas las pruebas

```bash
uv run pytest
```

## Ejecutar pruebas con cobertura

```bash
uv run pytest --cov=src --cov-report=term-missing --cov-fail-under=85
```

## Ejecutar pruebas unitarias específicas

```bash
uv run pytest tests/test_sistema_notas.py -v
```

## Ejecutar pruebas BDD

```bash
uv run pytest tests/bdd/steps/test_registro_notas_steps.py -v
```

---

# Resultados de pruebas

El proyecto cuenta con:

| Tipo de prueba | Cantidad |
|---|---:|
| Pruebas unitarias | 14 |
| Pruebas BDD | 8 |
| Total de pruebas automatizadas | 22 |

Resultado final:

```text
22 passed
```

---

# Reflexión final

Diseñar los casos de prueba antes de programar permitió comprender mejor las reglas del sistema y anticipar escenarios que podían fallar. Esto ayudó a no enfocarse únicamente en los casos positivos, sino también en entradas inválidas, valores límite y condiciones especiales como el registro duplicado de una materia en el mismo semestre.

Lo más difícil de seguir el ciclo TDD fue escribir primero pruebas que fallaran, porque normalmente existe la tentación de implementar la lógica directamente. La mayor tentación de saltarme un paso apareció en los requisitos sencillos, como determinar si una nota aprueba o reprueba, pero seguir el ciclo RED, GREEN y REFACTOR ayudó a dejar evidencia clara del avance y a mejorar la calidad del código.

---

# Estado final del proyecto

El sistema cumple con los cuatro requerimientos solicitados:

| Requerimiento | Estado |
|---|---|
| Registrar nota entre 0.0 y 5.0 | Cumplido |
| Determinar aprobación o reprobación | Cumplido |
| Calcular promedio de notas | Cumplido |
| Evitar duplicados por materia y semestre | Cumplido |

Además, el repositorio incluye:

- Código de producción separado de las pruebas.
- Tests unitarios.
- Escenarios BDD en Gherkin.
- Step definitions funcionales.
- Pipeline CI/CD en GitHub Actions.
- Cobertura superior al 85%.
- README con análisis, casos de prueba, evidencia y reflexión.