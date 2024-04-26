import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_faces(img, color=(255, 0 ,0)): #Default color is blue
    """
    Detect faces in an image, convert the image to grayscale to improve detection efficiency,
    and draw rectangles around detected faces using a specified color.
    
    Parameters:
    - img: The original image in which faces are to be detected.
    - color: The color of the rectangle as a tuple (B, G, R).
    
    Returns:
    - The original image with rectangles drawn around detected faces.
    """
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    # Detect faces within the grayscale image
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
    return img
