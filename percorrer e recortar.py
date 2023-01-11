import os
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image_files = os.listdir('./fotos')
print('1')
savedir = 'fotoscorte/'
for file in image_files:
    print('2')
    image = cv2.imread('./fotos/{}'.format(file))
    print('3')
    print(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print('4')

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        face_image = image[y:y+h, x:x+w]
        cv2.imwrite(savedir + 'face_{}.jpg'.format(file), face_image)