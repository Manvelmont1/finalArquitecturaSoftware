import pyodbc
from abc import ABC, abstractmethod

CONNECTION_STRING = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=LAPTOP-SQRL55HD\\SQLEXPRESS;"
    "DATABASE=fasecolda;"
    "UID=sa;"
    "PWD=Solin1227;"
    "TrustServerCertificate=yes;"
    "Encrypt=yes;"
)

class IAccidente(ABC):

    @abstractmethod
    def obtener_resumen_por_placa(self, placa: str) -> dict:
        pass

class Accidente(IAccidente):

    def _conectar(self):
        return pyodbc.connect(CONNECTION_STRING)

    def obtener_resumen_por_placa(self, placa: str) -> dict:
        query = """
            SELECT
                SUM(CASE WHEN severidad = 'solo latas' THEN 1 ELSE 0 END) AS soloLatas,
                SUM(CASE WHEN severidad = 'heridos'    THEN 1 ELSE 0 END) AS heridos,
                SUM(CASE WHEN severidad = 'muertos'    THEN 1 ELSE 0 END) AS muertos
            FROM AccidentesFasecolda
            WHERE placa = ?
        """
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(query, placa)
            row = cursor.fetchone()
            return {
                "soloLatas": row.soloLatas or 0,
                "heridos":   row.heridos   or 0,
                "muertos":   row.muertos   or 0,
            }
