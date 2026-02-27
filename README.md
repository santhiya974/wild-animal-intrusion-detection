# 🐾 Wild Animal Detection in Restricted Area

This project is a real-time wild animal detection system built using YOLO and OpenCV.  
It detects animals from live webcam input and triggers alerts when an animal is identified.

The system is designed to help monitor restricted areas and improve safety by providing instant detection and notifications.

---

## 🚀 Features

- Real-time detection using webcam
- YOLO model for object detection
- Displays bounding boxes with confidence score
- Plays siren sound when an animal is detected
- Sends automatic email alert with detected animal name
- Works with trained custom model (.pt file)

---

## 🛠️ Tech Stack

- Python
- OpenCV
- Ultralytics YOLO
- Pygame (for sound alert)
- SMTP (for email notification)
- Threading (for background alerts)

---

## ⚙️ How It Works

1. Captures live video from webcam.
2. Uses trained YOLO model (`best.pt`) to detect animals.
3. If confidence > 50%, it:
   - Draws bounding box
   - Displays animal name + confidence
   - Plays alert sound
   - Sends email notification

---

## ▶️ How to Run

1. Clone the repository:https://github.com/santhiya974/wild-animal-intrusion-detection.git

2. Install required packages:
2. Install required packages:eg: pip install ultralytics opencv-python pygame

3. Place your trained model file (`best.pt`) inside the project folder.

4. Update:
- Email credentials
- Sound file path
- Model path

5. Run the script:python filename.py

---

## 📧 Email Alert

When an animal is detected, the system automatically sends an email notification with the detected animal name.

---

## 📷 Output

(Add screenshots of detection output here)

---

## 📌 Use Case

- Forest border monitoring  
- Wildlife conservation  
- Restricted area security  
- Human-animal conflict prevention  

---

## 🔮 Future Improvements

- Add SMS notification  
- Deploy on Raspberry Pi  
- Add admin dashboard  
- Store detection logs in database  
