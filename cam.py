import cv2

for i in range(10):
    cap = cv2.VideoCapture(i)
    if not cap.read()[0]:
        break
    cap.release()
    print(f"Camera index {i} is available.")
