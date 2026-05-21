# Sistema de Registro de Notas Académicas

Sistema para gestionar el registro y cálculo de notas académicas de estudiantes.

## Características

- Registro de estudiantes
- Registro de cursos
- Asignación de notas (0.0 - 10.0)
- Cálculo de promedios
- Consulta de notas y promedios

## Estructura del Proyecto

```
registro-notas-academicas/
├── src/
│   └── registro_notas/
│       ├── __init__.py
│       └── sistema_notas.py
├── tests/
│   ├── test_sistema_notas.py
│   └── bdd/
│       ├── features/
│       │   └── registro_notas.feature
│       └── steps/
│           └── test_registro_notas_steps.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── README.md
├── pyproject.toml
└── .gitignore
```

## Instalación

```bash
pip install -e .
```

## Ejecutar Tests

### Tests Unitarios
```bash
pytest tests/test_sistema_notas.py -v
```

### Tests BDD
```bash
behave tests/bdd/features/registro_notas.feature
```

### Todos los tests con cobertura
```bash
pytest tests/test_sistema_notas.py -v --cov=src/registro_notas --cov-report=term-missing
```

## Uso

```python
from registro_notas import SistemaNotas

# Crear instancia del sistema
sistema = SistemaNotas()

# Registrar estudiantes
sistema.registrar_estudiante("001", "Juan Pérez")
sistema.registrar_estudiante("002", "María López")

# Registrar cursos
sistema.registrar_curso("MAT101", "Matemáticas I")
sistema.registrar_curso("FIS101", "Física I")

# Registrar notas
sistema.registrar_nota("001", "MAT101", 8.5)
sistema.registrar_nota("001", "FIS101", 7.5)

# Calcular promedio
promedio = sistema.calcular_promedio("001")
print(f"Promedio: {promedio}")
```

## CI/CD

El proyecto utiliza GitHub Actions para ejecutar tests automáticamente en cada push y pull request.
