import cv2
import os
from datetime import datetime

# Create 'img' directory if it doesn't exist
# os.makedirs('img', exist_ok=True)

# Initialize the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    
    if ret:
        cv2.imshow('Press S to take snapshot', frame)
        
        # Check for 's' key press
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            timestamp = datetime.now().strftime('%H%M%S')
            filename = f'images/capture_image/snapshot_{timestamp}.jpg'
            
            # Save the frame as an image file in img folder
            cv2.imwrite(filename, frame)
            print(f"Snapshot saved as '{filename}'.")
            break
        elif key == ord('q'):
            break
    else:
        print("Error: Unable to capture image.")
        break

cap.release()
cv2.destroyAllWindows()
