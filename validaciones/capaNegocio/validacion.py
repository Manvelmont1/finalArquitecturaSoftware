from capaDatos.validacion import IValidacionRepositorio, IFasecoldaCliente

class ValidacionServicio:
    def __init__(self, repositorio: IValidacionRepositorio, fasecolda_cliente: IFasecoldaCliente):
        self._repositorio = repositorio
        self._fasecolda_cliente = fasecolda_cliente

    def procesar_evaluacion(self, placa: str, cc_cliente: str) -> dict:
        historial = self._fasecolda_cliente.obtener_resumen_accidentes(placa)
        
        puntos = 0
        puntos += historial.get("soloLatas", 0) * 100
        puntos += historial.get("heridos", 0) * 200
        puntos += historial.get("muertos", 0) * 300
        
        # Limite: 400 puntos.
        if puntos >= 400:
            resultado_db = "rechazada"
            respuesta_api = {"cotizacion": False}
        else:
            resultado_db = "aprobada"
            respuesta_api = {"cotizacion": True}

        self._repositorio.guardar_resultado(placa, cc_cliente, resultado_db)
        
        return respuesta_api
