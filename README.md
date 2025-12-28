# ♻️ Waste AI – Hệ thống nhận diện & phân loại rác thải bằng YOLOv8

## 📌 Giới thiệu
**Waste AI** là project ứng dụng trí tuệ nhân tạo để **nhận diện và phân loại rác thải** (nhựa, kim loại, giấy, rác hữu cơ, …) dựa trên mô hình **YOLOv8**.

Dự án phục vụ cho:
- Học tập & nghiên cứu AI
- Đồ án môn học
- Demo nhận diện rác thải bằng camera / ảnh

---

## 🧠 Công nghệ sử dụng
- Python 3.10
- YOLOv8 (Ultralytics)
- PyTorch
- OpenCV
- Flask (nếu có giao diện web)
- Dataset từ **Roboflow**

---

## 📁 Cấu trúc thư mục
waste-ai/
│
├── app.py # Chương trình chạy nhận diện
├── requirements.txt # Thư viện cần cài
├── templates/ # Giao diện (HTML)
├── datasets/ # Dataset (KHÔNG upload lên GitHub)
├── models/ # Model YOLO (.pt)
├── runs/ # Kết quả train
└── README.md

yaml
Sao chép mã

---

## 📦 Cài đặt môi trường

### 1️⃣ Tạo môi trường ảo (khuyến nghị)
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
2️⃣ Cài thư viện
bash
Sao chép mã
pip install -r requirements.txt
📊 Dataset (Roboflow)
🔗 Nguồn dataset
Dataset được lấy từ Roboflow Universe (Waste Detection):

👉 Ví dụ:

arduino
Sao chép mã
https://universe.roboflow.com/
(Bạn có thể tìm với từ khóa: waste detection, trash detection, garbage detection)

🪜 Các bước tải dataset từ Roboflow
🔹 Bước 1: Truy cập Roboflow
Vào: https://universe.roboflow.com

Đăng nhập (Google/GitHub đều được)

🔹 Bước 2: Tìm dataset
Gõ tìm kiếm: waste detection

Chọn dataset phù hợp

Nhấn Download Dataset

🔹 Bước 3: Cấu hình dataset
Format: YOLOv8

Image Size: 640 (hoặc 320 nếu train CPU)

Nhấn Download

🔹 Bước 4: Giải nén
Giải nén thư mục tải về

Đặt vào project theo cấu trúc:

bash
Sao chép mã
datasets/waste-detection-1/
│
├── train/
├── valid/
├── test/
└── data.yaml
📌 File data.yaml sẽ được dùng khi train model.

🧠 Train mô hình YOLOv8
Train nhanh trên CPU (khuyến nghị)
bash
Sao chép mã
yolo task=detect mode=train \
model=models/yolov8n.pt \
data=datasets/waste-detection-1/data.yaml \
epochs=15 \
imgsz=320 \
batch=4 \
device=cpu \
workers=2
📌 Model sau khi train xong nằm tại:

swift
Sao chép mã
runs/detect/train/weights/best.pt
▶️ Chạy chương trình nhận diện
chạy app
mã
python app.py
📌 Đảm bảo đường dẫn model đúng:

python
Sao chép mã
model = YOLO("runs/detect/train/weights/best.pt")
🚫 Lưu ý quan trọng
KHÔNG upload dataset lên GitHub

KHÔNG upload file .pt nặng

Dataset chỉ được hướng dẫn tải qua Roboflow

👨‍💻 Tác giả
Nguyễn Vũ Xuân Kiên

GitHub: https://github.com/xkien2k4

