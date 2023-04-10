
# :cyclone: MCHRUIS2022 :cyclone:
MCHR, es una aplicación orientada a generar una alternativa a la manipulación del ordenador, esto mediante un algoritmo de aprendizaje profundo encargado del reconocimiento de gestos y a un modelo ya entrenado encargado de la esqueletización de la mano de la librería mediapipe. Estos en conjunto nos permiten generar una alternativa para controlar del mouse y de más funciones necesarias al momento de realizar una presentación o hacer un uso cotidiano del ordenador.

## :star: Requisitos mínimos :star:
*	**Tener una Web Cam o dispositivo de salida de video.**
*	**Python 3.10.7**
*	**PyQt5**
*	**Mediapipe** 
*	**Tensorflow** 
* **OpenCV** 
*	**Pynput** 
*	**Pyautogui** 
*	**Winsound** 
*	**WinRaR**
* **YOLOv8**
## :star: Recomendaciones :star:
*	**Encontrarse a una distancia de la cámara de 0.6 [metros].**
*	**Contar con una correcta iluminación que no genere ruido en la imagen, esto para que la inferencia sea rápida y efectiva al momento de requerir una acción**
*	**Si es posible evitar fondos de enfoque con mucho ruido (personas de fondo distintas al expositor o usuario, destellos de luz, etc)**


## :milky_way: MODOS DE OPERACIÓN :milky_way:
* **MODO MOUSE**
* **MODO RECONOCIMIENTO DE GESTOS**

## :hand: Gestos *(MODO MOUSE)* 👊
| Click Izquierdo | Click Derecho | Mover Mouse | No Seguimiento |
| --- | --- | --- | --- |
| <img src="images/click_izquierdo.png" width="300" height="200"> | <img src="images/click_derecho.png" width="300" height="200"> | <img src="images/mover_mouse.png" width="300" height="200"> | <img src="images/no_seguimiento.png" width="300" height="200"> |

| Desplazarse arriba | Desplazarse abajo | Cambiar a modo RECONOCIMIENTO | DETENER MCHR |
| --- | --- | --- | --- |
| <img src="images/up_scroll.png" width="300" height="200"> | <img src="images/down_scroll.png" width="300" height="200"> | <img src="images/cambiar_a _modo_reconocimiento.png" width="300" height="200"> | <img src="images/salir_de_mchr.png" width="300" height="200"> |

## 🤙 Gestos *(MODO RECONOCIMIENTO)* 👌
| Silencio | Modo Mouse | F5 | ESC |
| --- | --- | --- | --- |
| <img src="images/MUTE.png" width="300" height="200"> | <img src="images/MODO_MOUSE.png" width="300" height="200"> | <img src="images/F5.png" width="300" height="200"> | <img src="images/ESC.png" width="300" height="200"> |

| DERECHA | IZQUIERDA | ON/OFF RECONOCIMIENTO | DETENER MCHR | 
| --- | --- | --- | --- |
| <img src="images/DERECHA.png" width="300" height="200"> | <img src="images/IZQUIERDA.png" width="300" height="200"> | <img src="images/ON_OFF_RECOGNITION.png" width="300" height="200"> |  <img src="images/DETENER_MCHR.png" width="300" height="200"> |





## 👷 Guía de instalación (Windows) 🔧
Para la instalación es necesario acceder al siguiente link de descarga: https://drive.google.com/drive/folders/1uhSPw3eL6WwMeCyOUweMhpeVK0je6cqL?usp=sharing

Dentro de este encontrarás un archivo llamado MCHR.zip este contiene todos los archivos necesarios para la ejecución del mismo, sin embargo, es necesario instalar las librerías necesarias para el correcto funcionamiento de **“MCHR”**, para instalar los requerimientos mínimos sigue los siguientes pasos:

1. **Instala Python 3.10.7.** Para esto dirígete al siguiente enlace: 
https://www.python.org/downloads/release/python-3107/ 

En la instalación de Python no olvides marcar la siguiente casilla para agregar la ruta de instalación de **Python 3.10** a la variable de entorno PATH del sistema. Esto permite ejecutar el intérprete de Python desde cualquier lugar en la línea de comandos sin tener que especificar la ruta completa al ejecutable. También permite que otros programas utilicen las librerías de Python instaladas en su sistema. Luego puedes continuar con una instalación normal de Python con el botón **“Install Now”**.

<img src="images/pythonsetup.png" width="300" height="200">


