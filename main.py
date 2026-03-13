import qrcode
import cv2
from pyzbar.pyzbar import decode
import os
import numpy as np

folder = "generated_qr"
if not os.path.exists(folder):
    os.makedirs(folder)

def generate_qr():
    print("\nSelect data type:")
    print("1. Website URL")
    print("2. Plain Text")
    print("3. Phone Number")
    print("4. Email")
    print("5. WiFi")

    choice = input("Enter choice: ").strip()
    if choice == "1":
        data = input("Enter URL: ").strip()
    elif choice == "2":
        data = input("Enter text: ").strip()
    elif choice == "3":
        phone = input("Enter phone number: ").strip()
        data = f"tel:{phone}"
    elif choice == "4":
        email = input("Enter email: ").strip()
        data = f"mailto:{email}"
    elif choice == "5":
        ssid = input("Enter WiFi name (SSID): ").strip()
        password = input("Enter WiFi password: ").strip()
        security = input("Security type (WPA/WEP): ").strip()
        data = f"WIFI:T:{security};S:{ssid};P:{password};;"
    else:
        print("Invalid choice.")
        return

    file_name = input("Enter file name (without extension): ").strip()  #File name input
    if file_name == "":
        print("File name cannot be empty.")
        return
    file_path = os.path.join(folder, file_name + ".png")

    fill = input("Enter QR color (default black): ").strip()    #Color input
    bg = input("Enter background color (default white): ").strip()
    if fill == "":
        fill = "black"
    if bg == "":
        bg = "white"

    try:    #Size input with error handling
        box = int(input("Enter box size (recommended 8-12): "))
        border = int(input("Enter border size (recommended 4): "))
    except ValueError:
        print("Invalid size input. Using default values.")
        box = 10
        border = 4

    try:    #QR code generation with error handling
        qr = qrcode.QRCode(
            version=1,
            box_size=box,
            border=border
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill, back_color=bg)

        print("\nPreviewing QR Code...")
        img.show()

        save = input("Save this QR code? (y/n): ").lower()
        if save == "y":
            img.save(file_path)
            print("QR Code saved at:", file_path)
        else:
            print("QR code not saved.")

    except Exception as e:
        print("Error generating QR code:", e)


def scan_qr():
    path = input("Enter image path: ").strip()  #File path input
    if not os.path.exists(path):
        print("File not found.")
        return
    img = cv2.imread(path)  #Read image using OpenCV
    if img is None:
        print("Invalid image file.")
        return

    decoded_objects = decode(img)   #Decode QR code from image
    if not decoded_objects:
        print("No QR code detected.")
        return
    print("\nDecoded Data:")
    for obj in decoded_objects:
        print(obj.data.decode("utf-8"))


def live_scan():
    import webbrowser
    print("\nOpening webcam... Press 'q' to quit or close the window")

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cv2.namedWindow("QR Scanner", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("QR Scanner", cv2.WND_PROP_TOPMOST, 1)

    opened_links = set()  # prevents opening the same link repeatedly
    while True:
        ret, frame = cap.read() #Capture webcam feed
        if not ret:
            print("Failed to access camera.")
            break

        decoded_objects = decode(frame)
        for obj in decoded_objects:
            data = obj.data.decode("utf-8") #Decode QR code data from webcam feed
            print("Detected:", data)

            if data.startswith("http") and data not in opened_links: #Open URLs in browser and keep track of opened links to avoid duplicates
                print("Opening link in browser...")
                webbrowser.open(data)
                opened_links.add(data)

            points = obj.polygon
            pts = [(p.x, p.y) for p in points]

            if len(pts) > 4:
                hull = cv2.convexHull(np.array(pts, dtype=np.float32))
                pts = [(int(x[0][0]), int(x[0][1])) for x in hull]

            for i in range(len(pts)):
                cv2.line(frame, pts[i], pts[(i + 1) % len(pts)], (0, 255, 0), 2)

            corner_length = 20
            for (x, y) in pts:
                cv2.line(frame, (x, y), (x + corner_length, y), (0, 255, 255), 3)
                cv2.line(frame, (x, y), (x, y + corner_length), (0, 255, 255), 3)

            n = len(points)
            for j in range(n):
                cv2.line(frame, points[j], points[(j + 1) % n], (0, 255, 0), 3)

            x, y = pts[0]
            cv2.putText(
                frame,
                data,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )   #Display decoded data above the QR code in the webcam feed

        cv2.imshow("QR Scanner", frame) #Display webcam feed with detected QR codes highlighted

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        if cv2.getWindowProperty("QR Scanner", cv2.WND_PROP_VISIBLE) < 1:   #Check if window is closed
            break

    cap.release()
    cv2.destroyAllWindows()


def menu():
    while True:
        print("\nQR TOOLKIT")
        print("1. Generate QR Code")
        print("2. Scan QR from Image")
        print("3. Live QR Scanner (Webcam)")
        print("4. Exit")

        option = input("Select an option: ").strip()

        if option == "1":
            generate_qr()
        elif option == "2":
            scan_qr()
        elif option == "3":
            live_scan()
        elif option == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    menu()