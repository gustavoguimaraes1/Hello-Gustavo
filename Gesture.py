import cv2
import mediapipe as mp

# MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Desenho
mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    # BGR -> RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detectar mãos
    results = hands.process(img_rgb)

    # Se encontrou mão
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            # Desenha pontos da mão
            mp_draw.draw_landmarks(
                img,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    cv2.imshow("Gestor de Gestos", img)

    # ESC fecha
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
