from capaDatos.accidente import IAccidente

class AccidenteServicio:

    def __init__(self, accidente: IAccidente):
        self._accidente = accidente

    def consultar_por_placa(self, placa: str) -> dict:
        return self._accidente.obtener_resumen_por_placa(placa)