import cv2

vidcap = cv2.VideoCapture('css.mp4')

success, image = vidcap.read()
count = 0

size = (1280, 720)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('output.mp4', fourcc, 60.0, size)


while success:
    if count % 12 == 0:
        video.write(image)
    success, image = vidcap.read()
    count += 1

video.release()

