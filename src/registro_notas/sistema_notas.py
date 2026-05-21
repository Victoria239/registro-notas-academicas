NOTA_MINIMA = 0.0
NOTA_MAXIMA = 5.0
NOTA_MINIMA_APROBACION = 3.0


class SistemaNotas:
    def __init__(self):
        self.notas = []

    def registrar_nota(self, estudiante, materia, semestre, nota):
        self._validar_rango_nota(nota)

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

    def _validar_rango_nota(self, nota):
        if nota < NOTA_MINIMA or nota > NOTA_MAXIMA:
            raise ValueError("La nota debe estar entre 0.0 y 5.0")