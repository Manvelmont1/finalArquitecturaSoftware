import pyodbc
import requests
from abc import ABC, abstractmethod

CONNECTION_STRING = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=LAPTOP-SQRL55HD\\SQLEXPRESS;"
    "DATABASE=validaciones;"
    "UID=sa;"
    "PWD=Solin1227;"
    "TrustServerCertificate=yes;"
    "Encrypt=yes;"
)

class IValidacionRepositorio(ABC):
    @abstractmethod
    def guardar_resultado(self, placa: str, cc_cliente: str, resultado: str) -> None:
        pass

class IFasecoldaCliente(ABC):
    @abstractmethod
    def obtener_resumen_accidentes(self, placa: str) -> dict:
        pass

class ValidacionRepositorio(IValidacionRepositorio):
    def _conectar(self):
        return pyodbc.connect(CONNECTION_STRING)

    def guardar_resultado(self, placa: str, cc_cliente: str, resultado: str) -> None:
        query = """
            INSERT INTO Validaciones (placa, ccCliente, resultado)
            VALUES (?, ?, ?)
        """
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (placa, cc_cliente, resultado))
            conn.commit()

class FasecoldaCliente(IFasecoldaCliente):
    def __init__(self, base_url: str = "http://localhost:8001"):
        # Puerto de fasecolda
        self.base_url = base_url

    def obtener_resumen_accidentes(self, placa: str) -> dict:
        try:
            response = requests.get(f"{self.base_url}/accidentes/{placa}", timeout=5)
            if response.status_code == 200:
                return response.json()
            return {"soloLatas": 0, "heridos": 0, "muertos": 0}
        except requests.exceptions.RequestException:
            raise RuntimeError("No se pudo establecer comunicación con el Microservicio de Fasecolda")
