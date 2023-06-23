from machine import Pin, ADC, I2C, PWM
import ssd1306
import math
import utime
import dht
import time

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

buzzer = None
soil = ADC(Pin(2))
i2c = I2C(scl=Pin(22), sda=Pin(21))
adc = ADC(Pin(15))
adc.atten(ADC.ATTN_11DB)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
d = dht.DHT11(Pin(5))
trigger = Pin(14, Pin.OUT)
echo = Pin(12, Pin.IN)


def humedad_suelo():
    lectura = max(0, min(100, abs((((soil.read_u16()-48440)*100)/3560)-100)))
    return lectura


def temperatura():
    try:
        d.measure()
        return d.temperature()
    except:
        return 10


def humedad_amb():
    try:
        d.measure()
        return d.humidity()
    except:
        return 65


def fotocelda():
    return ((adc.read()-4095)*-100)/4095


def leerDistancia():
    trigger.value(0)
    time.sleep_us(2)
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)

    while echo.value() == 0:
        pass
    start_time = time.ticks_us()

    while echo.value() == 1:
        pass
    end_time = time.ticks_us()

    return time.ticks_diff(end_time, start_time) / 58.0

def problem():
    a = leerDistancia()
    b = fotocelda()
    c = temperatura()
    d = humedad_amb()
    e = humedad_suelo()

    z = 0
    if b < 80:
        z += 1
    if c < 8 or c > 35:
        z += 1
    if d < 30 or d > 90:
        z += 1
    if e < 15 or e > 60:
        z += 1

    return z


