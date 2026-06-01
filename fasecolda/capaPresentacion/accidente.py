# fasecolda/capaPresentacion/accidente.py
from fastapi import APIRouter, HTTPException, Depends
from capaNegocio.accidente import AccidenteServicio
from capaDatos.accidente import Accidente, IAccidente

router = APIRouter(prefix="/accidentes", tags=["Accidentes"])

# Función proveedora de la dependencia
def obtener_servicio_accidente() -> AccidenteServicio:
    # Aquí es el único lugar de la capa que conoce la implementación concreta (Accidente)
    return AccidenteServicio(accidente=Accidente())

@router.get("/{placa}")
def consultar_accidentes(placa: str, servicio: AccidenteServicio = Depends(obtener_servicio_accidente)):
    try:
        resultado = servicio.consultar_por_placa(placa)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    