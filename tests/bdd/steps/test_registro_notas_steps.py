import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from registro_notas.sistema_notas import SistemaNotas


scenarios("../features/registro_notas.feature")


@pytest.fixture
def contexto():
    return {
        "sistema": None,
        "resultado": None,
        "error": None,
        "cantidad_notas_antes": 0,
    }


@given("existe un sistema de registro de notas vacío")
def sistema_vacio(contexto):
    contexto["sistema"] = SistemaNotas()
    contexto["resultado"] = None
    contexto["error"] = None
    contexto["cantidad_notas_antes"] = 0


@given(parsers.parse('el estudiante "{estudiante}" tiene registrada una nota de {nota:f} en "{materia}" para el semestre "{semestre}"'))
def registrar_nota_previa(contexto, estudiante, nota, materia, semestre):
    contexto["sistema"].registrar_nota(estudiante, materia, semestre, nota)


@when(parsers.parse("consulto el estado académico para una nota de {nota:f}"))
def consultar_estado_academico(contexto, nota):
    contexto["resultado"] = contexto["sistema"].determinar_estado(nota)


@when(parsers.parse('solicito el promedio del estudiante "{estudiante}"'))
def solicitar_promedio(contexto, estudiante):
    contexto["resultado"] = contexto["sistema"].calcular_promedio(estudiante)


@when(parsers.parse('intento registrar otra nota de {nota:f} para el estudiante "{estudiante}" en "{materia}" para el semestre "{semestre}"'))
def intentar_registrar_otra_nota(contexto, nota, estudiante, materia, semestre):
    contexto["cantidad_notas_antes"] = len(contexto["sistema"].notas)

    try:
        contexto["sistema"].registrar_nota(estudiante, materia, semestre, nota)
    except ValueError as error:
        contexto["error"] = str(error)


@then(parsers.parse('el sistema debe indicar que el estudiante está "{estado}"'))
def validar_estado_academico(contexto, estado):
    assert contexto["resultado"] == estado


@then(parsers.parse("el promedio debe ser {promedio:f}"))
def validar_promedio(contexto, promedio):
    assert contexto["resultado"] == promedio


@then(parsers.parse('el sistema debe mostrar el error "{mensaje}"'))
def validar_mensaje_error(contexto, mensaje):
    assert contexto["error"] == mensaje


@then("la nota debe quedar registrada correctamente")
def validar_registro_correcto(contexto):
    assert contexto["error"] is None
    assert len(contexto["sistema"].notas) == contexto["cantidad_notas_antes"] + 1