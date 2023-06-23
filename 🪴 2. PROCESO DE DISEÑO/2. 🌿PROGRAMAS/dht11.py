import machine
import dht

#dht_pin = machine.Pin(5)  # Ajusta el número de pin GPIO al que está conectado el sensor DHT11
d = dht.DHT11(machine.Pin(5))

def temperatura():
     try:
        d.measure()
        return d.temperature()
     except:
        return 10
#temperatura = leer_temperatura()
     return(format(temperatura()))

def humedad_amb():
    try:
        d.measure()
        return d.humidity()
    except:
        return 65
#temperatura = leer_temperatura()
    return(format(humedad_amb()))