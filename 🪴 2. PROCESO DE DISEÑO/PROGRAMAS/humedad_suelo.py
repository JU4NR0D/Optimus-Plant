from machine import Pin, ADC
import utime

soil = ADC(Pin(2))

def humedad_suelo():
    #lectura = abs((((soil.read_u16()-48440)*100)/3560)-100)
   # lectura = max(0, min(100, lectura))  # Asegura que el valor esté entre 0 y 100
    return(max(0, min(100, abs((((soil.read_u16()-48440)*100)/3560)-100))))

#while True: