# ----LIBRERIAS----
import cv2  # OPENCV
import numpy as np  # NUMPY
import MouseTrackingMP as MT  # Programa.py que contiene las funciones necesarias para la detección y uso de la mano como cursor
import pynput  # Librería para controlar el mouse/teclado
# Librería PYNPUT
from pynput import mouse, keyboard
from pynput.mouse import Button, Controller  # De pynput importamos el mouse
from pynput.keyboard import Key, Controller  # De pynput importamos el teclado
import pyautogui
import winsound


def handt():
    # ----VARIABLES----
    WidthCam, HighCam = 640, 480  # Tamaño de ventana que se abre en OPENCV
    InteractionRange = 100  # Rango en el que puede interactuar la mano para ser reconocida como mouse
    WidthScreen, HighScreen = pyautogui.size()  # Obtenemos las dimensiones de nuestra pantalla
    smoothing = 5  # Intensidad del smoothingvizado
    T1x, T1y = 0, 0
    T2x, T2y = 0, 0
    i = 0  # ??????????
    z = 0  # Bandera EXIT
    c = 0  # Bandera CHANGE MODE
    # Definimos el mouse mediante la funcion Controller de "pynput"
    mouse_controller = mouse.Controller()  # Importamos el controlador del mouse
    keyboard_controller = keyboard.Controller()  # Importamos el controlador del teclado
    # ----Lectura de cámara con OPENCV----
    cap = cv2.VideoCapture(0)  # Dispositivo 0
    # ----Definiendo el ancho de la pantalla de OPENCV para retorno de imagen al cliente
    cap.set(3, WidthCam)
    cap.set(4, HighCam)
    # ----Declaración del detector (función de SeguimientoManos (MT))----
    Detector = MT.hand_detector(maxHands=1)  # número máximo de manos a reconocer 1 para que no se descontrole
    while True:  # Iniciamos el bucle que se encargará de que todo siga funcionando indefinidamente
        # ----Ahora vamos a encontrar los landmarks de la mano----
        ret, frame = cap.read()  # Leemos la cámara
        frame = Detector.FindHands(frame)  # Capturamos el frame mediante la función FindHands
        lista, bbox = Detector.FindPosition(frame)  # Mostramos las posiciones

        # ----Obtener la punta del dedo indice y corazon---- "p = punta" [4-p pulgar] [8-p índice] [12-p corazón] [16-p anular] [20-p meñique]
        if len(lista) != 0:  # Solo si lista no está vacía
            x1, y1 = lista[8][1:]  # Extraemos las coordenadas del dedo indice
            x2, y2 = lista[12][
                     1:]  # Extraemos las coordenadas del dedo corazon (NO SURE: Esto se hace para luego poder calcular la distancia entre los Fingers que guardemos)
            x0, y0 = lista[3][
                     1:]  # Extraemos las coordenadas de la mitad del dedo pulgar (Para la acción de CLICK IZQUIERDO)
            x4, y4 = lista[16][1:]  # Extraemos las coordenadas del dedo anular
            x5, y5 = lista[20][1:]  # Extraemos las coordenadas del dedo meñique
            x6, y6 = lista[5][
                     1:]  # Extraemos las coordenadas de la base del dedo índice (Para la acción de CLICK IZQUIERDO)
            x7, y7 = lista[4][1:]
            # print(x1,y1,x2,y2)

            # ----Comprobando qué Fingers estan arriba----
            Fingers = Detector.UpFingerDetector()  # Con la función UpFingerDetector de detector, entramos en un bucle que contará 5 posiciones (sensando si alguno de las 5 puntas de los Fingers está arriba)
            # print(Fingers)
            cv2.rectangle(frame, (InteractionRange, InteractionRange), (WidthCam - InteractionRange, HighCam - 2*InteractionRange), (0, 0, 255),
                          2)  # Generamos el InteractionRange que simbolizará los límites del cursor (en color azul estará representado).
            # ----ACTIVAR MODO MOVIMIENTO: Sólo levantar el dedo índice---- (OJO: Siento que falta añadir a la condición cada uno de las otras puntas de los Fingers a fin de que no se mueva el cursor con una señal distinta a la indicada)
            if Fingers[0] == 0 and Fingers[1] == 1 and Fingers[2] == 0 and Fingers[3] == 0 and Fingers[
                4] == 0:  # Si el indice está arriba y el pulgar y corazón abajo se mueve
                # ----EN MOVIMIENTO: conversión a los pixeles de la pantalla----
                x3 = np.interp(x1, (InteractionRange, WidthCam - InteractionRange), (0, WidthScreen))  # (p-índice)Mediante la función interp de numpy, hacemos la conversión a los píxeles de la pantalla
                y3 = np.interp(y1, (InteractionRange, HighCam - 2*InteractionRange), (0, HighScreen))  # (p-corazón)
                # ----smoothingvizando el movimiento del cursor----
                T2x = T1x + (x3 - T1x) / smoothing  # Ubicacion actual = ubicaciónanterior + x3 - Pa dividida en el valor de smoothingvizado
                T2y = T1y + (y3 - T1y) / smoothing

                RealHandMovement = WidthScreen - T2x
                pos = (RealHandMovement, T2y)
                # ----MOVIMIENTO DEL MOUSE----
                mouse_controller.position = pos
                # autopy.mouse.move(WidthScreen - T2x,T2y) #Enviamos las coordenadas de los puntos smoothingvizados (T2x y T2y) a la función de autopy mouse.move (WidthScreen-T2x es necesario que el cursor se mueva correctamente de manera horizontal, ya que la vista del teléfono es en espejo)
                cv2.circle(frame, (x1, y1), 10, (255, 0, 0), cv2.FILLED)  # Dibujamos un circulo más grande en la punta del dedo índice (Lo puse en color azul para notar la diferencia del gesto)
                T1x, T1y = T2x, T2y  # Guardamos la vieja posición del cursor
            # GUÍA PARA CONDICIONALES Fingers[0] == 1 and Fingers[1] == 1 and Fingers[2] == 1 and Fingers[3] == 1 and Fingers[4] == 1
            # ----CLICK IZQUIERDO----
            if Fingers[0] == 1 and Fingers[1] == 1 and Fingers[2] == 0 and Fingers[3] == 0 and Fingers[
                4] == 0:  # Si el indice esta arriba y el pulgar también
                # ----Encontramos la distancia entre los Fingers----
                Length, frame, line = Detector.DistanceCalculator(5, 3, frame)  # Nos entrega la distancia entre el punto 8 y 4 (Dedo índice y pulgar)
                # print(Length)#Impresión de la distancia en pantalla
                # ----Si la distancia es menor a 30 realizamos el click IZQUIERDO----
                if Length < 25:  # Se puede modificar dependiendo de la distancia de la cámara (Funciona bien a 1 [metro])
                    # cv2.circle(frame, (x0,y0), 10, (255,0,0), cv2.FILLED) #Fingers que interactúan se ponen de color rojo
                    # cv2.circle(frame, (x6,y6), 10, (255,0,0), cv2.FILLED) #Fingers que interactúan se ponen de color rojo
                    mouse_controller.click(Button.left,
                                           1)  # 1 click (si queremos doble click solo reemplazamos por: [ , 2 ] )

            # ----CLICK DERECHO----
            if Fingers[0] == 0 and Fingers[1] == 1 and Fingers[2] == 1 and Fingers[3] == 0 and Fingers[
                4] == 0:  # Si el indice esta arriba y el corazon también
                # ----Encontramos la distancia entre los Fingers----
                Length, frame, line = Detector.DistanceCalculator(8, 12, frame)  # Nos entrega la distancia entre el punto 8 y 12 (Dedo índice y corazón)
                # print(Length)#Impresión de la distancia en pantalla
                if Length < 30:
                    # cv2.circle(frame, (line[4],line[5]), 10, (0,255,0), cv2.FILLED) #Fingers que interactúan se ponen de color rojo
                    # ----Si la distancia es menor a 30 realizamos el click DERECHO----
                    mouse_controller.click(Button.right, 1)
            # ----Scroll UP----
            if Fingers[0] == 0 and Fingers[1] == 0 and Fingers[2] == 0 and Fingers[3] == 0 and Fingers[
                4] == 1:  # Solamente se ejecuta si el meñique está arriba y los demás abajo
                cv2.circle(frame, (x5, y5), 10, (255, 0, 0), cv2.FILLED)  # Fingers que interactúan se ponen de color rojo
                mouse_controller.scroll(0,2)  # Si queremos que baje más rapido o más lento basta con poner 1 o 3 respectivamente

            # ----Scroll DOWN----
            if Fingers[0] == 1 and Fingers[1] == 0 and Fingers[2] == 0 and Fingers[3] == 0 and Fingers[
                4] == 0:  # Solamente se ejecuta si el pulgar está arriba y los demás abajo
                cv2.circle(frame, (x7, y7), 10, (255, 0, 0), cv2.FILLED)  # Fingers que interactúan se ponen de color rojo
                mouse_controller.scroll(0,
                                        -2)  # Si queremos que baje más rapido o más lento basta con poner 1 o 3 respectivamente
            # ----DETENER APLICACION ----
            if Fingers[0] == 1 and Fingers[1] == 1 and Fingers[2] == 0 and Fingers[3] == 0 and Fingers[
                4] == 1:  # (SPIDERMAN SIGNAL)Solamente se ejecuta si el pulgar, dedo índice y meñique están arriba y los demás abajo
                winsound.Beep(500, 500)
                z = 1  # Bandera para finalizar
            # ----CAMBIAR A MODO "GESTURE RECOGNITION"----
            if Fingers[0] == 1 and Fingers[1] == 1 and Fingers[2] == 1 and Fingers[3] == 1 and Fingers[
                4] == 1:  # Solamente se ejecuta si la mano está completamente abierta (todos los Fingers en estado HIGH)
                winsound.Beep(500, 500)
                break

        cv2.imshow("MOUSE TRACKER", frame)  # Ventana desplegada con nombre X y cuya imagen se encuentra en frame
        k = cv2.waitKey(1)  # Espera la tecla presionada
        if k == 27 or z == 1:  # Si pulsamos ESC se cierra la ventana, Si las Banderas z o c se ponen en 1 se cierra también la única diferencia es que z está encargada de finalizar completamente mientras que c se refiere al switcheo entre modos
            break
    cap.release()  # Liberamos la cámara (Device X)
    cv2.destroyAllWindows()  # Cerramos lasventanas creadas por OPENCV
    return z


