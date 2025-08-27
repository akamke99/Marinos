# Marinos

Este repositorio contiene los códigos relacionados con el siguiente esquema de sistema:

![Esquemático del sistema](https://github.com/user-attachments/assets/c85c7ac7-c3b4-4ef7-afc6-ad6a7807dd6c)

## Estructura del repositorio

### 📁 `Raspberrycodes/`

Contiene los scripts utilizados para configurar y controlar módulos conectados a la **Raspberry Pi**, incluyendo:

- Control de frecuencia mediante Valon Synth.
- Señales PWM para control de hardware externo.
- Integración opcional de módulo GPS.

### 📁 `signal_hound/`

Código que permite la comunicación entre un **PC** y el **analizador de espectro Signal Hound SA Series**.  
Este módulo facilita la recolección de datos de espectro para análisis posterior.

### 📁 `arduino/`

Código embebido en el **Arduino**, encargado de:

- Recolectar datos desde el **diodo** (sensor).
- Almacenar la información en una tarjeta **SD**.

## Descripción general

El sistema está compuesto por tres módulos principales (Raspberry, PC con Signal Hound, y Arduino) que trabajan en conjunto para medir, registrar y analizar señales RF.  
Cada carpeta en el repositorio contiene el software específico que corre en cada dispositivo del sistema.

---
