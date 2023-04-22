import numpy as np
import cv2
from pynput.keyboard import Key, Controller
import winsound
from ultralytics import YOLO
import time
def inf():
    keyboard = Controller()
    model = YOLO("bestcolab3dataset.pt")
    cap = cv2.VideoCapture(0)

    class BreakAll(Exception):
        pass

    a = []  # lista para definir que gesto es el más probable
    b = []  # lista para saber si se esta realizando verdaderamente un gesto

    t = 0 # esta variable sirve para clasificar el gesto
    h = 0 # número maximo de muestras para escoger una inferencia
    y = False # sirve para determinar en que estado esta el algoritmo (on,off)
    i = 0 #para definir si se detiene el proceso
    w = 0 #sirve para determinar si quiere terminar el proceso definitivamente
    z = 0
    while True:

        try:
            sucess, img = cap.read()
            img1 = cv2.resize(img.copy(), (224, 224), interpolation=cv2.INTER_CUBIC)
            p5 = img1.copy()
            p6 = img1.copy()
            x1 = np.array(img1).reshape(224, 224, 3)  # Convertimos la imagen a una matriz
            results = model.predict(source=x1, conf=0.6, show=True)
            texto5 = "ON"
            texto6 = "OFF"
            ubicacion = (0, 15)
            font = cv2.FONT_ITALIC
            tamañoLetra = 0.5
            colorLetra = (0, 94, 255)
            grosorLetra = 2

            # Escribir texto
            cv2.putText(p5, texto5, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)
            cv2.putText(p6, texto6, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)

            for result in results:
                print("clase:", result.boxes.cls)
                for i in result.boxes.cls:
                    x = i.item()
                    k = int(i)
                    b.append(k)
                    print('b = ', b)
                    print('Y1 = ', y)

                    if h == 4:
                        h = 0
                        z = max(b, key=b.count)
                        print('lo más probable = ', z)
                        if z == 3:
                            winsound.Beep(500, 500)
                            time.sleep(0.5)
                            cv2.destroyAllWindows()
                            y = True
                        b.clear()
                        a.clear()
                    print('Y2 = ', y)

                    if y == True:
                        print("ENTRO AL WHILE")
                        a.append(k)
                        print("a = ", a)
                        if t == 4:

                            print("ENTRO AL BUCLE")

                            t = 0
                            l = max(a, key=a.count)
                            # print('lo más probable = ',l)
                            if l == 4:
                                winsound.Beep(500, 500)
                                cv2.destroyAllWindows()
                                keyboard.press(Key.media_volume_mute)
                                keyboard.release(Key.media_volume_mute)
                            if l == 6:
                                winsound.Beep(500, 500)
                                cv2.destroyAllWindows()
                                keyboard.press(Key.f5)
                                keyboard.release(Key.f5)
                            if l == 1:
                                winsound.Beep(500, 500)
                                cv2.destroyAllWindows()
                                keyboard.press(Key.right)
                                keyboard.release(Key.right)
                            if l == 7:
                                winsound.Beep(500, 500)
                                cv2.destroyAllWindows()
                                keyboard.press(Key.left)
                                keyboard.release(Key.left)
                            if l == 5:
                                winsound.Beep(500, 500)
                                cv2.destroyAllWindows()
                                raise BreakAll()
                            if l == 3:
                                winsound.Beep(500, 500)
                                time.sleep(0.5)
                                cv2.destroyAllWindows()
                                y = False
                            if l == 2:
                                winsound.Beep(500, 500)
                                cv2.destroyAllWindows()
                                w = 1
                                raise BreakAll()
                            if l == 0:
                                winsound.Beep(500, 500)
                                keyboard.press(Key.esc)
                                keyboard.release(Key.esc)
                            a.clear()
                            b.clear()
                        t = t + 1
                    h = h + 1

            if y == True:
                cv2.imshow('image', p5)
            if y == False:
                cv2.imshow('image', p6)
        except BreakAll:
            break

    return w


