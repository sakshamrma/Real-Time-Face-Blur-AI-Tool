## 🚀 Real-Time Face Blur AI Tool | Python + OpenCV 🔥

A real-time AI-powered face blur tool built using Python and OpenCV.
This project detects faces from your webcam and automatically blurs them to protect privacy — perfect for college projects, resumes, AI beginners, and computer vision learners.

## 🎯 Features:
🔥 Real-time face detection
🔒 Automatic face blur for privacy
👨‍💻 Works with any webcam
🤖 Uses Haarcascade or DNN AI models
🎓 Ideal for college submissions & CV projects


## 🧠 Tech Stack: 
Tool	Purpose:
🐍 Python:	Main programming language
👁️ OpenCV:	Face detection & blurring
🤖 Haarcascade / DNN: 	Pre-trained AI models
🎥 Webcam	Real-time input feed

## ⚙️ Installation: 

1️⃣ Clone the repo:
git clone https://github.com/sakshamrma/Real-Time-Face-Blur-AI-Tool
cd <Real-Time-Face-Blur-AI-Tool>

2️⃣ Install OpenCV
pip install opencv-python

3️⃣ (Optional but Recommended) Download DNN Model
Download these files and place them in your project folder:
deploy.prototxt
res10_300x300_ssd_iter_140000.caffemodel

Download from OpenCV official model repo:
https://github.com/opencv/opencv/tree/master/samples/dnn/face_detector

▶️ Usage:
Run the real-time blur script:
python3 blur_realtime.py
Press Q to exit.

## 🧩 Core Logic Snippet
for (x, y, w, h) in faces:
    face = frame[y:y+h, x:x+w]
    blur = cv2.GaussianBlur(face, (75, 75), 30)
    frame[y:y+h, x:x+w] = blur
    
This loop takes each detected face, applies a heavy blur, and places it back into the video frame.

## 🚀 Future Upgrades
🔥 Pixelated mosaic blur instead of smooth blur
🎛️ GUI version with Tkinter
📹 Blur faces in saved videos
🎯 Track & blur only selected people
🤖 Deep-learning based face detection upgrade

## 👤 Author
Saksham Sharma (CodeSham)
🎥 YouTube: https://youtube.com/@CodeSham
🐙 GitHub: https://github.com/sakshamrma

## ⭐ Support
If you like this project, please ⭐ star the repo — it motivates me to create more crazy Python projects!

## 📜 License
MIT License
