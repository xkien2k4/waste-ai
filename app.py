import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import os
import time
from ultralytics import YOLO

# =====================
# CONFIG
# =====================
MODEL_PATH = "models/best.pt"
OUTPUT_DIR = "outputs"
CAMERA_ID = 0

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =====================
# LOAD MODEL
# =====================
model = YOLO("runs/detect/train3/weights/best.pt")

# =====================
# MAIN WINDOW
# =====================
root = tk.Tk()
root.title("AI Phân loại rác - YOLOv8")
root.geometry("800x600")

label = tk.Label(root, text="AI PHÂN LOẠI RÁC THẢI", font=("Arial", 18, "bold"))
label.pack(pady=10)

image_label = tk.Label(root)
image_label.pack()

# =====================
# FUNCTIONS
# =====================
def show_image(img_path):
    img = Image.open(img_path)
    img = img.resize((600, 400))
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk

def detect_from_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
    )
    if not file_path:
        return

    img = cv2.imread(file_path)
    results = model(img)
    annotated = results[0].plot()

    output_path = os.path.join(OUTPUT_DIR, "result_file.jpg")
    cv2.imwrite(output_path, annotated)

    show_image(output_path)

def detect_from_camera():
    cap = cv2.VideoCapture(CAMERA_ID)
    if not cap.isOpened():
        messagebox.showerror("Lỗi", "Không mở được camera")
        return

    messagebox.showinfo("Camera",
        "Nhấn C để chụp ảnh\nNhấn ESC để thoát camera"
    )

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Camera", frame)
        key = cv2.waitKey(1)

        if key == 27:  # ESC
            break

        if key == ord('c') or key == ord('C'):
            timestamp = int(time.time())
            output_path = f"{OUTPUT_DIR}/result_camera_{timestamp}.jpg"

            results = model(frame)
            annotated = results[0].plot()

            cv2.imwrite(output_path, annotated)
            show_image(output_path)

    cap.release()
    cv2.destroyAllWindows()

# =====================
# BUTTONS
# =====================
btn_file = tk.Button(
    root, text=" Nhận diện từ ảnh file",
    width=30, height=2,
    command=detect_from_file
)
btn_file.pack(pady=10)

btn_camera = tk.Button(
    root, text=" Nhận diện từ camera",
    width=30, height=2,
    command=detect_from_camera
)
btn_camera.pack(pady=10)

btn_exit = tk.Button(
    root, text=" Thoát",
    width=20, height=2,
    command=root.quit
)
btn_exit.pack(pady=20)

root.mainloop()
