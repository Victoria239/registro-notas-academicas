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