import cv2 
# from pyezviz import EzvizClient, EzvizCamera 
# import sys

# Replace with your camera's IP address, username and password
camera_url = "rtsp://admin:CIPVVI@192.168.1.9/h264_stream"

# def main():
#     client = EzvizClient("admin", "CIPVVI", "eu")
#     try:
#         client.login()
#         camera = EzvizCamera(client, "camera_serial_number")
#         print(camera.status())
#         camera.move('left')
#         camera.move('left')
#         camera.move('up')
#         camera.move('down')
#         camera.move('up')
#         camera.move('down')
#         print("Camera loaded")
#     except BaseException as exp:
#         print(exp)
#         return 1
#     finally:
#         client.close_session()

# Open video capture using camera URL
cap = cv2.VideoCapture(camera_url)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is read correctly
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break

    # Display the resulting frame
    cv2.imshow('Ezviz Camera Feed', frame)

    # main()

    # Exit if 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release capture and close all windows
cap.release()
cv2.destroyAllWindows()





