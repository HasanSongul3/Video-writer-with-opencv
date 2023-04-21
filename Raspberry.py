import cv2

# Video kaydı için gerekli ayarları yapalım
video_kayit = cv2.VideoWriter('video_kaydi.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 25, (640,480))

# Kamera erişimini başlatalım
kamera = cv2.VideoCapture(0)

while True:
    # Görüntüyü kare kare okuyalım
    ret, kare = kamera.read()

    # Eğer kare okunamazsa döngüden çıkalım
    if not ret:
        break

    # Görüntüyü masaüstüne kaydedelim
    video_kayit.write(kare)

    # 'q' tuşuna basıldığında çekmeyi durduralım
    if cv2.waitKey(1) == ord('q'):
        break

# Gerekli temizlik işlemlerini yapalım
kamera.release()
video_kayit.release()
cv2.destroyAllWindows()