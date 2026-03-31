# 🎯 Computer Vision Attendance System

## 📌 Overview
This project is an automated attendance system using **Face Recognition**. It detects and recognizes faces in real-time using a webcam and marks attendance with timestamps.

## 🚀 Features
- Real-time face detection & recognition
- Automated attendance logging
- No manual intervention
- Reduces proxy attendance
- Easy to use and setup

## 🛠 Tech Stack
- Python
- OpenCV
- face_recognition
- NumPy

## 📂 Project Structure
```
├── main.py
├── requirements.txt
├── README.md
```

## ⚙️ Installation

```bash
git clone https://github.com/10162-glitch/cv-attendance-system.git
cd cv-attendance-system
pip install -r requirements.txt
```

## ▶️ Usage

```bash
python main.py
```

- Make sure webcam is enabled
- Add known faces before running system

## 🧠 How It Works
1. Capture video from webcam
2. Detect faces using OpenCV
3. Encode faces using face_recognition
4. Match with known dataset
5. Mark attendance with timestamp

## ⚠️ Challenges
- Lighting conditions
- Face angles
- Performance optimization

## 🔮 Future Improvements
- GUI interface
- Cloud database
- Mobile integration

## 🤝 Contribution
Feel free to fork and improve this project.

## 📜 License
For educational use only.
