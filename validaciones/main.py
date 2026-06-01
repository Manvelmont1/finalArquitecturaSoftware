import uvicorn
from fastapi import FastAPI
from capaPresentacion.validacion import router

app = FastAPI(title="Microservicio de Validaciones de Pólizas")
app.include_router(router)

if __name__ == "__main__":
    # Corre en el puerto 8000:
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)