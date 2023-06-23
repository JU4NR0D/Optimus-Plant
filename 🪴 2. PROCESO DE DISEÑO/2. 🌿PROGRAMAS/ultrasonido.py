import machine
import time

# Configuración de los pines
#TRIGGER_PIN = 12
#ECHO_PIN = 14
 
# Inicializar los pines del sensor de ultrasonido
trigger = machine.Pin(14, machine.Pin.OUT)
echo = machine.Pin(12, machine.Pin.IN)

def leerDistancia():
    # Generar un pulso de 10 microsegundos en el pin TRIGGER para iniciar la medición
    trigger.value(0)
    time.sleep_us(2)
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)

    # Esperar a que el pin ECHO se active
    while echo.value() == 0:
        pass
    start_time = time.ticks_us()

    # Esperar a que el pin ECHO se desactive
    while echo.value() == 1:
        pass
    end_time = time.ticks_us()

    # Calcular la duración del pulso en microsegundos
    #pulse_duration = time.ticks_diff(end_time, start_time)

    # Calcular la distancia en centímetros
    #distance_cm = time.ticks_diff(end_time, start_time)/ 58.0

    return time.ticks_diff(end_time, start_time)/ 58.0
    