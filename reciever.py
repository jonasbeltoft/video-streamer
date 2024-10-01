import cv2

# Address of the incoming TCP stream (replace IP and port as needed)
stream_url = 'tcp://0.0.0.0:5000/?listen'

# Open the video stream using cv2.VideoCapture
cap = cv2.VideoCapture()
cap.open(stream_url)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
cap.set(cv2.CAP_PROP_FPS, 3100)
ret, frame = cap.read()

if not cap.isOpened():
    print("Error: Unable to open the TCP stream.")
    exit()

# Loop to continuously capture frames and display them
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read from the stream.")
        break

    # Display the frame
    cv2.imshow('Webcam Stream', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the display window
cap.release()
cv2.destroyAllWindows()
