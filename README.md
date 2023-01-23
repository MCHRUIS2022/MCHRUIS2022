
# MCHRUIS2022
Este proyecto de pregrado ha sido realizado con el fin de generar una alternativa que facilite el desarrollo de un Docente o usuario común en una presentación realizada a una clase o un público específico. Todo esto mediante el desarollo de un algoritmo de aprendizaje profundo.

## Características
- MODO MOUSE
- MODO RECONOCIMIENTO DE GESTOS

## Gestos *(MODO MOUSE)*
| Click Izquierdo | Click Derecho | Mover Mouse | No Seguimiento |
| --- | --- | --- | --- |
| <img src="images/click_izquierdo.png" width="300" height="300"> | <img src="images/click_derecho.png" width="300" height="300"> | <img src="images/mover_mouse.png" width="300" height="300"> | <img src="images/no_seguimiento.png" width="300" height="300"> |

| Desplazarse arriba | Desplazarse abajo | Cambiar a modo RECONOCIMIENTO | Salir de MCHR |
| --- | --- | --- | --- |
| <img src="images/up_scroll.png" width="300" height="300"> | <img src="images/down_scroll.png" width="300" height="300"> | <img src="images/cambiar_a _modo_reconocimiento.png" width="300" height="300"> | <img src="images/salir_de_mchr.png" width="300" height="300"> |

## Gestos *(MODO RECONOCIMIENTO)*
| Silencio | Modo Mouse | F5 | ESC |
| --- | --- | --- | --- |
| <img src="images/silencio2.png" width="300" height="300"> | <img src="images/OK.png" width="300" height="300"> | <img src="images/ONE.png" width="300" height="300"> | <img src="images/DISLIKE.png" width="300" height="300"> |

| DERECHA | IZQUIERDA | ON/OFF RECONOCIMIENTO |
| --- | --- | --- | 
| <img src="images/FIST.png" width="300" height="300"> | <img src="images/peace.png" width="300" height="300"> | <img src="images/LIKE.png" width="300" height="300"> | 






## Guía de instalación (Windows)
Para la instalación es necesario acceder al siguiente link de descarga: https://drive.google.com/file/d/10nLCzaP3M0eqhLqYXXXX_C5h6OnG6Z8yjWu/view?usp=sharing
Dentro de este encontrarás un archivo llamado MCHR.zip este contiene todos los archivos necesarios para la ejecución del mismo, sin embargo, es necesario instalar las librerías necesarias para el correcto funcionamiento de “MCHR”, para instalar los requerimientos mínimos sigue los siguientes pasos:

1. Instala Python 3.10.7. Para esto dirígete al siguiente enlace: https://www.python.org/downloads/release/python-3107/ . En la instalación de Python no olvides marcar la siguiente casilla para agregar la ruta de instalación de Python 3.10 a la variable de entorno PATH del sistema. Esto permite ejecutar el intérprete de Python desde cualquier lugar en la línea de comandos sin tener que especificar la ruta completa al ejecutable. También permite que otros programas utilicen las librerías de Python instaladas en su sistema. Luego puedes continuar con una instalación normal de Python con el botón “Install Now”.
<img src="images/pythonsetup.png" width="300" height="200">

2. Abre “Símbolo del sistema” ó “CMD”, de esta manera mediante el administrador de paquetes de Python “pip” instalaremos las librerías necesarias para la ejecución de MCHR, entonces hay que escribir cada una de las siguientes líneas en el símbolo del sistema:

```python 
pip install PyQt5
```
```python 
pip install mediapipe
```
```python 
pip install tensorflow
```
```python 
pip install opencv-python
```
```python 
pip install pynput
```
```python 
pip install pyautogui
```

## Licencia
Incluye la licencia bajo la cual se distribuye tu aplicación (por ejemplo, MIT License)

## Contribuciones
Si deseas contribuir al desarrollo de esta aplicación, sigue estas instrucciones:
1. Haz un fork del repositorio.
2. Crea una rama para las modificaciones que desees hacer.
3. Haz un pull request.

