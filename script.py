import cv2
import os

# Um vídeo é uma sequência de imagens exibidas a uma taxa de quadros por segundo.
# Cada quadro é uma matriz de pixels, onde cada pixel possui 3 canais de cor ordenados como BGR no OpenCV

# Prepara a pasta para o Desafio Extra 1
os.makedirs("frames", exist_ok=True)

cap = cv2.VideoCapture("video_exemplo.mp4")

# Desafio Extra 3: Captura o FPS do vídeo para o cálculo de duração
fps = cap.get(cv2.CAP_PROP_FPS)

quadros = []
i = 0

while True:
    ret, quadro = cap.read()
    if not ret:
        break
    
    quadros.append(quadro)
    
    # Desafio Extra 1: Salva todos os quadros na pasta frames/
    cv2.imwrite(f"frames/{i:03d}.jpg", quadro)
    i += 1

cap.release()

total_lidos = len(quadros)
print(f"Total de quadros: {total_lidos}") # Requisito: imprimir total

if total_lidos > 0:
    # Desafio Extra 3: Duração do vídeo em segundos
    duracao = total_lidos / fps if fps > 0 else 0
    print(f"Duração do vídeo: {duracao:.2f} segundos")

    # Requisito: Salvar o quadro do meio
    indice_meio = total_lidos // 2
    quadro_meio = quadros[indice_meio]
    cv2.imwrite("frame_meio.jpg", quadro_meio)
    print(f"Salvo frame_meio.jpg (referente ao quadro {indice_meio})")

    # Desafio Extra 2: Converter quadro do meio para cinza e detectar bordas
    cinza = cv2.cvtColor(quadro_meio, cv2.COLOR_BGR2GRAY)
    bordas = cv2.Canny(cinza, threshold1=50, threshold2=150)
    cv2.imwrite("frame_meio_bordas.jpg", bordas)
    print("Salvo frame_meio_bordas.jpg com filtro Canny aplicado")