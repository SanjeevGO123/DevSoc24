# Weapon Detection System using YOLOv8
## Introduction
In an era where public safety is of paramount importance, our Weapon Detection System emerges as a groundbreaking solution. Powered by the advanced YOLOv8 model and leveraging the robustness of the PyTorch framework, our system offers real-time weapon detection with unprecedented accuracy. Designed for seamless integration with webcams and video files, this system stands as an invaluable tool for law enforcement agencies and security personnel, aiming to fortify public spaces and preemptively counteract potential threats.

## Key Features
- Real-time Detection: Instantaneously identifies weapons in live video feeds, enabling swift response to threats.
- High Accuracy: Utilizes YOLOv8's deep learning algorithms for precise weapon recognition, minimizing false positives.
- Versatile Application: Suitable for deployment in various settings, including schools, malls, and public gatherings.
- User-friendly Interface: Simplified operations for non-technical users, ensuring wide accessibility and ease of use.
- Customizable Alerts: Configurable notifications for detected threats, facilitating prompt action.

## Technology Stack
- Programming Language: Python 3.6+
- Frameworks: TensorFlow 2.0+, PyTorch, Django
- Libraries: OpenCV, Numpy


## Getting Started
### Requirements
Ensure you have the following prerequisites installed on your system:

- Python 3.6 or higher
- TensorFlow 2.0 or higher
- PyTorch
- OpenCV
- Numpy
- Django
### Installation
Jumpstart your weapon detection system setup with these simple steps:

#### Clone the Repository
```bash

git clone https://github.com/SanjeevGO123/DevSoc24.git
```
Navigate to the Project Directory
```bash
cd DevSoc24
```
#### Install Dependencies
```bash
pip install -r requirements.txt
```
#### Usage
Weapon Detection via Webcam
Activate real-time weapon detection using your webcam:

```bash
cd clientside
python main.py
```
Server-Side Deployment
Start the server to manage weapon detection processes:

```bash
cd serverside
python manage.py runserver
```
