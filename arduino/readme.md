# Medición de la respuesta del diodo con Arduino

## Descripción del código

Este código se encarga de **medir la respuesta del diodo** conectado al
amplificador y registrar las lecturas digitales en un **Arduino**.

En la salida del diodo receptor **HP 8470B** se implementó un **op-amp**
con filtro pasabajos y un amplificador de alta ganancia, diseñado para trabajar
con una **señal en DC que conmuta a 10 Hz**.\
El Arduino registra esta señal en el rango de **0--5 V**, con una **tasa
de muestreo de 50 Hz**.

------------------------------------------------------------------------

## Resultados de la medición

Se caracterizó la respuesta del diodo en un rango de **--40 a --14
dBm**, obteniéndose una curva de comportamiento **exponencial**.\
Este resultado dificultó un análisis detallado de la salida en DC,
debido a la alta **sensibilidad del detector**.

------------------------------------------------------------------------

## Próximos pasos

-   Implementar un **filtro RF** para concentrar el análisis en la señal
    de interés.\
-   Evaluar el uso de un **receptor heterodino** que permita una
    caracterización más lineal y precisa.

------------------------------------------------------------------------

![Medición: Voltaje vs
dBm](https://github.com/user-attachments/assets/bf388891-5b7f-4483-ab31-892a06354748)
