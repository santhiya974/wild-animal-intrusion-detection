from ultralytics import YOLO
import cv2
import math
import smtplib
from email.mime.text import MIMEText
import threading
import pygame

# Initialize pygame mixer for sound playback
pygame.mixer.init()

# Function to send email notification
def send_email(animal):
    sender_email = "sender@gmail.com"
    receiver_email = "receiver@gmail.com"
    password = "abcd efgh ijkl mboof"  # Use App Password if 2FA is enabled

    subject = f"Animal Detected: {animal}"
    body = f"The following animal has been detected: {animal}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f"Email sent: {subject}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Lock for controlling sound playback
sound_lock = threading.Lock()

# Function to play sound
def play_sound():
    with sound_lock:
        # Load and play sound asynchronously
        sound = pygame.mixer.Sound('C:\\Users\\santh\\Downloads\\siren-alert-96052.mp3')  # Replace with your sound file
        sound.play()
        # Wait for sound to finish playing before releasing lock
        while pygame.mixer.get_busy():
            pygame.time.wait(100)

# Running real-time from webcam
cap = cv2.VideoCapture(0)

model = YOLO('D:\\Wildlife-Conservation-Detection-main\\best.pt')
classnames = [
    'antelope', 'bear', 'cheetah', 'human', 'coyote', 'crocodile', 'deer', 'elephant', 'flamingo',
    'fox', 'giraffe', 'gorilla', 'hedgehog', 'hippopotamus', 'hornbill', 'horse', 'hummingbird', 'hyena',
    'kangaroo', 'koala', 'leopard', 'lion', 'meerkat', 'mole', 'monkey', 'moose', 'okapi', 'orangutan',
    'ostrich', 'otter', 'panda', 'pelecaniformes', 'porcupine', 'raccoon', 'reindeer', 'rhino', 'rhinoceros',
    'snake', 'squirrel', 'swan', 'tiger', 'turkey', 'wolf', 'woodpecker', 'zebra'
]

running = True

while running:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    frame = cv2.resize(frame, (640, 480))
    
    result = model(frame, stream=True)

    for info in result:
        boxes = info.boxes
        for box in boxes:
            confidence = box.conf[0]
            confidence = math.ceil(confidence * 100)
            class_index = int(box.cls[0])

            if confidence > 50 and class_index < len(classnames):
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
                cv2.putText(frame, f'{classnames[class_index]} {confidence}%', (x1 + 8, y1 + 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                # Play buzzer sound in a separate thread
                threading.Thread(target=play_sound, daemon=True).start()

                # Send email notification in separate thread
                threading.Thread(target=send_email, args=(classnames[class_index],), daemon=True).start()

    cv2.imshow('Animal Detection', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
        running = False
        break

cap.release()
cv2.destroyAllWindows()

# Stop all sounds and quit mixer on exit
pygame.mixer.stop()
pygame.mixer.quit()




