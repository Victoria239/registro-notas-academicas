NOTA_MINIMA = 0.0
NOTA_MAXIMA = 5.0
NOTA_MINIMA_APROBACION = 3.0


class SistemaNotas:
    def __init__(self):
        self.notas = []

    def registrar_nota(self, estudiante, materia, semestre, nota):
        self._validar_rango_nota(nota)
        self._validar_nota_duplicada(estudiante, materia, semestre)

        self.notas.append({
            "estudiante": estudiante,
            "materia": materia,
            "semestre": semestre,
            "nota": nota
        })

    def determinar_estado(self, nota):
        self._validar_rango_nota(nota)

        if nota >= NOTA_MINIMA_APROBACION:
            return "Aprobado"

        return "Reprobado"

    def calcular_promedio(self, estudiante):
        notas_estudiante = self._obtener_notas_estudiante(estudiante)

        if not notas_estudiante:
            return 0.0

        return sum(notas_estudiante) / len(notas_estudiante)

    def _obtener_notas_estudiante(self, estudiante):
        return [
            registro["nota"]
            for registro in self.notas
            if registro["estudiante"] == estudiante
        ]

    def _validar_rango_nota(self, nota):
        if nota < NOTA_MINIMA or nota > NOTA_MAXIMA:
            raise ValueError("La nota debe estar entre 0.0 y 5.0")

    def _validar_nota_duplicada(self, estudiante, materia, semestre):
        for registro in self.notas:
            es_misma_nota = (
                registro["estudiante"] == estudiante
                and registro["materia"] == materia
                and registro["semestre"] == semestre
            )

            if es_misma_nota:
                raise ValueError(
                    "Ya existe una nota registrada para esta materia en el mismo semestre"
                )