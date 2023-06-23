from machine import Pin, ADC
import time

adc = ADC(Pin(15))
adc.atten(ADC.ATTN_11DB)
#ldr_pin = Pin(15, Pin.IN)
def fotocelda():
    # Configuración del pin de la fotocelda
    #ldr_pin = Pin(15, Pin.IN)

    # Configuración del ADC (Convertidor Analógico-Digital)
    #adc = ADC(Pin(15))
    #adc.atten(ADC.ATTN_11DB)  # Configuración de atenuación para una mayor resolución

   # while True:
        #ldr_value =((adc.read()-4095)*-100)/4095  # Leer el valor analógico de la fotocelda
        return( ((adc.read()-4095)*-100)/4095)

       # time.sleep(1)  # Esperar 1 segundo antes de leer nuevamente

# Llamar a la función para obtener los valores continuamente
#fotocelda()