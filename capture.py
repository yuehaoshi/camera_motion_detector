import cv2, time

# Create a video. 0 means the default laptop camera
video = cv2.VideoCapture(0)

a = 1
# Loop through frames in the video
while True:
    a += 1
    check, frame = video.read()
    print(check)
    print(frame)

    # Convert RGB frame to gray scale for each frame in the video
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # time.sleep(3)
    cv2.imshow("Capturing", gray)

    # Each frame will be shown in 100ms (0.1s). If this parameter is 0, then it means the frame will wait until the user print a key in keyboard.
    key = cv2.waitKey(100)

    # Press q in keyboard and the while loop will be broken (frame not continue showing)
    if key == ord('q'):
        break
print(a) # Count the number of frames
video.release()
cv2.destroyAllWindows