import cv2
import mediapipe as mp
import time

# Inicialização do MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# Variáveis para detectar aceno
prev_x = 0
aceno_direcao = None
contador_acenos = 0
ultimo_tempo_aceno = 0
cooldown = 3  # segundos
gesto_detectado = False

# Captura da câmera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Erro ao abrir a câmera!")
    exit()

while True:
    success, frame = cap.read()
    if not success:
        print("Erro ao capturar frame")
        break

    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    h, w, _ = frame.shape
    
    # Resetar a detecção se passou o cooldown
    if time.time() - ultimo_tempo_aceno > cooldown:
        contador_acenos = 0
        gesto_detectado = False
    
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            # Pegando a posição da landmark da palma (ponto 9)
            cx = int(handLms.landmark[9].x * w)
            
            # Inicializa prev_x na primeira execução
            if prev_x == 0:
                prev_x = cx
                continue
                
            # Calcula diferença de posição
            diff = cx - prev_x
            
            # Detecta movimento significativo (>15 pixels)
            if abs(diff) > 15:
                direcao = "direita" if diff > 0 else "esquerda"
                if direcao != aceno_direcao:
                    aceno_direcao = direcao
                    contador_acenos += 1
                    ultimo_tempo_aceno = time.time()
                    print(f"Aceno detectado: {direcao} (Total: {contador_acenos})")
            
            prev_x = cx

    # Verifica se detectou pelo menos 4 mudanças de direção (2 acenos completos)
    if contador_acenos >= 4 and not gesto_detectado:
        gesto_detectado = True
        print("ALERTA: Pedido de ajuda detectado!")
    
    # Mostra informações na tela
    cv2.putText(frame, f"Acenos: {contador_acenos}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    if gesto_detectado:
        cv2.putText(frame, '⚠️ PEDIDO DE AJUDA DETECTADO ⚠️', (30, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    
    # Mostra tempo restante para completar o gesto
    tempo_restante = max(0, cooldown - (time.time() - ultimo_tempo_aceno))
    cv2.putText(frame, f"Tempo: {tempo_restante:.1f}s", (w-150, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Sistema de Alerta por Gesto", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC para sair
        break

cap.release()
cv2.destroyAllWindows()
