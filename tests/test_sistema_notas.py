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