2. Es necesario entonces descomprimir el archivo **MCHR.zip** (Recomendación **WinRaR** para extraer el paquete) dentro de cualquier carpeta o directorio (Para mayor facilidad sugerimos el **Escritorio**).

3. Es posible instalar cada una de las dependencias de manera automática y con las versiones usadas al momento de desarrollar el proyecto, para esto simplemente ejecuta el archivo **Requirements_Setup.bat**.


![gif1cmd](images/INSTALACION.gif)


## 🏃 Como ejecutar la aplicación 🏃

En la carpeta de instalación de MCHR, se debe ejecutar el archivo “MCHR.bat” y si cumplimos con todos los requisitos deberíamos observar una pantalla de carga y el primer plano de la aplicación como podemos ver a continuación.

| Pantalla de carga |  Primera ventana de MCHR |
| --- | --- |
| <img src="images/pp1.png" width="300" height="200"> | <img src="images/pppp2.png" width="300" height="200"> |
 
 ## 🔧 Herramientas de la interfaz 🔧
 
 En la interfaz de MCHR observaremos información importante que debemos comprender para hacer un correcto uso de la aplicación.
 

| Primera Ventana | 
| --- |
| <img src="images/ppprimera_ventana.png" width="500" height="400"> |
 
* Enumerado como **"1"** en la imagen anterior, tenemos la descripción corta sobre la herramienta y las demás imágenes.
* Enumerado como **“2”** en la imagen anterior, tenemos los gestos del **Modo Reconocimiento de gestos**, estos buscan dar una vista previa al usuario sobre qué tipo de gestos fueron implementados.
* Enumerado como **“3”** en la imagen anterior, tenemos una vista previa del **Modo Mouse**, el cual está encargado de hacer el seguimiento de los puntos de la mano que luego serán claves para el movimiento del cursor y demás interacciones del mismo.
* Enumerado como **“4”** en la imagen anterior, tenemos **Siguiente**. Este es un botón encargado de dirigir al usuario a la **Segunda Ventana**.


| Segunda Ventana | 
| --- |
| <img src="images/ssegunda_ventana.png" width="500" height="400"> |
 
* Enumerado como **“1”** en la imagen anterior, tenemos la condición de funcionamiento de **MCHR**, la cual nos indica que para un correcto funcionamiento y reconocimiento deberíamos encontrarnos a **0.6 Metros** de distancia de nuestra cámara o dispositivo de salida de video.
* Enumerado como **“2”** en la imagen anterior, tenemos los gestos implementados en el **Modo Mouse**, con una descripción corta de su funcionamiento.
* Enumerado como **“3”** en la imagen anterior, tenemos los gestos implementados en el **Modo Reconocimiento**, con una descripción corta de su funcionamiento.
* Enumerado como **“4”** en la imagen anterior, tenemos el botón **Iniciar** el cual está encargado de iniciar el programa que permitirá manipular el mouse y demás atajos de nuestro ordenador.
 
 
## Funciones MCHR
Las funciones del **Modo Mouse** y el **Modo Reconocimiento**, se encuentran descritas en las **páginas 8-13** del **Manual Guía de la aplicación**.

## Referencias 
Link del DataSet usado: 
[HaGRID DataSet](https://www.kaggle.com/datasets/innominate817/hagrid-classification-512p?select=hagrid-classification-512p) 
[DataSet para entrenamiento YOLOV8](https://drive.google.com/drive/folders/1TSrakKjMMILNfUa8KeRd8A4_6WvjCv60?usp=sharing) 

## Manual Guía **(PDF)**:  
[Click aquí para ver el Manual en PDF](images/manual_de_uso_mchr.pdf)


## Modelos entrenados en **Colab**
Modelo 1 : [ResNet50](https://colab.research.google.com/drive/1CSXaRBbjOonK1VZMjUEiAZDQaI2VLxHY?usp=sharing)  
Modelo 2 : [MobilNetv1](https://colab.research.google.com/drive/1izLoCM4b4xdJvLr8L9ct0IoGpIJ51Xx9?usp=sharing)  
Modelo 3 : [Custom](https://colab.research.google.com/drive/1yMgmy6W3P7BwWbJgVUpwga_rzLeVMrqY?usp=sharing)  
Modelo 4 : [YoloV8](https://colab.research.google.com/drive/11JK3w8RwnQeheKwCwyf9dzJMxid7iTQk?usp=sharing)











