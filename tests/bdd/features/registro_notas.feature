Feature: Registro y consulta de notas académicas
  Como funcionario académico de la Universidad Regional del Sur
  quiero registrar y consultar las notas de los estudiantes
  para conocer su desempeño académico y evitar registros duplicados.

  Background:
    Given existe un sistema de registro de notas vacío

  @critical @smoke
  Scenario Outline: Determinar si un estudiante aprueba o reprueba una materia
    When consulto el estado académico para una nota de <nota>
    Then el sistema debe indicar que el estudiante está "<estado>"

    Examples:
      | nota | estado    |
      | 3.0  | Aprobado  |
      | 4.5  | Aprobado  |
      | 2.9  | Reprobado |

  @regression
  Scenario: Calcular promedio de un estudiante con varias notas
    Given el estudiante "Ana" tiene registrada una nota de 4.0 en "Matematicas" para el semestre "2026-1"
    And el estudiante "Ana" tiene registrada una nota de 3.0 en "Fisica" para el semestre "2026-1"
    And el estudiante "Ana" tiene registrada una nota de 5.0 en "Quimica" para el semestre "2026-1"
    When solicito el promedio del estudiante "Ana"
    Then el promedio debe ser 4.0

  @regression
  Scenario: Calcular promedio de un estudiante sin notas
    When solicito el promedio del estudiante "Ana"
    Then el promedio debe ser 0.0

  @critical
  Scenario: Evitar registrar dos notas para la misma materia en el mismo semestre
    Given el estudiante "Ana" tiene registrada una nota de 4.0 en "Matematicas" para el semestre "2026-1"
    When intento registrar otra nota de 4.5 para el estudiante "Ana" en "Matematicas" para el semestre "2026-1"
    Then el sistema debe mostrar el error "Ya existe una nota registrada para esta materia en el mismo semestre"

  @regression
  Scenario: Permitir registrar la misma materia en semestre diferente
    Given el estudiante "Ana" tiene registrada una nota de 4.0 en "Matematicas" para el semestre "2026-1"
    When intento registrar otra nota de 4.5 para el estudiante "Ana" en "Matematicas" para el semestre "2026-2"
    Then la nota debe quedar registrada correctamente

  @smoke
  Scenario: Permitir registrar materias diferentes en el mismo semestre
    Given el estudiante "Ana" tiene registrada una nota de 4.0 en "Matematicas" para el semestre "2026-1"
    When intento registrar otra nota de 4.5 para el estudiante "Ana" en "Fisica" para el semestre "2026-1"
    Then la nota debe quedar registrada correctamente