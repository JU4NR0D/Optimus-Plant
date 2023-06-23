# Componentes en Protoboard

En la fase de diseño, nuestro objetivo principal es comprender las conexiones y funcionalidades de cada componente de forma individual en relación a la placa ESP32 en la protoboard. Para lograrlo, realizamos un análisis detallado de las características de cada componente, incluyendo su voltaje, la información que genera o necesita, y otros aspectos relevantes.

A continuación, se presentan imágenes de cada componente junto con una breve explicación de su función:

Sensor de Humedad Capacitivo: Este sensor permite medir la humedad relativa del ambiente utilizando la técnica de capacitancia. Proporciona una salida analógica, por tanto tendrá conexiones con el pin GPIO2, los otros dos cables son GND (Cable Negro) y VCC (Cable Rojo). Es necesario establecer la conexión adecuada entre el sensor de humedad capacitivo y la ESP32 para recibir y procesar estos datos, esto se hace a través de la programación del microcontrolador, funciona bien con 3.3V.

[Insertar imagen del sensor de humedad capacitivo]

DHT11: El sensor DHT11 es un sensor de temperatura y humedad relativa del ambiente. Proporciona información precisa sobre la temperatura y la humedad en forma digital. Para utilizar el DHT11, se deben establecer las 3 conexiones de la siguiente manera: el DAC se conecta con el GPIO5 y los otros dos son GND y VCC, funciona bien con un voltaje de 3.3V.

[Insertar imagen del sensor DHT11]

Módulo sensor de Fotorresistencia de 3 pines: Este módulo permite medir la intensidad de luz ambiental utilizando una fotorresistencia. Proporciona una salida analógica proporcional a la intensidad de luz detectada. Se debe conectar correctamente al GPIO15 que es un ADC, los otros a VCC y GND, funciona bien con un voltaje de 3.3V.

[Insertar imagen del módulo sensor de fotorresistencia de 3 pines]

HC-SR04: El módulo HC-SR04 es un sensor ultrasónico de distancia. Utiliza ondas ultrasónicas para medir la distancia entre el sensor y un objeto. Proporciona una salida digital que indica la distancia medida. Es necesario establecer las conexiones en: ECHO con el GPIO13 y el TRIGGER con el GPIO12, GND, y VCC de 5V. Se deben procesar estos datos con programación.

[Insertar imagen del módulo HC-SR04]

Pantalla Gráfica OLED I2C: Esta pantalla OLED utiliza la interfaz I2C para mostrar información al usuario de manera visual. Permite mostrar texto, números y gráficos en un tamaño compacto. Es necesario identificar los pines de la ESP32 que se utilizarán para la comunicación con la pantalla y establecer las conexiones correctas para su funcionamiento, por ejemplo el SDA va conectado al GPIO21 y el SCL al GPIO22, puesto a que son los indicados en el pinout para este motivo, funciona con un VCC de 3V y un GND conectado naturalmente a alguna tierra, las caras que incorporaremos son programables.

[Insertar imagen de la pantalla gráfica OLED I2C]

Amplificador de Audio Digital PAM-8403: Este amplificador digital se utiliza para amplificar señales de audio. Es compatible con diferentes fuentes de sonido y altavoces. Se debe conectar el L + y - del OUT con el buzzer para reproducir el audio de manera adecuada y en el IN se conecta el R con el pin GPIO4 ya que es ADC, y el resto es GND´s y VCC funcional de 3.3V.

[Insertar imagen del amplificador de audio digital PAM-8403]

Buzzer de Sonido: El buzzer se utiliza para generar sonidos audibles. Se puede utilizar para emitir señales acústicas o reproducir melodías simples. Es necesario establecer la conexión adecuada entre el buzzer y la PAM8403 para controlar los sonidos generados.

[Insertar imagen del buzzer de sonido]

Estas imágenes y explicaciones proporcionan una visión general de cada componente y su función en relación con la placa ESP32. El conocimiento detallado de las conexiones y características individuales de cada componente nos permitirá realizar un diseño preciso y eficiente del sistema posteriormente en la etapa de elaboración de la PCB.

A través de este enlace te diriges a la carpeta que contiene la programación de cada componente por separado: [LINK A CARPETA →](https://github.com/JU4NR0D/Optimus-Plant/tree/main/%F0%9F%AA%B4%202.%20PROCESO%20DE%20DISE%C3%91O/2.%20%F0%9F%8C%BFPROGRAMAS)

O puedes ver el proceso de elaboración de la PCB en este otro link: [LINK PCB→](https://github.com/JU4NR0D/Optimus-Plant/blob/main/%F0%9F%AA%B4%202.%20PROCESO%20DE%20DISE%C3%91O/README.md)
