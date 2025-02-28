# Internet Connection Monitor

Este proyecto es un script en Python que monitorea el estado de la conexión a Internet en intervalos personalizables. Registra los períodos de conexión activa e inactiva en un archivo de log y genera un resumen detallado de los intervalos. Perfecto para analizar la inestabilidad de la red y diagnosticar problemas de conectividad.

## Características principales:
- Monitoreo en tiempo real de la conexión a Internet.
- Intervalos de verificación de conexión personalizables.
- Generación de logs detallados y resúmenes de intervalos.

## Requisitos:
- Python 3.x
- Librería `requests`

## Uso:
1. Clona el repositorio.
2. Ejecuta el script:
   `py internet_monitor.py`
3. Ingresar el intervalo


## Ejemplo de summary.log
```
Resumen de intervalos:
Intervalo 1: Activa durante 304.81 segundos
Intervalo 2: Perdida durante 16.12 segundos
Intervalo 3: Activa durante 18.81 segundos
Intervalo 4: Perdida durante 14.11 segundos
Intervalo 5: Activa durante 477.18 segundos
Intervalo 6: Perdida durante 14.12 segundos
Intervalo 7: Activa durante 404.14 segundos
```
