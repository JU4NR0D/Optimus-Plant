import machine
import time

def sonido():
    # Definir la configuración del buzzer
   # BUZZER_PIN = 2
   # BUZZER_FREQ = 2000

    # Definir la secuencia de notas para la canción de Star Wars
    STAR_WARS_SONG = [
        (392, 500),
        (392, 500),
        (392, 500),
        (311, 350),
        (466, 150),
        (392, 500),
        (311, 350),
        (466, 150),
        (392, 1000),
        (587, 500),
        (587, 500),
        (587, 500),
        (622, 350),
        (466, 150),
        (369, 500),
        (311, 350),
        (466, 150),
        (392, 1000),
        (392, 350)
         ]

    # Inicializar el buzzer
    buzzer = machine.PWM(machine.Pin(32))
    buzzer.freq(2000)

    # Reproducir la canción de Star Wars
    for note in STAR_WARS_SONG:
        buzzer.freq(note[0])
        time.sleep_ms(note[1])

    
    # Detener el buzzer al finalizar la canción
    buzzer.deinit()

# Llamar a la función para reproducir la canción de Star Wars
sonido()