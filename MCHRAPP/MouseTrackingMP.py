# importamos las libreríass
import math
import cv2
import mediapipe as mp
import time


# creamos la clase
class hand_detector():
    # inicializamos los parámetros de detección
    def __init__(self, mode=False, maxHands=2, modelC=1, DetectionConfidence=0.75, TrackConfidence=0.75):
        self.mode = mode
        self.maxHands = maxHands
        self.modelC = modelC  # NUEVO PARAMETRO DEL MODELO DE MEDIAPIPE
        self.DetectionConfidence = DetectionConfidence
        self.TrackConfidence = TrackConfidence

        # creamos los objetos que detectan las manos y las dibujan
        self.mpHands = mp.solutions.hands
        self.manos = self.mpHands.Hands(self.mode, self.maxHands, self.modelC, self.DetectionConfidence, self.TrackConfidence)
        self.draw = mp.solutions.drawing_utils
        self.tip = [4, 8, 12, 16, 20]

    # funcion para encontrar las manos
    def FindHands(self, frame, dibujar=True):
        imgcolor = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.manos.process(imgcolor)

        if self.results.multi_hand_landmarks:
            for mano in self.results.multi_hand_landmarks:
                if dibujar:
                    self.draw.draw_landmarks(frame, mano, self.mpHands.HAND_CONNECTIONS)  # DIBUJAMOS LAS CONEXIONES DE LOS PUNTOS
        return frame

    # funcion para encontrar la posición
    def FindPosition(self, frame, ManoNum=0, dibujar=True):
        x_list = []
        y_list = []
        bbox = []
        self.list = []
        if self.results.multi_hand_landmarks:
            miMano = self.results.multi_hand_landmarks[ManoNum]
            for id, lm in enumerate(miMano.landmark):
                highh, widthh, c = frame.shape  # extraemos las dimensiones de los fps
                sx, sy = int(lm.x * widthh), int(lm.y * highh)  # transformando la información a pixeles
                x_list.append(sx)
                y_list.append(sy)
                self.list.append([id, sx, sy])
                if dibujar:
                    cv2.circle(frame, (sx, sy), 5, (0, 0, 0), cv2.FILLED)  # dibujamos un círculo

            xmin, xmax = min(x_list), max(x_list)
            ymin, ymax = min(y_list), max(y_list)
            bbox = xmin, ymin, xmax, ymax
            if dibujar:
                cv2.rectangle(frame, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20), (0, 255, 0), 2)
        return self.list, bbox

    # funcion para detectar Fingers arriba
    def UpFingerDetector(self):
        Fingers = []
        if self.list[self.tip[0]][1] > self.list[self.tip[0] - 1][1]:
            Fingers.append(1)
        else:
            Fingers.append(0)

        for id in range(1, 5):
            if self.list[self.tip[id]][2] < self.list[self.tip[id] - 2][2]:
                Fingers.append(1)
            else:
                Fingers.append(0)

        return Fingers

    # funcion para detectar la distancia entre Fingers
    def DistanceCalculator(self, p1, p2, frame, dibujar=True, r=10, t=3):
        x1, y1 = self.list[p1][1:]
        x2, y2 = self.list[p2][1:]
        sx, sy = (x1 + x2) // 2, (y1 + y2) // 2
        if dibujar:
            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), t)
            cv2.circle(frame, (x1, y1), r, (0, 0, 255), cv2.FILLED)
            cv2.circle(frame, (x2, y2), r, (0, 0, 255), cv2.FILLED)
            cv2.circle(frame, (sx, sy), r, (0, 0, 255), cv2.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)

        return length, frame, [x1, y1, x2, y2, sx, sy]


# funcion  principal
def main():
    xtime = 0
    vtime = 0

    # leemos cámara web
    cap = cv2.VideoCapture(0)
    # creamos el objeto
    Detector = hand_detector()  # ejecutamos la funcion hand_detector
    # realizamos la detección de las manos

    while True:
        ret, frame = cap.read()
        # una vez que obtenemos la imagen la enviamos
        frame = Detector.FindHands(frame)
        list, bbox = Detector.FindPosition(frame)
        if len(list) != 0:
            print(list[4])
        # mostramos los fps
        vtime = time.time()
        fps = 1 / (vtime - xtime)
        xtime = vtime

        cv2.putText(frame, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Manos", frame)
        k = cv2.waitKey(1)

        if k == 27:  # si le damos a escape cerramos todo
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()


