import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from face_detection import detect_faces

# Initialize the main application window with a title.
root = tk.Tk()
root.title("Face Detection GUI")

# Label for displaying video frames.
label = ttk.Label(root)
label.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E))

# Video capture object for the webcam.
cap = cv2.VideoCapture(0)
current_color = (255, 0, 0) # Default color Blue

def submit_name():
    """ Fetch the name from the entry widget and update the greeting label. """
    user_name = name_entry.get()
    name_label.config(text=f"Hello, {user_name}!")

# Entry widget for user to input their name.
name_entry = ttk.Entry(root, width=20)
name_entry.grid(row=1, column=0, padx=10, pady=10)

# Button to submit the name, triggering the greeting update.
submit_btn = ttk.Button(root, text="Submit", command=submit_name)
submit_btn.grid(row=1, column=1, padx=10, pady=10)

# Label to display a greeting with the user's name.
name_label = ttk.Label(root, text="Please enter your name above.")
name_label.grid(row=2, column=0, columnspan=2, pady=10)

def show_frames():
    """ 
    Capture frame-by-frame from the camera, detect faces, and update the GUI. 
    """
    ret, frame = cap.read()
    if ret:
        # Convert color to RGB (from BGR), process it, and convert it to a format that Tkinter can use.
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = detect_faces(frame, color=current_color)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
    label.after(20, show_frames)  # Schedule the next frame update.

def start_video():
    """ Start video stream. """
    show_frames()

def stop_video():
    """ Stop video stream and quit the application. """
    cap.release()
    root.quit()

def change_color(new_color):
    """ 
    Change the color of the face detection rectangle based on user selection. 
    
    Parameters:
    - new_color: A string representing the color to be used for drawing rectangles. 
    
    """
    global current_color
    color_dict = {
        "Blue": (255, 0, 0),  # BGR for blue
        "Green": (0, 255, 0),  # BGR for green
        "Red": (0, 0, 255),    # BGR for red
        "Yellow": (0, 255, 255) # BGR for yellow
    }
    current_color = color_dict[new_color]

# Dropdown menu for selecting the rectangle color.
color_var = tk.StringVar(root)
color_var.set("Blue")  # Default selection
color_menu = ttk.OptionMenu(root, color_var, "Blue", "Red", "Green", "Yellow", command=change_color)
color_menu.grid(row=3, column=0, columnspan=2, pady=10)

# Buttons to start and stop the video stream.
btn_start = ttk.Button(root, text="Start Camera", command=start_video)
btn_start.grid(row=4, column=0, pady=10, padx=5)

btn_stop = ttk.Button(root, text="Stop Camera", command=stop_video)
btn_stop.grid(row=4, column=1, pady=10, padx=5)

root.mainloop()
