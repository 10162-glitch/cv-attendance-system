# Automated Vision-Based Attendance System

## Project Overview
A Computer Vision application designed to automate the classroom attendance process. It utilizes facial recognition to identify students from a live camera feed and logs their presence into a CSV file with precise timestamps. This serves as the Bring Your Own Project (BYOP) submission for the Computer Vision course.

## Problem Solved
Manual attendance in large lectures is inefficient, time-consuming, and susceptible to proxy attendance. This project provides a frictionless, automated alternative that recovers valuable teaching time.

## Technologies Used
* **Python 3.x**
* **OpenCV:** For real-time image processing and webcam feed handling.
* **face_recognition (Dlib):** For extracting 128D facial encodings and matching them against known images.
* **Pandas / Standard CSV:** For data logging and storage.

## Setup and Installation
1. Clone the repository: 
   ```bash
   git clone https://github.com/10162-glitch/cv-attendance-system.git
