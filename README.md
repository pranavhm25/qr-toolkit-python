![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)

# QR Toolkit (Python)

A **command-line QR toolkit built with Python** that can generate and scan QR codes using images or a live webcam.
This project demonstrates practical use of **image processing, computer vision, CLI design, and Python libraries**.

It allows users to generate customized QR codes for different data types and scan QR codes from both images and a webcam feed.

---

# Features

### QR Code Generation

* Generate QR codes for multiple data types:

  * Website URLs
  * Plain text
  * Phone numbers
  * Email addresses
  * WiFi credentials
* Choose a **custom file name**
* Customize **QR color and background color**
* Adjust **QR size and border**
* **Preview QR code before saving**
* Automatically stores generated QR codes in a dedicated folder

---

### QR Code Scanning

* Scan QR codes from an **image file**
* **Live webcam QR scanner**
* Detects and decodes QR codes in real time
* Displays decoded data on the video feed
* Draws bounding boxes around detected QR codes

---

### Error Handling

The application includes validation and error handling for:

* Invalid file paths
* Invalid numeric input
* Camera access failure
* Missing QR codes in scanned images

---

# Technologies Used

| Technology | Purpose                            |
| ---------- | ---------------------------------- |
| Python     | Core programming language          |
| qrcode     | Generate QR codes                  |
| Pillow     | Image processing                   |
| OpenCV     | Webcam access and video processing |
| pyzbar     | QR code decoding                   |
| Git        | Version control                    |
| GitHub     | Project hosting                    |

---

# Project Structure

```
qr-toolkit-python
│
├── main.py
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── generated_qr
│
└── venv
```

### Explanation

* **main.py** -> Main application script
* **generated_qr/** -> Stores generated QR images
* **requirements.txt** -> List of project dependencies
* **.gitignore** -> Prevents unnecessary files from being pushed
* **venv/** -> Virtual environment (ignored by Git)

---

# Installation

Follow these steps to run the project locally.

## 1. Clone the Repository

```
git clone https://github.com/pranavhm25/qr-toolkit-python.git
cd qr-toolkit-python
```

---

## 2. Create a Virtual Environment

```
python -m venv venv
```

---

## 3. Activate the Virtual Environment

### Windows (Command Prompt)

```
venv\Scripts\activate
```

### Windows (PowerShell)

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

---

## 4. Install Required Libraries

```
pip install -r requirements.txt
```

---

# Running the Application

Run the program using:

```
python main.py
```

You will see the menu:

```
QR TOOLKIT

1. Generate QR Code
2. Scan QR from Image
3. Live QR Scanner (Webcam)
4. Exit
```

---

# Usage

## Generate QR Code

Steps:

1. Select **Generate QR Code**
2. Choose the data type
3. Enter the required information
4. Customize color and size
5. Preview the QR code
6. Save the QR code if satisfied

Generated QR codes will be stored inside:

```
generated_qr/
```

---

## Scan QR from Image

Steps:

1. Choose **Scan QR from Image**
2. Enter the path to the image file
3. The program decodes and prints the QR data

Example:

```
Decoded Data:
https://github.com
```

---

## Live QR Scanner (Webcam)

Steps:

1. Choose **Live QR Scanner**
2. The webcam will open
3. Point the camera at a QR code
4. The decoded data will appear on the video feed

To exit:

```
Press Q
or close the scanner window
```

---

# Example Use Cases

This tool can be used for:

* Sharing website links
* Sharing contact information
* Creating WiFi login QR codes
* Testing QR codes
* Building automation tools
* Learning computer vision basics

---

# Future Improvements

Planned improvements for this project include:

* QR codes with **embedded logos**
* **Batch QR generation** from CSV files
* **QR generation history log**
* **GUI version using Tkinter**
* **Web version using Flask**
* Automatic opening of detected URLs in the browser

---

# Requirements

Dependencies used in this project:

```
qrcode
opencv-python
pyzbar
pillow
```

These are automatically installed using:

```
pip install -r requirements.txt
```

---

# License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute the code with proper attribution.

---

# Author

**H M Pranav**

Information Science & Engineering Student
MS Ramaiah Institute of Technology, Bangalore

GitHub:
https://github.com/pranavhm25

---

# Contributing

Contributions, suggestions, and improvements are welcome.

If you want to contribute:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

# Acknowledgements

Thanks to the open-source libraries used in this project:

* qrcode
* OpenCV
* pyzbar
* Pillow

They make QR code generation and scanning simple and powerful in Python.
