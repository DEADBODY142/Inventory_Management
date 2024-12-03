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
    # Read frame continuously
    ret, frame = cap.read()
    
    if ret:
        # Display the frame in a window
        cv2.imshow('Press S to take snapshot', frame)
        
        # Check for 's' key press
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            # Save the frame as an image file in img folder
            timestamp = datetime.now().strftime('%H%M%S')
            filename = f'images/capture_image/snapshot_{timestamp}.jpg'
            
            # Save the frame as an image file in img folder
            cv2.imwrite(filename, frame)
            print(f"Snapshot saved as '{filename}'.")
            break
        # if cv2.getWindowProperty('Press S to take snapshot', cv2.WND_PROP_VISIBLE) < 1:
        #     break
        
        # Break the loop if 'q' is pressed
        # elif key == ord('q'):
        #     break
    else:
        print("Error: Unable to capture image.")
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
