import serial
import datetime
import os

# Crear carpeta si no existe
log_dir = "/home/drone/gps"
os.makedirs(log_dir, exist_ok=True)

# Crear nombre de archivo con fecha y hora
filename = datetime.datetime.now().strftime("gps_log_%Y-%m-%d_%H-%M.txt")
filepath = os.path.join(log_dir, filename)

# Función para convertir coordenadas NMEA a decimal
def convert_to_degrees(raw_value):
    decimal_value = raw_value / 100.00
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - degrees) / 0.6
    position = degrees + mm_mmmm
    return round(position, 6)

# Configurar el puerto serie
ser = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)


try:
    with open(filepath, "a") as log_file:
        log_file.write("Timestamp,Latitude,Longitude\n")
        
        while True:
            line = ser.readline().decode("ascii", errors="ignore").strip()
            if "$GPGGA" in line or "$GNGGA" in line:
                parts = line.split(",")
                if len(parts) > 5 and parts[2] and parts[4]:
                    try:
                        raw_lat = float(parts[2])
                        raw_lon = float(parts[4])
                        lat = convert_to_degrees(raw_lat)
                        lon = convert_to_degrees(raw_lon)

                        if parts[3] == "S":
                            lat = -lat
                        if parts[5] == "W":
                            lon = -lon

                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        log_line = f"{timestamp},{lat},{lon}\n"
                        log_file.write(log_line)
                        log_file.flush()
                        print(log_line.strip())

                    except ValueError:
                        continue

except KeyboardInterrupt:
    ser.close()