def carasad():
    
    oled.fill(0)  # Limpiar la pantalla

    a = leerDistancia()
    b = fotocelda()
    c = temperatura()
    d = humedad_amb()
    e = humedad_suelo()
    x = problem()

    if a < 50 and x==4  :
        
        oled.fill(0)  # Limpiar la pantalla
        oled.ellipse(64, 32, 30, 24, 1)
        oled.line(54, 20, 62, 28, 1)
        oled.line(54, 28, 62, 20, 1)
        oled.line(78, 20, 70, 28, 1)
        oled.line(78, 28, 70, 20, 1)
        oled.ellipse(64, 45, 10, 6, 1)
        oled.text("Voy", 0,1,1)
        oled.text("a", 0,8,1)
        oled.text("morir", 0,15,1)
        oled.show()
        buzzer = PWM(Pin(32))  # Inicializar el objeto PWM
        buzzer.freq(2000)

        for note in STAR_WARS_SONG:
            buzzer.freq(note[0])
            time.sleep_ms(note[1])

        buzzer.deinit()

        
    elif a > 50 and x==4 :
       
        oled.fill(0)  # Limpiar la pantalla
        oled.ellipse(64, 32, 30, 24, 1)
        oled.line(54, 20, 62, 28, 1)
        oled.line(54, 28, 62, 20, 1)
        oled.line(78, 20, 70, 28, 1)
        oled.line(78, 28, 70, 20, 1)
        oled.ellipse(64, 45, 10, 6, 1)
        oled.text("Voy", 0,1,1)
        oled.text("a", 0,8,1)
        oled.text("morir", 0,15,1)
        oled.show()
    
    elif a < 50 and x==3:
     
     oled.fill(0)  # Limpiar la pantalla
     oled.ellipse(64, 32, 30, 24, 1)
     oled.ellipse(54, 25, 8, 12, 1)
     oled.ellipse(74, 25, 8, 12, 1)
     oled.ellipse(54, 25, 4, 6, 1)
     oled.ellipse(74, 25, 4, 6, 1)
     oled.pixel(54, 25, 0)
     oled.pixel(74, 25, 0)
     oled.line(48, 15, 58, 20, 1)
     oled.line(70, 20, 80, 15, 1)
     oled.line(54, 45, 64, 35, 1)
     oled.line(64, 35, 74, 45, 1)
     oled.text("Deseas", 0,1,1)
     oled.text("que", 0,7,1)
     oled.text("muera?", 0,13,1)
     oled.show()
     buzzer = PWM(Pin(32))  # Inicializar el objeto PWM
     buzzer.freq(2000)

     for note in STAR_WARS_SONG:
        buzzer.freq(note[0])
        time.sleep_ms(note[1])

     buzzer.deinit()
        
    elif a > 50 and x==3:
     oled.fill(0)  # Limpiar la pantalla
     oled.ellipse(64, 32, 30, 24, 1)
     oled.ellipse(54, 25, 8, 12, 1)
     oled.ellipse(74, 25, 8, 12, 1)
     oled.ellipse(54, 25, 4, 6, 1)
     oled.ellipse(74, 25, 4, 6, 1)
     oled.pixel(54, 25, 0)
     oled.pixel(74, 25, 0)
     oled.line(48, 15, 58, 20, 1)
     oled.line(70, 20, 80, 15, 1)
     oled.line(54, 45, 64, 35, 1)
     oled.line(64, 35, 74, 45, 1)
     oled.text("Deseas", 0,1,1)
     oled.text("que", 0,7,1)
     oled.text("muera?", 0,13,1)
     oled.show()
    
    elif a < 50 and x==2:
     
     oled.fill(0)  # Limpiar la pantalla
     oled.ellipse(64, 32, 30, 24, 1)
     oled.ellipse(54, 25, 8, 12, 1)
     oled.ellipse(74, 25, 8, 12, 1)
     oled.ellipse(54, 25, 4, 6, 1)
     oled.ellipse(74, 25, 4, 6, 1)
     oled.pixel(54, 25, 0)
     oled.pixel(74, 25, 0)
     oled.text("Toy", 0,1,1)
     oled.text("triste", 0,8,1)
     center_x = 64
     center_y = 63
     radius = -20
     start_angle = math.pi * 0.3  # Ángulo de inicio (en radianes)
     end_angle = math.pi * 0.7  # Ángulo final (en radianes)
     arc_points = 20  # Número de puntos para trazar el arco

     for i in range(arc_points + 1):
        angle = start_angle + (end_angle - start_angle) * i / arc_points
        x = int(center_x + math.cos(angle) * radius)
        y = int(center_y + math.sin(angle) * radius)
        oled.pixel(x, y, 1)
     oled.show()
     buzzer = PWM(Pin(32))  # Inicializar el objeto PWM
     buzzer.freq(2000)

     for note in STAR_WARS_SONG:
        buzzer.freq(note[0])
        time.sleep_ms(note[1])

     buzzer.deinit()
     
    elif a > 50 and x==2:
      oled.fill(0)  # Limpiar la pantalla
      oled.ellipse(64, 32, 30, 24, 1)
      oled.ellipse(54, 25, 8, 12, 1)
      oled.ellipse(74, 25, 8, 12, 1)
      oled.ellipse(54, 25, 4, 6, 1)
      oled.ellipse(74, 25, 4, 6, 1)
      oled.pixel(54, 25, 0)
      oled.pixel(74, 25, 0)
      oled.text("Toy", 0,1,1)
      oled.text("triste", 0,8,1)
      center_x = 64
      center_y = 63
      radius = -20
      start_angle = math.pi * 0.3  # Ángulo de inicio (en radianes)
      end_angle = math.pi * 0.7  # Ángulo final (en radianes)
      arc_points = 20  # Número de puntos para trazar el arco

      for i in range(arc_points + 1):
        angle = start_angle + (end_angle - start_angle) * i / arc_points
        x = int(center_x + math.cos(angle) * radius)
        y = int(center_y + math.sin(angle) * radius)
        oled.pixel(x, y, 1)
      oled.show()
      
    elif a<50 and x==1:
            if b < 100:
                oled.fill(0)
                oled.ellipse(64, 32, 20, 14, 1)  # Elipse exterior del sol
                oled.line(64, 8, 64, 16, 1)  # Rayo vertical superior
                oled.line(64, 48, 64, 56, 1)  # Rayo vertical inferior
                oled.line(32, 32, 40, 32, 1)  # Rayo horizontal izquierdo
                oled.line(86, 32, 94, 32, 1)  # Rayo horizontal derecho
                oled.line(40, 12, 48, 20, 1)  # Rayo diagonal superior izquierdo
                oled.line(80, 42, 88, 50, 1)  # Rayo diagonal inferior derecho
                oled.line(88, 12, 80, 20, 1)  # Rayo diagonal superior derecho
                oled.line(44, 42, 36, 50, 1)  # Rayo diagonal inferior izquierdo
                oled.line(2,39,16,39,1)# signo menos
                oled.line(9,46,9,32,1)#rayita para signo más
                oled.text("Dame ", 0,8, 1)
                oled.text("luz", 0,16 , 1)
                oled.show()
                buzzer = PWM(Pin(32))  # Inicializar el objeto PWM
                buzzer.freq(2000)

                for note in STAR_WARS_SONG:
                     buzzer.freq(note[0])
                     time.sleep_ms(note[1])

                buzzer.deinit()

            elif c < 8:
                oled.fill(0)
                oled.ellipse(64, 32, 30, 30, 1)  # Cara
                oled.ellipse(54, 25, 8, 12, 1)  # Ojo izquierdo
                oled.ellipse(74, 25, 8, 12, 1)  # Ojo derecho
                oled.ellipse(54, 25, 4, 6, 1)  # Pupila izquierda
                oled.ellipse(74, 25, 4, 6, 1)  # Pupila derecha
                oled.line(48, 38, 58, 43, 1)  # Ceja izquierda
                oled.line(70, 43, 80, 38, 1)  # Ceja derecha
                oled.line(54, 48, 74, 48, 1)  # Boca
                oled.text("(", 45, 15, 1)
                oled.text(")", 85, 15, 1)
                oled.text("(", 45, 35, 1)
                oled.text(")", 85, 35, 1)
                oled.text("(", 45, 55, 1)
                oled.text(")", 85, 55, 1)
                oled.text("Teno",0,1,1)
                oled.text("frio",0,8,1)
                oled.show()
                buzzer = PWM(Pin(32))  # Inicializar el objeto PWM
                buzzer.freq(2000)

                for note in STAR_WARS_SONG:
                     buzzer.freq(note[0])
                     time.sleep_ms(note[1])

                buzzer.deinit()
                
            elif c > 35:
                oled.fill(0)
                oled.ellipse(64, 32, 30, 30, 1)  # Cara
                oled.ellipse(54, 25, 8, 12, 1)  # Ojo izquierdo
                oled.ellipse(74, 25, 8, 12, 1)  # Ojo derecho
                oled.ellipse(54, 25, 4, 6, 1)  # Pupila izquierda
                oled.ellipse(74, 25, 4, 6, 1)  # Pupila derecha
                oled.ellipse(64, 50, 10, 6, 1)  # Boca
                oled.ellipse(90, 25, 2, 5, 1)  # Gota de sudor
                oled.ellipse(90, 50, 3, 8, 1)  # Gota de sudor
                oled.text("Estoy ", 0,8, 1)
                oled.text("muy", 0,16 , 1)
                oled.text("hot!", 0, 24, 1)
                oled.show()
                buzzer = PWM(Pin(32))  # Inicializar el objeto PWM
                buzzer.freq(2000)

                for note in STAR_WARS_SONG:
                     buzzer.freq(note[0])
                     time.sleep_ms(note[1])

                buzzer.deinit()
                
            elif d < 30:
                oled.fill(0)
                oled.text("La humedad aqui",0, 0,1)
                oled.text("es muy baja",0, 25,1)
                oled.text("ayudame :((((",0, 50,1)
                oled.show()
                buzzer = PWM(Pin(32))  # Inicializar el objeto PWM
                buzzer.freq(2000)

                for note in STAR_WARS_SONG:
                     buzzer.freq(note[0])
                     time.sleep_ms(note[1])

                buzzer.deinit()
                
            elif d > 90:
                oled.fill(0)
                oled.ellipse(64, 32, 30, 30, 1)  # Cara
                oled.ellipse(54, 25, 8, 12, 1)
                oled.ellipse(74, 25, 8, 12, 1)
                oled.ellipse(54, 25, 4, 6, 1)
                oled.ellipse(74, 25, 4, 6, 1)
                oled.pixel(54, 25, 0)
                oled.pixel(74, 25, 0)
                oled.ellipse(64, 45, 8, 4, 1)  # Boca
                oled.ellipse(48, 40, 6, 3, 1)  # Mejilla izquierda
                oled.ellipse(82, 40, 6, 3, 1)# Mejilla derecha
                oled.text("me",0,1,1)
                oled.text("vuelvo ",0,8,1)
                oled.text("moho",0,15,1)
                oled.show()
                buzzer = PWM(Pin(32))  # Inicializar el objeto PWM
                buzzer.freq(2000)

                for note in STAR_WARS_SONG:
                     buzzer.freq(note[0])
                     time.sleep_ms(note[1])

                buzzer.deinit()
                
            elif e < 15:
                oled.fill(0)
                oled.ellipse(64, 32, 30, 30, 1)  # Cara
                oled.line(54, 25, 62, 33, 1)  # Ojo izquierdo
                oled.line(54, 33, 62, 25, 1)  # Ojo izquierdo
                oled.line(70, 25, 78, 33, 1)  # Ojo derecho
                oled.line(70, 33, 78, 25, 1)  # Ojo derecho
                oled.ellipse(64, 45, 10, 6, 1)  # Boca
                oled.ellipse(70, 55, 3, 6, 1)
                oled.text("Tengo",0,1,1)
                oled.text("mucha",0,8,1)
                oled.text("sed",0,15,1)
                oled.show()
                buzzer = PWM(Pin(32))  # Inicializar el objeto PWM
                buzzer.freq(2000)

                for note in STAR_WARS_SONG:
                     buzzer.freq(note[0])
                     time.sleep_ms(note[1])

                buzzer.deinit()
                
            elif e > 60:
                oled.fill(0)
                oled.ellipse(64, 32, 30, 30, 1)  # Cara
                oled.line(54, 25, 62, 33, 1)  # Ojo izquierdo
                oled.line(54, 33, 62, 25, 1)  # Ojo izquierdo
                oled.line(70, 25, 78, 33, 1)  # Ojo derecho
                oled.line(70, 33, 78, 25, 1)  # Ojo derecho
                oled.line(54, 45, 74, 45, 1)  # Boca
                oled.line(62, 50, 62, 60, 1)
                oled.line(66, 50, 66, 60, 1)
                oled.line(70, 50, 70, 60, 1)
                oled.text("Bebi",0,1,1)
                oled.text("mucha",0,8,1)
                oled.text("agua",0,15,1)
                oled.show()
                buzzer = PWM(Pin(32))  # Inicializar el objeto PWM
                buzzer.freq(2000)

                for note in STAR_WARS_SONG:
                     buzzer.freq(note[0])
                     time.sleep_ms(note[1])

                buzzer.deinit()
                   
    elif a>50 and x==1:
            if b < 80:
                oled.fill(0)
                oled.ellipse(64, 32, 20, 14, 1)  # Elipse exterior del sol
                oled.line(64, 8, 64, 16, 1)  # Rayo vertical superior
                oled.line(64, 48, 64, 56, 1)  # Rayo vertical inferior
                oled.line(32, 32, 40, 32, 1)  # Rayo horizontal izquierdo
                oled.line(86, 32, 94, 32, 1)  # Rayo horizontal derecho
                oled.line(40, 12, 48, 20, 1)  # Rayo diagonal superior izquierdo
                oled.line(80, 42, 88, 50, 1)  # Rayo diagonal inferior derecho
                oled.line(88, 12, 80, 20, 1)  # Rayo diagonal superior derecho
                oled.line(44, 42, 36, 50, 1)  # Rayo diagonal inferior izquierdo
                oled.line(2,39,16,39,1)# signo menos
                oled.line(9,46,9,32,1)#rayita para signo más
                oled.text("Dame ", 0,8, 1)
                oled.text("luz", 0,16 , 1)
                oled.show()
               

            elif c < 8:
                oled.fill(0)
                oled.ellipse(64, 32, 30, 30, 1)  # Cara
                oled.ellipse(54, 25, 8, 12, 1)  # Ojo izquierdo
                oled.ellipse(74, 25, 8, 12, 1)  # Ojo derecho
                oled.ellipse(54, 25, 4, 6, 1)  # Pupila izquierda
                oled.ellipse(74, 25, 4, 6, 1)  # Pupila derecha
                oled.line(48, 38, 58, 43, 1)  # Ceja izquierda
                oled.line(70, 43, 80, 38, 1)  # Ceja derecha
                oled.line(54, 48, 74, 48, 1)  # Boca
                oled.text("(", 45, 15, 1)
                oled.text(")", 85, 15, 1)
                oled.text("(", 45, 35, 1)
                oled.text(")", 85, 35, 1)
                oled.text("(", 45, 55, 1)
                oled.text(")", 85, 55, 1)
                oled.text("Teno",0,1,1)
                oled.text("frio",0,8,1)
                oled.show()
                
                
            elif c > 35:
                oled.fill(0)
                oled.ellipse(64, 32, 30, 30, 1)  # Cara
                oled.ellipse(54, 25, 8, 12, 1)  # Ojo izquierdo
                oled.ellipse(74, 25, 8, 12, 1)  # Ojo derecho
                oled.ellipse(54, 25, 4, 6, 1)  # Pupila izquierda
                oled.ellipse(74, 25, 4, 6, 1)  # Pupila derecha
                oled.ellipse(64, 50, 10, 6, 1)  # Boca
                oled.ellipse(90, 25, 2, 5, 1)  # Gota de sudor
                oled.ellipse(90, 50, 3, 8, 1)  # Gota de sudor
                oled.text("Estoy ", 0,8, 1)
                oled.text("muy", 0,16 , 1)
                oled.text("hot!", 0, 24, 1)
                oled.show()
                
            elif d < 30:
                oled.fill(0)
                oled.text("La humedad aqui",0, 0,1)
                oled.text("es muy baja",0, 25,1)
                oled.text("ayudame :((((",0, 50,1)
                oled.show()
                
            elif d > 90:
                oled.fill(0)
                oled.ellipse(64, 32, 30, 30, 1)  # Cara
                oled.ellipse(54, 25, 8, 12, 1)
                oled.ellipse(74, 25, 8, 12, 1)
                oled.ellipse(54, 25, 4, 6, 1)
                oled.ellipse(74, 25, 4, 6, 1)
                oled.pixel(54, 25, 0)
                oled.pixel(74, 25, 0)
                oled.ellipse(64, 45, 8, 4, 1)  # Boca
                oled.ellipse(48, 40, 6, 3, 1)  # Mejilla izquierda
                oled.ellipse(82, 40, 6, 3, 1)# Mejilla derecha
                oled.text("me",0,1,1)
                oled.text("vuelvo ",0,8,1)
                oled.text("moho",0,15,1)
                oled.show()
                
            elif e < 15:
                oled.fill(0)
                oled.ellipse(64, 32, 30, 30, 1)  # Cara
                oled.line(54, 25, 62, 33, 1)  # Ojo izquierdo
                oled.line(54, 33, 62, 25, 1)  # Ojo izquierdo
                oled.line(70, 25, 78, 33, 1)  # Ojo derecho
                oled.line(70, 33, 78, 25, 1)  # Ojo derecho
                oled.ellipse(64, 45, 10, 6, 1)  # Boca
                oled.ellipse(70, 55, 3, 6, 1)
                oled.text("Tengo",0,1,1)
                oled.text("mucha",0,8,1)
                oled.text("sed",0,15,1)
                oled.show()
                
            elif e > 60:
                oled.fill(0)
                oled.ellipse(64, 32, 30, 30, 1)  # Cara
                oled.line(54, 25, 62, 33, 1)  # Ojo izquierdo
                oled.line(54, 33, 62, 25, 1)  # Ojo izquierdo
                oled.line(70, 25, 78, 33, 1)  # Ojo derecho
                oled.line(70, 33, 78, 25, 1)  # Ojo derecho
                oled.line(54, 45, 74, 45, 1)  # Boca
                oled.line(62, 50, 62, 60, 1)
                oled.line(66, 50, 66, 60, 1)
                oled.line(70, 50, 70, 60, 1)
                oled.text("Bebi",0,1,1)
                oled.text("mucha",0,8,1)
                oled.text("agua",0,15,1)
                oled.show()
                
                
    else:
       oled.fill(0)
       oled.ellipse(64, 32, 30, 24, 1)
       oled.ellipse(54, 25, 8, 12, 1)
       oled.ellipse(74, 25, 8, 12, 1)
       oled.ellipse(54, 25, 4, 6, 1)
       oled.ellipse(74, 25, 4, 6, 1)
       oled.pixel(54, 25, 0)
       oled.pixel(74, 25, 0)
       oled.text("Ando", 0,4,1)
       oled.text("feli!", 0,12,1)
       for x in range(20):
          y = int(27 + math.sqrt(20**2 - (x-10)**2))
          oled.pixel(55+x, y, 1)
        #oled.pixel(84-x, y, 1)
       oled.show()
       
        
        
    
# Bucle principal
while True:
    carasad()
    utime.sleep(1)