from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from capaNegocio.validacion import ValidacionServicio
from capaDatos.validacion import ValidacionRepositorio, FasecoldaCliente

router = APIRouter(prefix="/validaciones", tags=["Validaciones"])

class SolicitudValidacion(BaseModel):
    cedulaCliente: str
    placa: str

def obtener_servicio_validacion() -> ValidacionServicio:
    return ValidacionServicio(
        repositorio=ValidacionRepositorio(),
        fasecolda_cliente=FasecoldaCliente()
    )

@router.post("/realizar-validacion")
def realizar_validacion(solicitud: SolicitudValidacion, servicio: ValidacionServicio = Depends(obtener_servicio_validacion)):
    try:
        resultado = servicio.procesar_evaluacion(
            placa=solicitud.placa, 
            cc_cliente=solicitud.cedulaCliente
        )
        return resultado
    except RuntimeError as re:
        # Solo si el servicio de fasecolda no responde:
        raise HTTPException(status_code=503, detail=str(re))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))