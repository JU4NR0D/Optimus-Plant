# Esquemático

Después de analizar cuidadosamente las conexiones realizadas durante la etapa de componentes en protoboard, es hora de trasladar esa información al diseño de la PCB. El objetivo principal de este paso es optimizar el espacio utilizado en el proyecto, reduciendo la cantidad de cables y conexiones necesarias entre los diferentes componentes.

Para llevar a cabo esta tarea, hemos utilizado el software KiCad en su versión 7.0.2. Esta potente herramienta nos ha permitido agilizar el proceso de elaboración del esquemático y, posteriormente, transferirlo al editor de placas. En el esquemático, se han establecido todas las conexiones requeridas entre los componentes previamente analizados.

Sin embargo, durante el proceso nos encontramos con un inconveniente. Aunque KiCad es una plataforma de código abierto y de uso gratuito, no contaba con los símbolos necesarios para la mayoría de los componentes utilizados en nuestro proyecto. Ante esta situación, hemos creado una carpeta exclusiva que contiene las huellas necesarias para cada componente.

Así, con todas las piezas en su lugar, presentamos el esquemático final de Optimus Plant. Este diseño refleja de manera clara y precisa todas las conexiones entre los componentes, permitiendo una visión completa del sistema.

![ESQUEMATICO_page-0001](https://github.com/JU4NR0D/Optimus-Plant/assets/136518038/5fede730-80a6-4ae3-b0b5-82f54e3fd4a4)

Una vez finalizado el esquemático, el siguiente paso consiste en asignar las huellas correspondientes a cada uno de los símbolos utilizados. Esto es necesario para asegurar que, al transferir el diseño al editor de placas, todos los componentes aparezcan correctamente junto con las conexiones de ruteo necesarias.

En nuestro caso, también nos encontramos con la situación de que algunas huellas necesarias no estaban disponibles en el software utilizado. Para abordar este problema, creamos una carpeta específica donde almacenamos las huellas faltantes. De esta manera, pudimos asegurarnos de tener todas las huellas necesarias para cada componente utilizado en nuestro proyecto.

Al asignar las huellas a los símbolos y contar con todas las huellas necesarias, estamos listos para proceder a la siguiente etapa: el editor de placas. Aquí podremos visualizar todos los componentes correctamente ubicados y las conexiones de ruteo que se deben realizar para garantizar un diseño preciso y funcional.




# Circuito

Luego de completar el esquemático, procedimos a transferir la net al editor de placas con gran claridad y precisión. Afortunadamente, el proceso de exportación fue exitoso y nos permitió trabajar con la distribución espacial de los componentes de manera adecuada.

El resultado final fue una placa de dimensiones 15 cm x 8 cm, diseñada para albergar todos los componentes necesarios. Esta elección de tamaño nos permitió asegurar un espacio suficiente para cada componente, así como para las conexiones y ruteo de señales de manera eficiente. 

Imagen de la parte frontal de la PCB:

![image](https://github.com/JU4NR0D/Optimus-Plant/assets/136518038/28c0ac60-3c45-4493-a3ff-0c92351f9c18)


Imagen de la parte posterior de la PCB:

![image](https://github.com/JU4NR0D/Optimus-Plant/assets/136518038/55778da0-a3fd-437e-8115-e8ff97dc1ce1)


Se tiene que comprobar que no hayan errores, ejecutando la DRC. Donde se registran 0 errores y 0 avisos, por lo que se considera ya lista para su fabricación:

![image](https://github.com/JU4NR0D/Optimus-Plant/assets/136518038/efc9c122-430d-4093-ae36-faf441e14645)

Entre las características principales de la placa, se destacan:

- Dimensiones: La placa tiene un tamaño de 15 cm x 8 cm, lo cual proporciona un área adecuada para alojar todos los componentes y las conexiones necesarias.
- Distribución eficiente: Gracias a una cuidadosa planificación y distribución del espacio, se logró una disposición óptima de los componentes en la placa, permitiendo un diseño limpio y ordenado.
- Conexiones claras: Las conexiones entre los componentes se realizaron de manera clara y precisa, asegurando un flujo adecuado de la información y minimizando la posibilidad de interferencias o cortocircuitos.
- Ruteo optimizado: Se tuvo en cuenta la ubicación de los componentes y las rutas de señal para lograr un ruteo eficiente, evitando cruces innecesarios y garantizando un buen rendimiento del circuito. Además de garantizar las reglas de ruteo, donde VCC y GND tenían un ancho de vía de 1.6mm y las demás señales tenían 1.2mm

Por último se adjuntan imagenes del visor 3D que nos ofrece el software, para mejorar la comprensión de las conexiones.

![VISOR 3D PCB_page-0001](https://github.com/JU4NR0D/Optimus-Plant/assets/136518038/8a15eac5-a191-4d69-b954-c35d891e5ee6)
![VISOR 3D PCB_page-0002](https://github.com/JU4NR0D/Optimus-Plant/assets/136518038/7456ea90-84a6-437a-bc3a-c5ecb83dbbae)
![VISOR 3D PCB_page-0003](https://github.com/JU4NR0D/Optimus-Plant/assets/136518038/a54b3aa9-bea5-4b4e-bbb0-2d9887d05cd5)

Se manda a fabricar con Yahiko electronica, donde nos pedían los archivos: Gerber con los drilling holes y PDF de la placa, adjuntos en este repositorio.
[Gerber fabricación de placa](https://github.com/JU4NR0D/Optimus-Plant/tree/main/%F0%9F%AA%B4%202.%20PROCESO%20DE%20DISE%C3%91O/3.%20%F0%9F%8C%BFPCB/2.%20%F0%9F%8C%B1%20GERBER%20PARA%20FABRICACI%C3%93N)
[PDF fabricación de placa](https://github.com/JU4NR0D/Optimus-Plant/tree/main/%F0%9F%AA%B4%202.%20PROCESO%20DE%20DISE%C3%91O/3.%20%F0%9F%8C%BFPCB/3.%20%F0%9F%8C%B1%20PDF%20PARA%20FABRICACI%C3%93N)

[YA ESTAMOS LISTOS PARA NUESTRA SIGUIENTE FASE: PROCESO DE UNIFICACIÓN, ACOMPAÑANOS!](https://github.com/JU4NR0D/Optimus-Plant/tree/main/%F0%9F%AA%B4%203.%20PROCESO%20DE%20UNIFICACI%C3%93N)

