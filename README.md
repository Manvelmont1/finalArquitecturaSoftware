# Final Arquitectura de Software

### Autores:
* Manuel Jose Velez Montoya.
* Mateo Cano Rendón.

# Instrucciones de ejecucion:

## 1. Iniciar el servicio de Fasecolda
 
Este servicio se conecta a la base de datos de accidentes de Fasecolda y expone el historial de siniestros por placa.
 
1. Abrir una terminal (CMD).
2. Navegar a la carpeta de fasecolda:
```
cd D:\...\...\fasecolda
```
 
3. Ejecutar el archivo desde el CMD para iniciar el servidor:
```
python main.py
```
 
El servicio se empezara a ejecutar desde: `http://localhost:8001`

## 2. Iniciar el servicio de validaciones
 Este usa al servicio de Fasecolda y guarda los registros en la base de datos de nombre "validaciones".
 
1. Abrir una terminal (CMD), (sin cerrar la anterior).
2. Navegar a la carpeta de validaciones:
```
cd D:\...\...\validaciones
```
 
3. Ejecuta el archivo en CMD para iniciar el servicio:
```
python main.py
```
 
El servicio se empezara a ejecutar en: `http://localhost:8000`
