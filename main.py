import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime

# 1. Setup paths and variables
path = 'known_faces'
images = []
classNames = []
myList = os.listdir(path)

# 2. Load images and extract names
print("Loading known faces...")
for cl in myList:
    # Skip hidden files
    if cl.startswith('.'):
        continue
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(f"Loaded faces for: {classNames}")

# 3. Function to encode loaded images
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        try:
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        except IndexError:
            print("Warning: No face found in one of the known_faces images.")
    return encodeList

encodeListKnown = findEncodings(images)
print('Encoding Complete.')

# 4. Function to log attendance
def markAttendance(name):
    # Create file if it doesn't exist
    if not os.path.isfile('attendance.csv'):
        with open('attendance.csv', 'w') as f:
            f.write('Name,Time,Date\n')
            
    with open('attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            
        # Only log if they haven't been logged yet today (simplified)
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            dateString = now.strftime('%Y-%m-%d')
            f.writelines(f'\n{name},{dtString},{dateString}')

# 5. Initialize Webcam
cap = cv2.VideoCapture(0)

print("Starting webcam... Press 'q' to quit.")
while True:
    success, img = cap.read()
    if not success:
        break
        
    # Resize frame for faster processing
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Find faces in current frame
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            
            # Scale face locations back up
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            
            # Draw box and text
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            
            markAttendance(name)

    cv2.imshow('Webcam Attendance', img)
    
    # Break loop on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
