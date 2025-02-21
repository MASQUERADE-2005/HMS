from picamera2 import Picamera2, Preview
import time

# Initialize the camera
picam2 = Picamera2()

# Create and configure preview settings
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)

# Start the preview window
picam2.start_preview(Preview.QTGL)  # Use Preview.NULL if no preview is needed

# Start the camera
picam2.start()
time.sleep(2)  # Allow the camera to warm up

# Capture an image and save it
picam2.capture_file("test.jpg")
