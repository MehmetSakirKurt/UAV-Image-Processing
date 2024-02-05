import cv2
from pyzbar.pyzbar import decode

# QR kodunu okuyan fonksiyon
def read_qr_code(frame):
    decoded_objects = decode(frame)
    for obj in decoded_objects:
        # QR kodunun içeriğini ve konumunu yazdır
        print("QR Code Detected:", obj.data.decode())
        return True
    return False

# Video dosyasının yolu
video_path = 'drone.mp4'  # Buraya video dosyasının yolunu girin

# Video akışını başlat
cap = cv2.VideoCapture(video_path)

qr_code_detected = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Eğer QR kodu henüz algılanmadıysa, oku
    if not qr_code_detected:
        qr_code_detected = read_qr_code(frame)

    # Videoyu göster
    cv2.imshow('QR Code Reader', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Video akışını serbest bırak ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()
