# language: es
Característica: Sistema de Registro de Notas Académicas
  Como administrador del sistema
  Quiero registrar y gestionar notas de estudiantes
  Para mantener un control académico eficiente

  Escenario: Registrar un nuevo estudiante
    Dado que tengo un sistema de notas
    Cuando registro un estudiante con id "001" y nombre "Juan Pérez"
    Entonces el estudiante debe estar registrado en el sistema

  Escenario: Registrar un estudiante duplicado
    Dado que tengo un sistema de notas
    Y he registrado un estudiante con id "001" y nombre "Juan Pérez"
    Cuando intento registrar un estudiante con id "001" y nombre "María López"
    Entonces el registro debe fallar

  Escenario: Registrar un nuevo curso
    Dado que tengo un sistema de notas
    Cuando registro un curso con id "MAT101" y nombre "Matemáticas I"
    Entonces el curso debe estar registrado en el sistema

  Escenario: Registrar una nota válida
    Dado que tengo un sistema de notas
    Y he registrado un estudiante con id "001" y nombre "Juan Pérez"
    Y he registrado un curso con id "MAT101" y nombre "Matemáticas I"
    Cuando registro una nota de 8.5 para el estudiante "001" en el curso "MAT101"
    Entonces la nota debe estar registrada correctamente

  Escenario: Calcular promedio de notas
    Dado que tengo un sistema de notas
    Y he registrado un estudiante con id "001" y nombre "Juan Pérez"
    Y he registrado los siguientes cursos:
      | id    | nombre         |
      | MAT101| Matemáticas I  |
      | FIS101| Física I       |
      | QUI101| Química I      |
    Y he registrado las siguientes notas para el estudiante "001":
      | curso | nota |
      | MAT101| 8.0  |
      | FIS101| 7.0  |
      | QUI101| 9.0  |
    Cuando calculo el promedio del estudiante "001"
    Entonces el promedio debe ser 8.0

  Escenario: Registrar nota fuera de rango
    Dado que tengo un sistema de notas
    Y he registrado un estudiante con id "001" y nombre "Juan Pérez"
    Y he registrado un curso con id "MAT101" y nombre "Matemáticas I"
    Cuando intento registrar una nota de 11.0 para el estudiante "001" en el curso "MAT101"
    Entonces el registro debe fallar
