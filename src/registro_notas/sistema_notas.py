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

        if nota >= 3.0:
            return "Aprobado"

        return "Reprobado"

    def _validar_rango_nota(self, nota):
        if nota < 0.0 or nota > 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0")