import uvicorn
from fastapi import FastAPI
# 1. Quitamos "fasecolda." del import
from capaPresentacion.accidente import router 

app = FastAPI(title="Microservicio Fasecolda")
app.include_router(router)

if __name__ == "__main__":
    # 2. Cambiamos "fasecolda.main:app" por "main:app"
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)