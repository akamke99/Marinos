# Control de Módulos en Raspberry Pi

Este sistema utiliza una Raspberry Pi para controlar distintos módulos relacionados con transmisión RF y señalización. A continuación, se describen los principales scripts utilizados, su función y su configuración.

## Estructura de módulos

### 1. `5dmb.py`

- **Función:** Configura el generador de frecuencia **Valon Synth** para emitir a **5 dBm**.
- **Requiere:** Librería oficial del Valon Synth disponible en [https://github.com/nrao/ValonSynth](https://github.com/nrao/ValonSynth).
- **Notas de uso:**  
  - El script ya se encuentra configurado para ejecutar correctamente con la Raspberry Pi.  
  - Si se necesita replicar la configuración en otra Raspberry, es posible copiar directamente los archivos correspondientes.

### 2. `pwm.py`

- **Función:** Controla la señal **PWM** emitida por la Raspberry Pi.
- **Frecuencia actual:** **10 Hz** (definida dentro del código).
- **Modificaciones:**  
  - Cualquier cambio en la frecuencia o configuración de la PWM debe realizarse directamente dentro del script.  
  - No requiere intervención externa o parámetros al ejecutarlo.

### 3. `gps.py`

- **Función:** Permite incorporar un **módulo GPS** externo.
- **Estado actual:**  
  - El código está funcional, pero **no se utiliza actualmente** en operaciones regulares.  
  - Su ejecución automática está **comentada en el crontab**.
  - Puede ser activado manualmente si se requiere en el futuro.

## Automatización con Crontab

La Raspberry Pi está configurada para iniciar automáticamente los scripts necesarios mediante el sistema `crontab`.  
Esto asegura que los módulos requeridos se ejecuten al arrancar el sistema sin intervención manual.

### Diagrama de conexión

La siguiente imagen muestra el diagrama de conexión y arquitectura del sistema:

![Diagrama del sistema](https://github.com/user-attachments/assets/7f974c4d-43ce-4adb-9a5c-ffdedeeb502c)

## Notas adicionales

- Para clonar o portar la configuración a otra Raspberry Pi, se recomienda copiar el entorno completo junto con los scripts (`5dmb.py`, `pwm.py`, y `gps.py`) y revisar las entradas en el crontab.
- Verificar dependencias externas (como la librería del Valon Synth) antes de ejecutar por primera vez en un nuevo dispositivo.
