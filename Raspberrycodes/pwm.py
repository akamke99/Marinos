import RPi.GPIO as GPIO
import time

# Configuración del pin
PIN_PWM = 18  # Cambia esto por el puerto GPIO que uses
FRECUENCIA = 10  # Frecuencia en Hz

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_PWM, GPIO.OUT)

# Inicializar PWM
pwm = GPIO.PWM(PIN_PWM, FRECUENCIA)
pwm.start(50)  # Ciclo de trabajo inicial (50%)

try:
    while True:
        time.sleep(1)  # Mantén la señal activa
except KeyboardInterrupt:
    print("Deteniendo PWM...")
    pwm.stop()
    GPIO.cleanup()
