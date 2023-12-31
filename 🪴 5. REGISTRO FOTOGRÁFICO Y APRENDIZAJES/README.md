# Retos del proyecto

En relación al proyecto, es importante destacar que la perfección no se logró en su primer intento. Surgieron diversos ajustes y cambios que fueron necesarios para llevarlo a cabo exitosamente. Sin embargo, estos desafíos fueron abordados con gran interés y compromiso por parte del equipo y el profesor Jhonny Cubides.

Cada uno de los ajustes y cambios realizados durante el desarrollo del proyecto nos dejó valiosas enseñanzas. Estas lecciones adquiridas resultan especialmente relevantes ya que nos brindan un conocimiento sólido sobre cómo enfrentar y superar desafíos similares en futuros proyectos.

## Reto #1: Elección de Sensor Resistivo de Humedad, SIN PAM8403

La ayuda y orientación recibida en la clase de Taller de Electrónica resultó crucial para evitar que nuestra caja negra quedara en un estado insatisfactorio. Inicialmente, estábamos utilizando un modelo anterior que carecía de la tecnología de amplificador de sonido y no habíamos seleccionado adecuadamente los componentes para el sensor de humedad del suelo.

Gracias a las instrucciones y consejos proporcionados en el taller, pudimos rectificar esta situación. Implementamos un nuevo diseño que incluía un amplificador de sonido, lo cual mejoró significativamente la calidad y potencia del sonido emitido. Además, realizamos una selección más acertada de componentes y optamos por un sensor de humedad del suelo capacitivo, que resultó ser más duradero y ofrecía un precio similar al anterior.

IMAGEN DE DIAGRAMA DE CAJA NEGRA OBSOLETO:

