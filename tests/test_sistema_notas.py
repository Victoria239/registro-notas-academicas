import pytest
from registro_notas.sistema_notas import SistemaNotas


def test_debe_registrar_nota_valida():
    sistema = SistemaNotas()

    sistema.registrar_nota("Ana", "Matemáticas", "2026-1", 4.0)

    assert len(sistema.notas) == 1


def test_debe_rechazar_nota_menor_a_cero():
    sistema = SistemaNotas()

    with pytest.raises(ValueError, match="La nota debe estar entre 0.0 y 5.0"):
        sistema.registrar_nota("Ana", "Matemáticas", "2026-1", -0.1)


def test_debe_rechazar_nota_mayor_a_cinco():
    sistema = SistemaNotas()

    with pytest.raises(ValueError, match="La nota debe estar entre 0.0 y 5.0"):
        sistema.registrar_nota("Ana", "Matemáticas", "2026-1", 5.1)


def test_debe_aceptar_nota_cero():
    sistema = SistemaNotas()

    sistema.registrar_nota("Ana", "Matemáticas", "2026-1", 0.0)

    assert len(sistema.notas) == 1


def test_debe_aceptar_nota_cinco():
    sistema = SistemaNotas()

    sistema.registrar_nota("Ana", "Matemáticas", "2026-1", 5.0)

    assert len(sistema.notas) == 1


def test_debe_aprobar_con_nota_tres():
    sistema = SistemaNotas()

    resultado = sistema.determinar_estado(3.0)

    assert resultado == "Aprobado"


def test_debe_reprobar_con_nota_menor_a_tres():
    sistema = SistemaNotas()

    resultado = sistema.determinar_estado(2.9)

    assert resultado == "Reprobado"


def test_debe_aprobar_con_nota_mayor_a_tres():
    sistema = SistemaNotas()

    resultado = sistema.determinar_estado(4.2)

    assert resultado == "Aprobado"


def test_debe_calcular_promedio_con_varias_notas():
    sistema = SistemaNotas()
    sistema.registrar_nota("Ana", "Matematicas", "2026-1", 4.0)
    sistema.registrar_nota("Ana", "Fisica", "2026-1", 3.0)
    sistema.registrar_nota("Ana", "Quimica", "2026-1", 5.0)

    promedio = sistema.calcular_promedio("Ana")

    assert promedio == 4.0


def test_debe_calcular_promedio_con_una_sola_nota():
    sistema = SistemaNotas()
    sistema.registrar_nota("Ana", "Matematicas", "2026-1", 3.5)

    promedio = sistema.calcular_promedio("Ana")

    assert promedio == 3.5


def test_debe_retornar_cero_si_estudiante_no_tiene_notas():
    sistema = SistemaNotas()

    promedio = sistema.calcular_promedio("Ana")

    assert promedio == 0.0