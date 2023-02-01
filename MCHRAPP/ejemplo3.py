
import numpy as np
import tensorflow as tf
import cv2
import time
from pynput import mouse, keyboard
from pynput.keyboard import Key, Controller
import winsound

def inf():
    keyboard = Controller()

    interpreter = tf.lite.Interpreter(model_path='ResNet_Model_Fin.tflite')

    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    print(input_details)
    print(output_details)

    height = input_details[0]['shape'][1]
    width = input_details[0]['shape'][2]

    print(height)
    print(width)

    output1 = np.squeeze(interpreter.get_tensor(output_details[0]['index']))
    print("output = ", output1)
    print("output_shape = ", output1.shape[-1])
    prom = []
    cap = cv2.VideoCapture(0)
    a = []  # lista para definir que gesto es el más probable
    b = []  # lista para saber si se esta realizando verdaderamente un gesto

    t = 0 # esta variable sirve para clasificar el gesto
    h = 0 # número maximo de muestras para escoger una inferencia
    y = False # sirve para determinar en que estado esta el algoritmo (on,off)
    i = 0 #para definir si se detiene el proceso
    w = 0 #sirve para determinar si quiere terminar el proceso definitivamente
    z = 0
    while True:

        sucess, img1 = cap.read()

        img2 = cv2.resize(img1.copy(), (224, 224), interpolation=cv2.INTER_CUBIC)
        o = cv2.resize(img1.copy(), (300,300), interpolation=cv2.INTER_CUBIC)
        p5 = o.copy()
        p6 = o.copy()
        # Redimensionamos las fotos
        x1 = np.array(img2).reshape(224, 224, 3)  # Convertimos la imagen a una matriz
        x = np.expand_dims(x1, axis=0)  # Agregamos nuevo eje
        x = np.float32(x)
        interpreter.set_tensor(input_details[0]['index'], x)
        interpreter.invoke()
        output = np.squeeze(interpreter.get_tensor(output_details[0]['index']))
        out = interpreter.get_tensor(output_details[0]['index'])
        # print("probabilidades = ", output)
        # print("salida  2 = ",output[2])
        if output[np.argmax(output)] >= 0.8:
            salida = np.argmax(out)
        else:
            salida = 10
            # print("no esta haciendo ningun gesto")
        # print("salida = ", salida)

        b.append(salida)
        print('b = ', b)
        print('Y1 = ', y)

        if h == 10:
            h = 0
            z = max(b, key=b.count)
            # print('lo más probable = ', z)
            if z == 4:
                winsound.Beep(500, 500)
                cv2.destroyAllWindows()
                y = True

            b.clear()

        print('Y2 = ', y)

        texto5 = "ON"
        texto6 = "OFF"
        ubicacion = (0,15)
        font = cv2.FONT_ITALIC
        tamañoLetra = 0.5
        colorLetra = (0, 94, 255)
        grosorLetra = 2

        # Escribir texto
        cv2.putText(p5, texto5, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)
        cv2.putText(p6, texto6, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)
        if y == True:
            print("ENTRO AL WHILE")
            a.append(salida)
            print("a = ",a)
            if t == 10:

                print("ENTRO AL BUCLE")


                t = 0
                l = max(a, key=a.count)
                # print('lo más probable = ',l)
                if l == 5:
                    winsound.Beep(500, 500)
                    cv2.destroyAllWindows()
                    keyboard.press(Key.media_volume_mute)
                    keyboard.release(Key.media_volume_mute)
                if l == 7:
                    winsound.Beep(500, 500)
                    cv2.destroyAllWindows()
                    keyboard.press(Key.f5)
                    keyboard.release(Key.f5)
                if l == 2:
                    winsound.Beep(500, 500)
                    cv2.destroyAllWindows()
                    keyboard.press(Key.right)
                    keyboard.release(Key.right)
                if l == 8:
                    winsound.Beep(500, 500)
                    cv2.destroyAllWindows()
                    keyboard.press(Key.left)
                    keyboard.release(Key.left)
                if l == 6:
                    winsound.Beep(500, 500)
                    cv2.destroyAllWindows()
                    break
                if l == 4:
                    winsound.Beep(500, 500)
                    cv2.destroyAllWindows()
                    y = False
                if l == 3:
                    winsound.Beep(500, 500)
                    cv2.destroyAllWindows()
                    w = 1
                if l == 1:
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
        k = cv2.waitKey(10) & 0xFF
        if k == 27 or w == 1:
            cap.release()
            cv2.destroyAllWindows()
            break
    return w