![SENSOR_DE_TEMPERATURA](https://github.com/JU4NR0D/Optimus-Plant/assets/136518038/40ecc0da-0da0-4ac8-a843-f1d1065c57ea)


## Reto #2: Precio Pantallas OLED

Inicialmente, teníamos la intención de incorporar una pantalla de gran tamaño en nuestro proyecto para poder mostrar claramente las necesidades de la planta, incluso desde una distancia prudente. Sin embargo, nos encontramos con un obstáculo inesperado cuando descubrimos que el costo de adquirir una pantalla de tan solo 2.42 pulgadas superaba los $100.000 COP, lo cual excedía nuestro presupuesto establecido para la inversión.

Ante esta situación, nos vimos obligados a replantear nuestra estrategia y buscar una alternativa más económica y viable. Decidimos explorar otras opciones de pantalla que se ajustaran a nuestras necesidades sin comprometer el presupuesto del proyecto.

Aunque la idea inicial de tener una pantalla grande era atractiva, entendimos que la funcionalidad y eficacia del proyecto no dependían exclusivamente del tamaño de la pantalla, sino de la información clara y precisa que se pudiera mostrar. Por lo tanto, comenzamos a evaluar otras alternativas de pantallas más pequeñas y asequibles que aún pudieran cumplir con los requisitos de visibilidad y legibilidad necesarios.

![image](https://github.com/JU4NR0D/Optimus-Plant/assets/136518038/0ff1a4df-6372-48b2-9428-106293188e8b)

Por lo tanto, nos tuvimos que acomodar al presupuesto, y hacer compra de una pequeña pantalla oled I2C como esta:

![image](https://github.com/JU4NR0D/Optimus-Plant/assets/136518038/9e89bf5f-79eb-47fc-b2ee-079e3c6f41a5)


## Reto #3: ESP32 de mala calidad

Lamentablemente, nos encontramos con contratiempos relacionados con la ESP32 que habíamos adquirido inicialmente en Chapinero a un precio exorbitante en comparación con el mercado ($52.000 COP en Marzo de 2023). Para nuestra sorpresa, esta placa resultó ser de baja calidad, presentando deficiencias incluso en la soldadura de los pines.

Afortunadamente, contamos con la ayuda del profesor Jhonny, quien nos brindó su apoyo y conocimientos técnicos para solucionar este problema, logrando corregir los pines mal soldados. Esto nos permitió continuar con el desarrollo del proyecto.

Sin embargo, nuestra mala suerte no terminó ahí. Durante el proceso de programación, el puerto USB de la placa se desprendió, generando nuevamente un inconveniente, que a pesar de nuestros intentos por repararlo utilizando diferentes métodos, lamentablemente resultó ser un caso perdido.

Imagen de ESP ya sin arreglo alguno:
![WhatsApp Image 2023-06-25 at 8 53 00 PM](https://github.com/JU4NR0D/Optimus-Plant/assets/136518038/65c65f8c-d707-4ce1-8858-6ced491c2586)


Estos incidentes nos enseñaron la importancia de investigar y adquirir componentes de calidad, así como la necesidad de contar con soporte técnico confiable. Además, nos recordaron la importancia de tener alternativas y soluciones de respaldo en caso de enfrentar dificultades técnicas imprevistas.

## Reto #4: Manejo de KiCad!

Adaptarnos a este entorno no fue fácil, requirió cometer errores, hacer esquemáticos que se tuvieron que desechar, como este:

![ESQUEMATICO ANTERIOR](https://github.com/JU4NR0D/Optimus-Plant/assets/136518038/a4866e7d-2cb9-49f1-a237-ddcd07b811e9)

Debido a que existían errores como estos (Retroalimentación Ing. Johnny Cubides):

![ESQUEMATICO ANTERIOR CORREGIDO](https://github.com/JU4NR0D/Optimus-Plant/assets/136518038/de52727c-aab5-4361-bc5d-45ea58c97c1b)

Posteriormente con orientación de videos en Youtube y el profesor encargado, se logró realizar esta PCB de manera correcta. (VER SECCIÓN 2.3)


## Reto #5: Correción diseño para imprimir

La impresión en Yahiko fue un proceso interesante, ya que era nuestro primer acercamiento a lo que era el mandar a hacer una PCB. Al hacerlo, nos pidieron archivos gerber con drilling holes y en pdf, sin embargo nuestro primer modelo que enviamos que fue este: [PDF_PCB (1).pdf](https://github.com/JU4NR0D/Optimus-Plant/files/11863805/PDF_PCB.1.pdf), un diseño un tanto diferente a lo que tenemos ahora, que se puede revisar en la carpeta de PCB.

El error con este diseño era que según Yahiko se debía: "Separar la capa de tierra de las pistas por que esta muy unido y quedaria en corto", ayudándonos a prevenir un incidente a futuro. De forma que el nuevo ruteo se encamino a esa contienda de no cruzar por ningún motivo esas pistas, o que queden estrechas.

## Reto más grande!!!

Por motivos casi salidos de una película, la PCB sufrió muchos daños por lo que montar el circuito final en esta fue imposible. Para empezar, se soldó directamente a ella, omitiendo el uso de una base. Además existían muchos daños debidos a la tecnología que no estaba en nuestras manos, por infortunio, tampoco se logró adquirir nuevamente la PCB, a razones de tiempos. Se adjunta imagen de la PCB


![WhatsApp Image 2023-06-28 at 11 31 21 PM](https://github.com/JU4NR0D/Optimus-Plant/assets/136518038/ab6f8664-e695-4c62-94f1-76eba3448b8b)

![pcb broken](https://github.com/JU4NR0D/Optimus-Plant/assets/136518038/48ae58bd-70f1-4996-932a-70d25caa7031)


Lo interesante de esto es que pudimos acercarnos a los laboratorios de mecatronica y experimentar dessoldando los componentes para salvarlos, haciendo uso de distintas máquinas y metiéndonos en este mundo aún más. Con esto, finiquitamos nuestro proyecto. Se aprendieron lecciones invaluables que nos servirán en un futuro.
