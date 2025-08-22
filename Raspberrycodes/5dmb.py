import time
from valon_synth import Synthesizer

# Tabla de niveles RF disponibles
rf_level_table = {-4: 0, -1: 1, 2: 2, 5: 3}

# Ruta del puerto USB del Valon
port = '/dev/serial/by-id/usb-Valon_Technology_Valon_USB_UART_A5VPHY1E-if00-port0'

# Crear instancia del sintetizador
synth = Synthesizer(port)

# Identificadores de sintetizadores
SYNTH_A = 0
SYNTH_B = 8

# Configurar frecuencia
target_freq = 3400.0  # MHz
synth.set_frequency(SYNTH_A, target_freq)
synth.set_frequency(SYNTH_B, target_freq)

# Definir niveles de potencia para
levels_to_toggle = [5]
index = 0  # Índice para alternar
synth.set_rf_level(SYNTH_A, 5)
print(f"Nivel de salida RF establecido: 5 dBm")
